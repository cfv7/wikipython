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
article = 'Lionel_Messi'
if len(sys.argv) > 1: article = sys.argv[1]

# can use either en.wiki or simple.wiki
r = requests.get('https://en.wikipedia.org/w/index.php?title=%s&action=render'%article)
data = r.text
soup = BeautifulSoup(data, "html.parser")

# stopwords, isn't currently working
stopwords = {"Retrieved", "html", "it", "the", "of", "a", "an"}

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
wc = WordCloud(max_words=2000, mask=snake_mask, stopwords=stopwords)

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