
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')# used to call html program
@app.route('/user')
def user_login():
    return "User logged in"
@app.route('/login', methods = ["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form.get("Name")
        email = request.form.get("Email")
        ph = request.form.get("Phone")
        return "Your name is " + name + " Your mail id is " + email + " And Your mobile no is " + ph + "And your resume is uploaded successfully"
    return render_template('index.html') 
if __name__ =='__main__':
	app.run(debug = True)

        
