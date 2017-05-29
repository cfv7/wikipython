from flask import Flask, request
from os import environ
from collections import Counter
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image
import io
import base64
import re
import requests
import numpy as np


app = Flask(__name__)
snake_mask = np.array(Image.open("snake.png")) 
stopwords = {"Retrieved", "html", "it", "the", "of", "a", "an", "for", "to", "in", "is", "through", "at", "which", "not", "was", "as", "by", "on", "may", "when", "and", "or", "with", "have", "he", "his", "him", "http", "www", "com", "update", "last", "org", "htm", "https", "they", "are", "from", "also", "that", "then", "many", "this", "January", "February", "March", "April", "May", "June", "July", "August","September", "October","November", "December"}

@app.route("/")
def create():
  print(request.args)
  article = request.args.get("article")
  if article:
    r = requests.get('https://en.wikipedia.org/w/index.php?title=%s&action=render'%article)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    wc = WordCloud(background_color='white', max_words=1000, mask=snake_mask, stopwords=stopwords).generate(soup.text)
    img = wc.to_image()
    # give a file-like string of bytes for a given input 
    png = io.BytesIO()
    img.save(png, "PNG")
    png = png.getvalue()
    # gives us an in-memory version of our conent
    # characters are rendering one set of bytes with a new set of bytes
    # b64 -> +, /, l, U, 1 ~ convert b64 png into text via ascii
    png = base64.b64encode(png).decode("ascii")
    html = """<img src="data:image/png;base64,%s" alt="word cloud">""" % png
  else:
    html = ""    
  return """
  <style type="text/css">
  .header{
    width: 100%;
    height: 10%;
    background-color: lightgreen;
    padding-left: 20px;
    padding-top: 12px;
  }

  .main-container{
    margin-right: 10%;
  }
  </style> 
  <div class="header">
  <h1>Wikipython</h1>
  </div>
  <p>this tool will generate a word cloud for any wikipedia article</p>
  <p>if searching for a name use case-sensitive: First_Last</p>
  <form>Wiki article<input name=article><input type=submit></form>
  """ + html

# last line of file
if __name__ == "__main__":
  app.run()


  