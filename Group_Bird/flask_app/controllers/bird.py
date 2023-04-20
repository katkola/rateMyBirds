from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_bcrypt import Bcrypt
from flask_app import app

from flask_app.models.register import User
from flask_app.models.bird import Bird

bcrypt = Bcrypt(app)


# None of the routes are rendering anything here yet -QT

@app.route('/bird/all')
def dashboard():
    return render_template('',users=User.get_all())

@app.route('/bird/add', methods=["POST"])
def create_bird():
    is_valid_bird = Bird.validate_bird(request.form)
    if not is_valid_bird:
        return redirect('/')

    data = {
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'user_id': session['user_id']
    }
    
    Bird.save_bird(data)
    return redirect("/")


@app.route('/bird/single')
def singleBird():
    data = {
        "id": session['user_id']
    }
    return render_template('.html',user=User.get_one(data),trees=Bird.get_mine(data))


# Throwing tis together, I will need to take a look at these, currently
#  do not have access to the python stack for some reason. - QT

# @app.route('/edit/<int:id>')
# def edit(id):
    
#     data ={ 

#         "id":id
#     }
#     return render_template("update.html",user=User.get_one(data),tree=Bird.get_one(data))


# @app.route('/bird/update/<int:id>', methods=['POSt'])
# def update(id):
#     data= {
#         **request.form,
#         "id":id
#     }
#     trees=Bird.update(data)
#     return redirect("/user_trees")


@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    } 
    birds=Bird.get_them(data)
    print(birds)
    return render_template("theirs.html",user=User.get_one(data),birds=birds)

@app.route('/destroy/<int:id>')
def destroy(id):
    # Bird.destroy_plant({'id': id})
    data ={

        'id': id
    }
    Bird.destroy_plant(data)
    return redirect("/")

# @app.route('/')
# def dashboard():
#     return redirect('/')
