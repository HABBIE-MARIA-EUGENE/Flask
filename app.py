from flask import Flask

app = Flask(__name__)       # Telling flask to make a new Flask app

@app.route("/")
def home():
    return "This is the HOME"

@app.route("/hall")
def hall():
    return "This is the HALL"

@app.route("/bedroom")
def bedroom():
    return "This is the BEDROOM"

@app.route("/kitchen")
def kitchen():
    return "This is the KITCHEN"

if __name__ == "__main__":
    app.run(debug=True)  