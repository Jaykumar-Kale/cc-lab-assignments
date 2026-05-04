# Cloud Computing Lab – Assignment 8
## Firebase Authentication + Flask Backend + Token Verification

---

## 📌 Assignment Title
Design an application to retrieve, verify, and store user credentials using Firebase Authentication, Google App Engine Standard Environment, and Google Cloud Datastore.

(Current implementation runs locally without billing.)

---

## 🎯 Objective

This project demonstrates:

1. User authentication using Firebase Authentication.
2. Secure token-based authentication using JWT (ID Token).
3. Backend token verification using Firebase Admin SDK.
4. REST API development using Flask.
5. Cloud-based architecture design pattern.

---

## 🏗 System Architecture

User (Browser)
        ↓
Firebase Client SDK (Login/Register)
        ↓
Firebase Authentication Server
        ↓
JWT ID Token Generated
        ↓
Frontend sends token to Backend API
        ↓
Flask Backend verifies token
        ↓
User is authenticated securely

---

## 🔐 Authentication Flow

Step 1: User registers or logs in using Firebase client SDK.

Step 2: Firebase generates a secure JWT ID token.

Step 3: Frontend sends this token to backend via POST request.

Step 4: Backend verifies token using Firebase Admin SDK.

Step 5: If token is valid → user is authenticated successfully.

---

## 🛠 Technologies Used

Frontend:
- HTML
- JavaScript
- Firebase Client SDK (v8)

Backend:
- Python
- Flask
- Flask-CORS
- Firebase Admin SDK

Cloud Platform:
- Firebase Authentication
- Token-Based Authentication (JWT)

---

## 📁 Project Structure

Assignment-8-firebase-appengine/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── serviceAccountKey.json (NOT uploaded to GitHub)
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md

---

## ▶️ How to Run the Project

### Step 1 – Run Backend

cd backend
python -m venv venv
venv\Scripts\activate   (Windows)
pip install -r requirements.txt
python main.py

Backend runs on:
http://127.0.0.1:5000

---

### Step 2 – Run Frontend

Open new terminal:

cd frontend
python -m http.server 5500

Open in browser:
http://127.0.0.1:5500

---

## 🧪 Testing Steps

1. Enter Email and Password.
2. Click Register (first time).
3. Click Login.
4. Backend terminal will show:

User Verified:
UID: XXXXX
Email: XXXXX

5. Browser shows success JSON response.

---

## 📡 API Endpoints

GET  /  
→ Returns backend status message.

GET  /health  
→ Returns server health check.

POST /verify  
→ Verifies Firebase ID token.

---

## 🔑 Security Concept Used

Token-Based Authentication (JWT)

• Password is never sent to backend.
• Firebase handles password securely.
• Backend verifies ID token.
• Only verified tokens are accepted.

This prevents:
- Password leakage
- Session hijacking
- Direct database access

---

## ☁ Cloud Concepts Demonstrated

✔ Authentication as a Service  
✔ Backend as a Service  
✔ RESTful API  
✔ Token Verification  
✔ Secure Cloud Architecture  
✔ Separation of Client and Server  

---

## 🧠 Viva Explanation (Short Version)

"User authenticates using Firebase client SDK.  
Firebase generates a JWT ID token.  
Frontend sends this token to Flask backend.  
Backend verifies token using Firebase Admin SDK.  
If token is valid, user is authenticated successfully."

---

## 🧠 Viva Explanation (Detailed Version)

1. We are using Firebase Authentication to handle user login and registration.
2. After successful login, Firebase generates an ID token (JWT).
3. This token is sent to the backend via a REST API.
4. Backend verifies token using Firebase Admin SDK.
5. Only verified users are processed.
6. This ensures secure cloud-based authentication without handling passwords manually.

---

## 🚀 Future Enhancements

• Store user login time in Firestore.
• Deploy backend to Google App Engine.
• Integrate Google Cloud Datastore.
• Add role-based authentication.

---

## ⚠ Important Note

serviceAccountKey.json is not uploaded to GitHub for security reasons.

Never share private keys publicly.

---

## ✅ Conclusion

This project successfully demonstrates secure cloud authentication architecture using:

- Firebase Authentication
- Flask Backend
- Token Verification
- Cloud-based design pattern

This implementation follows real-world industry authentication flow.

---

END OF README