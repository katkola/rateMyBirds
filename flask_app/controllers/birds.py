from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bird import Bird
from flask_app.models.user import User


@app.route('/bird/add', methods=["POST"])
def create_bird():
    is_valid_bird = Bird.validate_bird(request.form)
    if not is_valid_bird:
        return redirect('/birds/new')

    data = {
        'species': request.form['species'],
        'description': request.form['description'],
        'user_id': session['user_id']
    }
    
    Bird.save(data)
    return redirect("/dashboard")

@app.route('/birds/view')
def one_bird():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('oneBird.html')

@app.route('/birds/new')
def bird_form():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    return render_template('newBirdForm.html', user=user)


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)

    return render_template("dashboard.html", birds=Bird.get_all())
