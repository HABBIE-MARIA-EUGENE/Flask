from flask import Flask

app = Flask(__name__)       # Telling flask to make a new Flask app

@app.route("/")             # Telling Flask which URL should trigger the function below
def home():
    return "This is the HOME"     # Sends back HTML or text to users browser

@app.route("/hall")
def hall():
    return "This is the HALL"

@app.route("/bedroom")
def bedroom():
    return "This is the BEDROOM"

@app.route("/kitchen")
def kitchen():
    return "This is the KITCHEN"

if __name__ == "__main__":             # This block runs only if this file is run directly  not imported
    app.run(debug=True)                # app.run()  starts the Flask server and debug=True enables debug mode