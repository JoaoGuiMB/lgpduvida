from dataclasses import dataclass
from collections import Counter

from .analysis import analyze

from search.analysis import analyze

@dataclass
class Article:
    articleNumber: int
    text: str

    @property
    def fulltext(self):
        return ' '.join([self.text])

    def analyze(self):
        self.term_frequencies = Counter(analyze(self.text))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)