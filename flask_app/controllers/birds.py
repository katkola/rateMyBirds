from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bird import bird

@app.route('/')
def home ():
    return render_template ('index.html')

@app.route('/profile')
def userprofile():
    return render_template ('profile.html')