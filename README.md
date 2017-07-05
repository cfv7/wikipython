# Wikipython
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()

A python tool that scrapes any Wikipedia page and outputs most commonly used words in a wordcloud.

![ozil gif](https://github.com/cfv7/wikipython/blob/master/examples/wiki_ozil.gif)

## Technology:
1. Framework: Flask
2. Libraries: BeautifulSoup4(BS4), Requests
3. Package: Wordcloud
4. Server: Gunicorn

## Process:
* scrape text from a wiki page
* parse the text into strings
* use the Counter functionality to total up most commonly occuring strings
* use regular expressions via python's re module
* plug those words

## Future:
* eventually I hope to work on a web spider which could scrape every page of a whole website rather than just a wiki page
* learn more about robot exclusion standard
* make an optional toggle to output an ordered list of top words
* toggle between wikipedias in different languagues (es.wiki or simple.wiki)

## Getting Started:
```
cd into your folder
pip install -r requirements
```
generate an image, for example: wikipedia.org/wiki/Lionel_Messi
```
python3 wikipython.py Lionel_Messi
```
or spin up a server 
```
python3 server.py 
```
once you've done this the Flask server can be accessed in your browser at 127.0.0.1:5000

Thanks for checking out my app. 

