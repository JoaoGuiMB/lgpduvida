# LGPDúvida

LGPDúvida is a chatbot that answers user's doubt about the brazilian's General Data Protection Regulation [LGPD](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm).

This project is a search engine that compares the users's doubt with the text of each article and classify them according with their content.

# How it works?

Firstly, each article of the official brazilian General Data Protection Regulation pass through a process of analysis that removes punctuation and accents, stop words (most common portuguese words), convertion to lowercase and applying stemming to every word (ensuring that different forms of a word map to the same stem, like brewery and breweries).

Then the query text (user's doubt) will pass through the same process and be compared with the articles and ranked by the term frequency.

To improve the scoring algorithm, it's necessary to compute the inverse articles frequency for a term by dividing the number of articles (N) in the index by the amount of articles that contain the term, and take a logarithm of that, then simply multiple the term frequency with the inverse article frequency during our ranking, so matches on terms that are rare in the article text will contribute more to the relevancy score.

The chatbot itself was developed using the low code platform [Blip](https://www.take.net/blip/)

# Usage

1. Clone the respository

```
 git clone https://github.com/JoaoGuiMB/lgpduvida.git
```

2. Install dependencies

```
pip3 freeze > requirements.txt
```

3. Run application

```
gunicorn main:app
```

4.Query

```
curl --request POST \
  --url http://localhost:8000/query \
  --header 'Content-Type: application/json' \
  --data '{
	"query": "Quais são os princípios dessa lei?"
}'
```

Or access the [chatbot](https://joao-martins-zfqmt.chat.blip.ai/?appKey=bGdwZHV2aWRhOjY4MTMwN2YyLTI2ZDctNDhhOC04YmNhLTk0NTMyZjcyMzgwZA==)

# Credits

This applications was strongly influeced by the tutorial made by [Bart de Goede](https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/)
