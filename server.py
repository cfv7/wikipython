from flask import Flask, request
from os import environ
import io
import base64
import re
import requests
from collections import Counter
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import numpy as np
from PIL import Image


app = Flask(__name__)
snake_mask = np.array(Image.open("snake.png")) 
stopwords = {"Retrieved", "html", "it", "the", "of", "a", "an"}



@app.route("/")
@app.route("/hello")
def say_hi():
  print(request.args)
  article = request.args.get("article")
  if article:
    r = requests.get('https://en.wikipedia.org/w/index.php?title=%s&action=render'%article)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    wc = WordCloud(max_words=2000, mask=snake_mask, stopwords=stopwords).generate(soup.text)
    img = wc.to_image()
    png = io.BytesIO()
    img.save(png, "PNG")
    png = png.getvalue()
    # gives us an in-memory version of our conent
    png = base64.b64encode(png).decode("ascii")
    html = """<img src="data:image/png;base64,%s" alt="word cloud">""" % png
  else:
    html = ""    
  return """
  <h1>Hello World!</h1>
  <form>Wiki article<input name=article><input type=submit></form>
  """ + html


















# last line of file
if __name__ == "__main__":
  app.run()


  