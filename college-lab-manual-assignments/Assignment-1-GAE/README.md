# Assignment 1 – Installation of Google App Engine and Hello World Application

## 📌 Objective
To install Google App Engine and develop a simple Hello World web application using Python.

---

## 🧠 Introduction
Google App Engine (GAE) is a Platform as a Service (PaaS) provided by Google Cloud. It allows developers to build and deploy scalable web applications without managing servers or infrastructure.

PaaS provides:
- Runtime environment
- Deployment tools
- Automatic scaling
- Load balancing
- Managed infrastructure

---

## 🏗 Architecture Overview
Client (Browser) → Flask Application → Google App Engine Runtime

In this assignment, the application is developed locally using Flask and configured for deployment using app.yaml.

---

## 📁 Project Structure

Assignment-1-GAE/
│
├── main.py
├── app.yaml
├── requirements.txt
├── venv/ (not pushed to GitHub)
└── README.md

---

## ⚙️ Technologies Used
- Python 3.11
- Flask Framework
- Google App Engine Configuration (app.yaml)
- Git & GitHub
- Virtual Environment (venv)

---

## 🚀 Steps to Run the Application Locally

1. Clone the repository:
   git clone https://github.com/Jaykumar-Kale/cc-lab-assignments.git

2. Navigate to the assignment folder:
   cd cc-lab-assignments/Assignment-1-GAE

3. Create a virtual environment:
   python -m venv venv

4. Activate virtual environment (PowerShell):
   .\venv\Scripts\activate

5. Install dependencies:
   pip install -r requirements.txt

6. Run the application:
   python main.py

7. Open browser and visit:
   http://127.0.0.1:8080

---

## 🖥 Output
The browser displays:

Hello World from Google App Engine - Assignment 1

---

## 📄 File Explanation

main.py  
Contains Flask web server logic and route configuration.

app.yaml  
Defines runtime environment and entrypoint configuration for Google App Engine.

requirements.txt  
Lists required Python libraries needed for the application.

---

## 🎓 Viva Questions & Answers

Q1. What is Google App Engine?  
Google App Engine is a Platform as a Service (PaaS) that allows developers to deploy scalable web applications without managing infrastructure.

Q2. What is PaaS?  
Platform as a Service provides a managed runtime environment for application development and deployment without handling servers.

Q3. What is the purpose of app.yaml?  
It defines runtime configuration and deployment settings for App Engine.

Q4. Why use a virtual environment?  
To isolate project dependencies and avoid conflicts with globally installed Python packages.

---

## ✅ Conclusion
Successfully developed and tested a Python-based web application using Google App Engine architecture and Flask framework. The project is version-controlled using Git and hosted on GitHub.
