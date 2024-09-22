# Ephemera - A Private Chatroom Web App
Video Demo: https://youtu.be/emQ_uM9wSzg

#### Description:
Ephemera is a private chatroom app designed for users who want to interact without sharing personal details like social media accounts or phone numbers. By simply sharing a code, you can create or join chatrooms to communicate securely with others. This webapp aims to address the growing concerns around privacy and cybersecurity by providing an anonymous space for conversations.

#### Features:
##### Private Chatrooms: 
Ephemera allows users to create or join private chatrooms using unique invitation codes. These chatrooms are designed for one-on-one or small group conversations, ensuring that only those with the code can enter, making your communication completely private.
In an era of increasing privacy concerns, Ephemera addresses these issues by allowing users to chat without the need to reveal personal details such as phone numbers or social media profiles. The platform does not require account creation, further reducing your digital footprint and protecting your anonymity. Whether you're having a sensitive conversation or just chatting casually, Ephemera ensures that your discussions remain private and secure.

##### Temporary Rooms: 
One of Ephemera's core privacy features is its temporary chatrooms. All conversations and messages are automatically deleted when all participants leave the room, ensuring that nothing is stored or retrievable after the chat ends.
This feature eliminates the worry of long-term data storage or leaks, allowing you to speak freely without fear of your words being saved or shared later. Whether you're discussing confidential information or having a casual talk, you can feel secure knowing that everything will be wiped clean once the conversation concludes. It’s ideal for those who prioritize short-lived, secure communication.
##### User-Friendly Interface: 
Ephemera has been designed with simplicity and ease of use in mind, ensuring that users can navigate and engage with the platform without technical challenges. The interface is intuitive, making it accessible even to those with limited tech experience. From creating or joining chatrooms to managing participants, every action is straightforward and requires minimal effort.

#### Technologies Used:
Backend: Flask, Python

Real-Time Communication: Flask-SocketIO

Frontend: HTML, CSS, JavaScript

Database: SQLite3 (temporary for future scaling options)

#### Installation and Setup:
Clone the repository:
```
git clone https://github.com/SanketJawali/PrivateChatroom
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
After running the above commands, the web app will open in your local browser. Open another tab in incognito mode (the other tab must be in incognito mode for it to work).
You can either log in/register or create a room on the homepage by entering a nickname. You can also set the maximum number of participants in the room, between 2 and 8. Once you’ve configured the room, click "Create."
After clicking 'Create,' you will be directed to your chatroom, where the room code will be displayed at the top. This code can be shared with anyone whom you wish to have a conversation with.
Once you are done with the conversation you can just leave the room by clicking the Leave Room button the left side of the site below the member list. Once all the participants of the room leave the room will automatically get deleted.

### Future Scope:
1. End-to-End Encryption: Implement encryption to ensure all conversations are completely private and secure.
2. Login-Specific Features: Introduce optional login functionality for users who want more personalized features.
3. Persistent Rooms: Option to create rooms that persist even after all participants have left, with the ability to reopen them later.
4. Advanced Moderation Tools: Provide room creators with admin privileges to manage participants, control access, and monitor chat activity.
5. File Sharing: Allow users to share files securely within a chatroom, enhancing collaboration and communication.
6. Notification System: Introduce real-time notifications for incoming messages and room invites.

#### Note:
This project is a personal passion project and is not intended for real-world use. The features mentioned in the "Future Scope" section may or may not be implemented. Currently, this project can only be run on a single device, meaning you cannot invite others to join your chatrooms. I aim to publish this project on a server after implementing more features like end-to-end encryption and special login functionality.

#### Contributing:
This is a passion project and is licensed under the MIT License. Feel free to fork or clone this repository and use it as you wish. You're also welcome to submit any issues or pull requests. I’d be happy to collaborate with anyone willing to share their knowledge and contribute to the project.
