import sys
import re
import requests
from collections import Counter
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from os import path
from PIL import Image


def wordCount(text):
  count = 0
  for character in text:
    if character == ' ' or character == '\t' or character == '\n':
      count = count + 1
  return count

# user can search their own input easily by running 'python3 snake-words.py magic' 
# proper names are typically case-sensitive First_Last
article = 'Python'
if len(sys.argv) > 1: article = sys.argv[1]

# can use either en.wiki or simple.wiki
r = requests.get('https://simple.wikipedia.org/w/index.php?title=%s&action=render'%article)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# stopwords  
stopwords = {"Retrieved", "html", "it", "the", "of", "a", "an", "for", "to", "in", "is", "through", "at", "which", "not", "was", "as", "by", "on", "may", "when", "and", "or", "with", "have", "he", "his", "him", "http", "www", "com", "update", "last", "org", "htm", "https", "they", "are", "from", "also", "that", "then", "many", "this", "January", "February", "March", "April", "May", "June", "July", "August","September", "October","November", "December"}

# # makes a simple word cloud 
# wordcloud = WordCloud(stopwords=stopwords).generate(soup.text)

# # cloud logic
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off") 

# manual regex with traditional list output 
regExSoup = re.findall(r'[A-Za-z]{4,}', soup.text)

# read the mask image
snake_mask = np.array(Image.open("snake.png")) 

# create cloud
wc = WordCloud(background_color="white", max_words=4000, mask=snake_mask, stopwords=stopwords)

# generate word cloud
wc.generate(soup.text)

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

def main():
  print('analyze ->', Counter(regExSoup).most_common(10))
  print('wordCount ->', wordCount(data))
main()