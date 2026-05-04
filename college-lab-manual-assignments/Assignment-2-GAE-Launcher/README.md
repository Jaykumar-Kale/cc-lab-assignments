# Assignment 2 – Launching Web Application using Google App Engine (GAE Launcher Equivalent)

## 📌 Objective
To launch a web application using Google App Engine launcher functionality through Google Cloud SDK.

---

## 🧠 Introduction

Earlier versions of Google App Engine used a GUI-based tool called **GAE Launcher** to start and deploy applications.

In modern Google Cloud environments, the launcher functionality is replaced by the **Google Cloud SDK CLI tools**.

The equivalent modern command for launching/deploying an application is:

gcloud app deploy

---

## 🏗 Conceptual Workflow

Application Files → app.yaml → Google Cloud SDK → App Engine Runtime

The deployment process performs the following steps:

1. Reads `app.yaml`
2. Identifies runtime (python311)
3. Installs dependencies from `requirements.txt`
4. Creates runtime container
5. Deploys application to App Engine

---

## 📁 Project Structure

Assignment-2-GAE-Launcher/

- main.py
- app.yaml
- requirements.txt
- README.md

---

## ⚙️ Technologies Used

- Python 3.11
- Flask
- Google Cloud SDK (CLI)
- Google App Engine Configuration
- Git & GitHub

---

## 🚀 Steps Performed

### 1️⃣ Navigate to Project Folder

cd D:\cc-lab-assignments\Assignment-2-GAE-Launcher

### 2️⃣ Attempt Deployment Using CLI

gcloud app deploy

This command acts as the modern replacement for the old GAE Launcher.

---

## ⚠ Important Note

Deployment requires an active billing account attached to the Google Cloud project.

Since billing was not enabled, full cloud deployment was not completed. However, the launcher functionality and deployment workflow were demonstrated successfully using Google Cloud SDK.

---

## 🔄 Difference Between Assignment 1 and Assignment 2

Assignment 1:
python main.py  
(Local Flask development server)

Assignment 2:
gcloud app deploy  
(App Engine deployment process using Cloud SDK)

---

## 🎓 Viva Questions & Answers

Q1. What was GAE Launcher?  
A GUI tool used in older versions of App Engine to manage and deploy applications.

Q2. What replaced GAE Launcher?  
Google Cloud SDK CLI tools.

Q3. What does `gcloud app deploy` do?  
It reads configuration files, installs dependencies, prepares runtime environment, and deploys the application to App Engine.

Q4. Why was deployment not fully completed?  
Because Google Cloud requires an active billing account to enable App Engine services.

---

## ✅ Conclusion

Successfully demonstrated modern Google App Engine launcher functionality using Google Cloud SDK. Understood deployment workflow, configuration management, and runtime environment setup in App Engine architecture.
