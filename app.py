from flask import Flask


app = Flask(__name__)      #constructor value 


@app.route('/')
def home():
    return 'Hello, World! This is my first Flask app.'





if __name__ == '__main__':
    app.run(debug=True) # To reload/ refresh the page automatically
