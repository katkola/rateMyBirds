from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from datetime import datetime, timedelta
from flask_app.config.news_config import api_key
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='0b45717f6a55487f8f0078b47e62751d')
import json
import requests

@app.route('/news')
def news():
    news = []
    month_ago = datetime.now() - timedelta(days=30)
    print(month_ago)
    formated_date = str(month_ago.isoformat())[:10]
    top_headlines = newsapi.get_everything(q='bird', 
    from_param=formated_date,
    page_size=5
    )
    articles = top_headlines['articles']

    return render_template('news.html', articles=articles)

@app.route('/about')
def about_devs():
    return render_template('about.html')