from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/welcome", methods=["POST"])
def welcome():
    user_name = request.form["username"]
    return render_template("welcome.html",name=user_name)

if __name__ == "__main__":
    app.run(debug = True)