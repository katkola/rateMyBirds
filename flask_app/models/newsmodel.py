import requests
from flask_app.config.news_config import api_key
newsapi = NewsApiClient(api_key='0b45717f6a55487f8f0078b47e62751d')

class News:
    def __init__(self,data):
    self.title= title
    self.description = description
    self.linke = linke

    @staticmethod
    def get_bird_headlines():
        top_headlines = newsapi.get_top_headlines(q='birds',
        sources='bbc-news,national-geographic',
        category='nature,environment,climate',
        language='en',country='us')
        console.log(top_headlines)

        articles = []

        for article in top_headlines['articles']:
            data= {
                'title': article['title'],
                'description': article['description'],
                'linke': article['url']
            }
            articles.append(cls(data))
        return articles



    @staticmethod
    def get_bird_news():
        url = "https://newsapi.org/v2/top-headlines?q=birds"
        parameters = {
            "query": description,
            "client_id": api_key
        }
        response = requests.get(url, params=parameters)
        print(response.json())
        for article in results.artiles:

        return json.loads(response.content)['urls']['raw']