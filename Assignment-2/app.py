from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/user')
def user():
    return "User logged in"
@app.route('/login', methods = ["POST","GET"])
def login():
    if request.method == "POST":
        Name = request.form.get("name")
        Email = request.form.get("email")
        Phone = request.form.get("phone")
        return "Your name is " + Name + " Your mail id is " + Email + " And Your mobile no is " + Phone + " Your resume is uploaded successfully"
    return render_template('index.html')
if __name__ =='__main__':
	app.run(debug = True)