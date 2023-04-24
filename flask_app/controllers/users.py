from flask import render_template, session,redirect, request,flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.bird import Bird
from flask_app.models.user import User

bcrypt=Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect("/")

    data = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"],
        "password":  bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.save(data)

    session['user_id'] = id
    session['firstname']= request.form['firstname']
    return redirect('/dashboard')

    
@app.route("/login",methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")

    session['user_id'] = user.id
    return redirect('/dashboard')



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/profile/<userId>")
def profile(userId):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": userId
    }
    user = User.get_one(data)

    return render_template("profile.html", user=user, birds=Bird.get_birds_by_user(data))