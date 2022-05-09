import json
from search.article import Article

def load_articles():
    ARTICLES_PATH = 'articles.json'
    file = open(ARTICLES_PATH)
    articles = json.load(file)  

    for _, article in enumerate(articles):
       yield Article(articleNumber=article['articleNumber'], text=article['text'])