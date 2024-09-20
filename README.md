# Ephemera - A Private Chatroom Web App
Video Demo: [URL HERE]
#### Description:
Ephemera is a private chatroom app designed for users who want to interact without sharing personal details like social media accounts or phone numbers. By simply sharing a code, you can create or join chatrooms to communicate securely with others. This app aims to address the growing concerns around privacy and cybersecurity by providing an anonymous space for conversations.

#### Features:
Private Chatrooms: Join or create chatrooms using unique codes for secure, invite-only communication.
Temporary Rooms: Once all participants leave, the chatroom and all messages disappear, ensuring your conversations are temporary.
User-Friendly Interface: Easy-to-navigate design for seamless chat experience.

#### Technologies Used:
Backend: Flask, Python
Real-Time Communication: Flask-SocketIO
Frontend: HTML, CSS, JavaScript
Database: SQLite3 (temporary for future scaling options)

#### Installation and Setup:
Clone the repository:
```
git clone <repository-url>
```
Navigate to the project directory:
```
cd ephemera
```
Install dependencies:
```
pip install -r requirements.txt
```
Run the app:
```
flask run
```

#### Usage:
Visit the homepage.
Enter a chatroom code or create a new one.
Share the code with others to join the room.
Leave the chatroom when done, and the room is deleted once everyone exits.

### Future Scope:
1. End-to-End Encryption: Implement encryption to ensure all conversations are completely private and secure.
2. Login-Specific Features: Introduce optional login functionality for users who want more personalized features.
3. Mobile Optimization: Enhance the app's responsiveness and performance for mobile devices.
Persistent Rooms (Optional): Option to create rooms that persist even after all participants have left, with the ability to reopen them later.
4. Advanced Moderation Tools: Provide room creators with admin privileges to manage participants, control access, and monitor chat activity.
5. File Sharing: Allow users to share files securely within a chatroom, enhancing collaboration and communication.
6. Notification System: Introduce real-time notifications for incoming messages and room invites.

#### Note:
This project is a personal passion project and should not be used in real-world scenarios. There may or may not be changes implementing the features mentioned in the Future Scope.

#### Contributing:
Feel free to fork the repository and submit pull requests. If you encounter any issues, you can open an issue to discuss.