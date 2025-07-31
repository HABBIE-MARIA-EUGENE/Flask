from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form["name"]
    email = request.form["email"]
    age = request.form["age"]

    return render_template("welcome.html",name=name, email=email, age=age)

if __name__ == "__main__":
    app.run(debug = True)