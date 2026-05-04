from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, auth
from datetime import datetime

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


# ---------------- ROOT ROUTE ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Cloud Assignment 8 Backend is running 🚀",
        "status": "OK",
        "available_endpoints": {
            "POST /verify": "Verify Firebase ID Token"
        }
    })


# ---------------- HEALTH CHECK ----------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "server": "Running",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


# ---------------- VERIFY TOKEN ----------------
@app.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.get_json()
        id_token = data.get('token')

        if not id_token:
            return jsonify({"error": "Token missing"}), 400

        # Verify Firebase ID token
        decoded_token = auth.verify_id_token(id_token)

        uid = decoded_token['uid']
        email = decoded_token['email']

        print("\nUser Verified:")
        print("UID:", uid)
        print("Email:", email)

        return jsonify({
            "status": "success",
            "message": "User verified successfully",
            "uid": uid,
            "email": email
        })

    except Exception as e:
        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 401


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(port=5000)