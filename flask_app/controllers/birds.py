from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bird import Bird
from flask_app.models.user import User
from flask_app.models.rating import Rating


@app.route('/bird/add', methods=["POST"])
def create_bird():
    is_valid_bird = Bird.validate_bird(request.form)
    if not is_valid_bird:
        return redirect('/birds/new')

    data = {
        'species': request.form['species'],
        'description': request.form['description'],
        'user_id': session['user_id'],
        'image_url': Bird.get_bird_image(request.form['description'])
    }
    
    Bird.save(data)
    return redirect("/dashboard")

@app.route('/rating/add', methods=["POST"] )
def create_rating():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'value': request.form['rating_value'],
        'bird_id': request.form['bird_id'],
        'user_id': session['user_id']
    }
    Rating.save(data)
    return('/birds/single/<bird_id>')


@app.route('/birds/single/<int:bird_id>')
def one(bird_id):
    data ={
        "id":bird_id
    }
    bird=Bird.get_one(data)
    return render_template("oneBird.html", bird=bird)

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

@app.route("/birds/delete/<int:bird_id>")
def delete_one(bird_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": bird_id
    }
    bird = Bird.get_one(data)
    if bird.user_id == session["user_id"]:
        Bird.delete_one(data)
    return redirect("/")
