from flask import Flask ,render_template


app = Flask(__name__)      #constructor value 


@app.route('/')         
@app.route('/home')         #either of these routes will trigger this function
def home():
    return render_template('register.html') #render_template is used to render the HTML file 





if __name__ == '__main__':
    app.run(debug=True) # To reload/ refresh the page automatically
