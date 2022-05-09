from crypt import methods
from load import load_articles
from search.index import Index

from flask import Flask, request, jsonify

app = Flask(__name__)

def index_article(articles, index):
    for i, article in enumerate(articles):
        index.index_article(article)
        if i % 5000 == 0:
            print(f'Indexed {i} documents', end='\r')
    return index

index = index_article(load_articles(),  Index())
print(f'Index contains {len(index.articles)} articles')

@app.route("/query", methods=["POST"] )
def query():
    query = request.json['query']
    print(query)

    print(f'Index contains {len(index.articles)} articles')
    results = index.search(query, rank=True)
    print(results)
    if(len(results) == 0):
        return jsonify([])
    return jsonify({ "articles": results })

#print(result)