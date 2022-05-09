from load import load_articles
from search.index import Index

from flask import Flask, request, jsonify

app = Flask(__name__)

def index_article(articles, index):
    for article in articles:
        index.index_article(article)
    return index

index = index_article(load_articles(),  Index())
print(f'Index contains {len(index.articles)} articles')

@app.route("/query", methods=["POST"] )
def query():
    query = request.json['query']

    print(f'Index contains {len(index.articles)} articles')
    results = index.search(query, rank=True)
    return jsonify({ "articles": results })
