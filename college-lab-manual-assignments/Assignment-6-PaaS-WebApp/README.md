# Assignment 6  
## Title: Web Application in a PaaS Environment  

---

## 🎯 Objective

To design and deploy a web application in a Platform as a Service (PaaS) environment and understand the deployment lifecycle in cloud computing.

---

## ☁️ Introduction to PaaS

Platform as a Service (PaaS) is a cloud computing model where the cloud provider delivers:

- Runtime environment  
- Operating system  
- Web server  
- Scaling mechanism  
- Load balancing  
- Deployment tools  

The developer only writes application code. Infrastructure management is fully handled by the cloud provider.

Example Used:  
Google App Engine (PaaS service by Google Cloud)

---

## 🔍 Difference Between IaaS and PaaS

| Feature | IaaS | PaaS |
|----------|------|------|
| VM Management | User | Cloud Provider |
| OS Installation | User | Cloud Provider |
| Scaling | Manual | Automatic |
| Focus | Infrastructure | Application Code |
| Example | OpenStack | Google App Engine |

---

## 🏗 Architecture of PaaS Deployment

Deployment Flow:

Developer → gcloud CLI → Cloud Build → Containerization → App Engine Runtime → Load Balancer → Public URL

Behind the scenes:

1. gcloud packages application.
2. Cloud Build creates container image.
3. Dependencies are installed.
4. Gunicorn starts application.
5. Load balancer routes traffic.
6. Auto-scaling is enabled.

---

## 📂 Project Structure

Assignment-6-PaaS-WebApp/
- main.py
- requirements.txt
- app.yaml
- README.md
- .gitignore

---

## 🛠 Step 1: Create Flask Application (main.py)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Assignment 6 - PaaS Web Application</h1>
    <p>This application demonstrates deployment in a PaaS environment.</p>
    """

@app.route("/about")
def about():
    return "This web app is built using Flask and deployed using Google App Engine."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```

---

## 📦 Step 2: Create requirements.txt

```
Flask
gunicorn
```

---

## ⚙ Step 3: Create app.yaml

```
runtime: python39

entrypoint: gunicorn -b :$PORT main:app

instance_class: F1

automatic_scaling:
  min_instances: 1
  max_instances: 2
```

---

## 🖥 Step 4: Run Application Locally (Development Mode)

```
python main.py
```

Open browser:

```
http://localhost:8080
```

Test routes:

```
http://localhost:8080/
http://localhost:8080/about
```

---

## 🧪 Step 5: Simulate Production Deployment Locally

Activate virtual environment:

```
venv\Scripts\activate
```

Run production server:

```
gunicorn -b 127.0.0.1:8080 main:app
```

This simulates how App Engine runs the application in production.

---

## 🚀 Step 6: Deployment to Google App Engine

Initialize project:

```
gcloud init
```

Deploy application:

```
gcloud app deploy
```

Open deployed app:

```
gcloud app browse
```

App Engine automatically:

- Builds container
- Installs dependencies
- Starts Gunicorn
- Assigns public URL
- Enables HTTPS
- Configures load balancing
- Enables auto-scaling

---

## 🔁 Auto Scaling Behavior

If traffic increases:

- New instances are created (horizontal scaling).
- Load balancer distributes traffic.
- When traffic decreases, extra instances are terminated.

If max_instances limit is reached:
- Requests queue
- Latency increases

---

## 🔐 Why Gunicorn?

Flask development server:
- Not production ready
- Single-threaded
- Debug only

Gunicorn:
- Production-grade WSGI server
- Multi-worker support
- Used by App Engine

---

## 🧠 Key Concepts Learned

- Platform as a Service (PaaS)
- Application containerization
- Production vs Development server
- Auto-scaling (Horizontal scaling)
- Managed load balancing
- Cloud runtime abstraction

---

## 📊 Request Handling Flow

User → Global Load Balancer → App Engine Service → Gunicorn → Flask → Response

---

## 🎓 Viva Preparation

What is PaaS?
A cloud model where the provider manages infrastructure and runtime, and the user deploys application code.

What is app.yaml?
Configuration file defining runtime, scaling, and startup command.

What is entrypoint?
Command used to start the application.

What is $PORT?
Environment variable provided by App Engine where application must bind.

What happens if traffic increases?
App Engine automatically scales horizontally by creating additional instances.

---

## 🏁 Conclusion

The web application was successfully developed, tested locally, and prepared for deployment in a PaaS environment using Google App Engine. This assignment demonstrates how PaaS abstracts infrastructure management and enables developers to focus entirely on application logic.

Assignment 6 completed successfully.
