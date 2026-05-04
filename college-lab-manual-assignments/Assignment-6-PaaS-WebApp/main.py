from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Assignment 6 - PaaS Web Application</h1>
    <p>This application is running locally and can be deployed to Google App Engine.</p>
    """

@app.route("/about")
def about():
    return "This web app demonstrates Platform as a Service (PaaS)."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
