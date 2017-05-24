import sys
import re
import requests
from collections import Counter
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordCount(text):
  count = 0
  for character in text:
    if character == ' ' or character == '\t' or character == '\n':
      count = count + 1
  return count

article = 'Lionel_Messi'
if len(sys.argv) > 1: article = sys.argv[1]
r = requests.get('https://simple.wikipedia.org/w/index.php?title=%s&action=render'%article)
data = r.text
soup = BeautifulSoup(data, "html.parser")
# makes a simple word cloud 
wordcloud = WordCloud().generate(soup.text)
# manual regex with traditional list output 
regExSoup = re.findall(r'[A-Za-z]{4,}', soup.text)
# cloud logic
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(soup.text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()  


def main():
  print('analyze ->', Counter(regExSoup).most_common(10))
  print('wordCount ->', wordCount(data))
  #print(soup.text)
  #print(soup.find_all('a'))
main()