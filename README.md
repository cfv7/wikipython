# Wikipython

## Summary:
A python tool that scrapes any Wikipedia page and outputs most commonly used words in a wordcloud.

![sample output](https://github.com/cfv7/wikipython/blob/master/examples/sample.png)


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
* make an optional toggle to output an <ol> of top words
* toggle between wikipedias in different languagues (es.wiki or simple.wiki)

## Getting Started
```
cd into your folder
pip install -r requirements
<!--you can search any desired article by entering the title of your article (wikipedia.org/wiki/Lionel_Messi) immediately after the file name-->
python3 wikipython.py Lionel_Messi
```