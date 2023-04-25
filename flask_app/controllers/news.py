from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for

from flask_app import News

@app.route('/news')
def news():
    news = []
    news = News.get_bird_headlines()

    return render_template('news.html', news=news)