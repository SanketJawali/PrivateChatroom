import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from random import choice
from string import ascii_letters, digits
from flask_socketio import SocketIO, leave_room, join_room, send, emit
from datetime import timedelta

# Configure application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_code'
socketio = SocketIO(app)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

data = sqlite3.connect("userdata.db", check_same_thread = False)
db = data.cursor()

# Active chatrooms
rooms = {}


def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += choice(ascii_letters  + digits)
        
        if code not in rooms:
            break
    
    return code


@app.route("/create", methods=["GET", "POST"])
def create():
    """ Create a room """ 

    # Setting the session to permanent to make it valid for 7 days
    session.permanent = True

    # Check if there is already a room code in the session
    if "room" in session and session["room"] in rooms:
        room = session["room"]
        return render_template("room.html", code=room)

    if request.method == "POST":
        nickname = request.form.get("nickname")
        participants = request.form.get("participants")

        if not nickname or not participants:
            session["create_error"] = "Missing Nickname or Participant count"
            if session.get("username"):
                return redirect("/index")
            return redirect("/")            

        # if session.get("room") is None:
        room = generate_unique_code(6)
        rooms[room] = {"participants": 0, "messages": [], "members": [], "maxParticipants": int(participants)}

        # Storing the data in session
        session["nickname"] = nickname
        session["room"] = room
        return redirect(url_for("room"))

    return redirect("/index", username=session["username"])


@app.route("/")
def homepage():
    """ View Homepage """

    create_error = ""
    create_error = session.pop("create_error", None)

    join_error = ""
    join_error = session.pop("join_error", None)

    return render_template("homepage.html", join_error=join_error, create_error=create_error)


@app.route("/index")
def index():
    """ Display index page after login """

    create_error = ""
    create_error = session.pop("create_error", None)

    join_error = ""
    join_error = session.pop("join_error", None)

    common_error = ""
    common_error = session.pop("error_message", None)

    return render_template("index.html", username=session.get("username"), join_error=join_error, create_error=create_error, common_error=common_error)


@app.route("/join", methods=["GET", "POST"])
def join():
    """ Join a room with a code """

    session.permanent = True

    if request.method == "POST":
        nickname = request.form.get("nickname")
        room = request.form.get("chatroom_code")

        if not nickname or not room:
            session["join_error"] = "Missing Nickname or Room Code"
            if session.get("username"):
                return redirect("/index")
            return redirect("/")
        
        if room not in rooms:
            session["join_error"] = "Enter a valid Room Code"
            if session.get("username"):
                return redirect("/index")
            return redirect("/")
        
        if rooms[room]["participants"] == rooms[room]["maxParticipants"]:
            session["join_error"] = "Room is currently full"
            if session.get("username"):
                return redirect("/index")
            return redirect("/")
        
        session["nickname"] = nickname
        session["room"] = room

        return redirect(url_for("room"))

    if session.get("username"):
        return redirect(url_for("index"))
    return redirect("/")


@app.route("/leave")
def leave():
    """ Leave the room and redirect to index page """

    room = session.get("room")
    name = session.get("nickname")
    
    if room and room in rooms:
        if name in rooms[room]["members"]:
            rooms[room]["members"].remove(name)
            rooms[room]["participants"] -= 1
        
        if rooms[room]["participants"] <= 0:
            del rooms[room]
    
    # Clear the room and nickname session data
    session.pop("room", None)
    session.pop("nickname", None)

    return redirect("/index")


@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in """

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return render_template("login.html", error = "Must provide username")

        # Ensure password was submitted
        elif not password:
            return render_template("login.html", error = "Must provide password", username = username)

        # Query database for username
        user = db.execute("SELECT id, pass FROM users WHERE username = ?;", (username,)).fetchone()
        # user[0] = "id" 
        # user[1] = "pass"       
        
        # Ensure username exists and password is correct
        if user is None or not check_password_hash(user[1], password):
            return render_template("login.html", error = "Invalid username and/or password", username = username, password = password)

        session["user_id"] = user[0]
        session["username"] = username

        # Redirect user to home page
        return redirect("/index")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """ Log user out """

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register user """

    # If form submited
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        # Apology if any of the inputs are blank
        if not username or not password or not confirm_password:
            return render_template("register.html", error="Please enter the required details", username=username)

        # Return error if password less than 8 char long
        if len(password) < 6 or len(password) > 20:
            return render_template("register.html", error="Password must be between 6 and 20 characters long", username=username)

        # Error if password didn't match
        if password != confirm_password:
            return render_template("register.html", error="Password didn't match", username=username)

        # Error if username already taken
        # The below sql quere outputs a dictionary, checking if the first elements value is 0
        user = db.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,)).fetchone()
        if user[0] != 0:
            return render_template("register.html", error="Username taken", username=username)

        # Generating a hash of the password
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)

        # Insert the new user into the database
        db.execute("INSERT INTO users (username, pass) VALUES (?, ?)", (username, password_hash))
        data.commit()

        # Render homepage
        return redirect("/login")

    # Via get method
    else:
        return render_template("register.html")


@app.route("/room")
def room():
    """ Entering the chatroom """

    room = session.get("room")
    
    # Ensure that the room code is valid and exists in the `rooms` dictionary
    if room not in rooms:
        session["common_error"] = "Room does not exist"
        if session.get("username"):
            return redirect("/index")
        return redirect("/")

    return render_template("room.html", code=room)  


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    # Emit the list of members
    emit("update_members", list(rooms[room]["members"]), to=request.sid)
    
    content = {
        "name": session.get("nickname"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)


@socketio.on("connect")
def connect():
    room = session.get("room")
    name = session.get("nickname")

    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({"name": name, "message": "Entered the room"}, to=room)
    rooms[room]["participants"] += 1
    rooms[room]["members"].append(name)
    # print(rooms[room])
    
    # Emit the list of members and past messages
    emit("update_members", list(rooms[room]["members"]), to=room)
    emit("past_messages", list(rooms[room]["messages"]), to=request.sid)



@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("nickname")
    leave_room(room)

    if room in rooms:
        if name in rooms[room]["members"]:
            rooms[room]['members'].remove(name)
        
        rooms[room]["participants"] -= 1

        send({"name": name, "message": "has left the room"}, to=room)
        emit("update_members", list(rooms[room]["members"]), to=room)
    
        if rooms[room]["participants"] <= 0:
            print(f"{room} deleted")
            # print(rooms[room])
            del rooms[room]
            return
    

if __name__ == "__main__":
    socketio.run(app)
