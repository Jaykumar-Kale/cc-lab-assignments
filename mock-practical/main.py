from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    output = ""
    for i in range(5):
        output += "Name: Jaykumar Kale<br>"
        output += "Seat No: 33324<br>"
        output += "Department: IT<br><br>"
    return output

if __name__ == "__main__":
    app.run(port=8080)