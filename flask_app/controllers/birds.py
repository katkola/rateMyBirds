from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bird import Bird

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bird/add', methods=["POST"])
def create_bird():
    is_valid_bird = Bird.validate_bird(request.form)
    if not is_valid_bird:
        return redirect('/')

    data = {
        'species': request.form['species'],
        'user_id': session['user_id']
    }
    
    Bird.save_bird(data)
    return redirect("/")

@app.route('/profile')
def profile():
    data = {
        "id": session['user_id']
    }
    return render_template('profile.html',user=User.get_one(data),birds=Bird.get_by_user(data))
