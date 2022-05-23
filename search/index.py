import math

from .timing import timing
from .analysis import analyze

class Index:
    def __init__(self):
        self.index = {}
        self.articles = {}

    def index_article(self, article):
        if article.articleNumber not in self.articles:
            self.articles[article.articleNumber] = article
            article.analyze()

        for token in analyze(article.fulltext):
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(article.articleNumber)

    def article_frequency(self, token):
        return len(self.index.get(token, set())) if len(self.index.get(token, set())) != 0 else 1

    def inverse_article_frequency(self, token):
        # Manning, Hinrich and Schütze use log10, so we do too, even though it
        # doesn't really matter which log we use anyway
        # https://nlp.stanford.edu/IR-book/html/htmledition/inverse-article-frequency-1.html
        return math.log10(len(self.articles) / self.article_frequency(token))

    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    @timing
    def search(self, query, search_type='AND', rank=False):
        """
        Search; this will return articles that contain words from the query,
        and rank them if requested (sets are fast, but unordered).

        Parameters:
          - query: the query string
          - search_type: ('AND', 'OR') do all query terms have to match, or just one
          - score: (True, False) if True, rank results based on TF-IDF score
        """
        print('Start search')
        if search_type not in ('AND', 'OR'):
            return []

        analyzed_query = analyze(query)
        results = self._results(analyzed_query)
        if search_type == 'AND':
            # all tokens must be in the article
            articles = [self.articles[article_articleNumber] for article_articleNumber in set.intersection(*results)]
        if search_type == 'OR':
            # only one token has to be in the article
            articles = [self.articles[article_articleNumber] for article_articleNumber in set.union(*results)]
        if rank:
            return self.rank(analyzed_query, articles)
        return articles

    def rank(self, analyzed_query, articles):
        results = []       
        if not articles:
         
            return results
        for article in articles:
            score = 0.0
            for token in analyzed_query:
                tf = article.term_frequency(token)
                idf = self.inverse_article_frequency(token)
                score += tf * idf
                article.score = score
                
            results.append(article)
        return sorted(results, key=lambda article: article.score, reverse=False)
