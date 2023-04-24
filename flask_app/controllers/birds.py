from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
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


@app.route('/rating/add', methods=["POST"] )
def create_rating():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'value': request.form['rating_value'],
        'bird_id': request.form['bird_id'],
        'user_id': session['user_id']
    }
    birdId = data['bird_id']
    Rating.save(data)
    return redirect(url_for('one', bird_id=birdId))


@app.route('/birds/single/<int:bird_id>')
def one(bird_id):
    data ={
        "id":bird_id
    }
    bird=Bird.get_one(data)
    ratings = Rating.get_ratings_for_bird(data)
    avg_rating = Rating.get_average_rating(data)
    return render_template("oneBird.html", bird=bird, avg_rating=avg_rating, ratings=ratings)


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


@app.route('/edit/<int:bird_id>')
def edit(bird_id):
    print(bird_id)
    data ={ 

        "id": bird_id,
        "species": 'species',
        "description": 'description'
    }
    Jane=Bird.get_one(data)
    print(Jane)
    return render_template("edit.html",bird=Bird.get_one(data))


@app.route("/bird/update/<int:bird_id>", methods=["POST"])
def Update_bird(bird_id):
    data = {
          "id": bird_id,
        "species": request.form['species'],
        "description": request.form['description']
    }
    bird=Bird.update(data)
    return redirect("/dashboard")


    return render_template("dashboard.html", birds=Bird.get_all())

