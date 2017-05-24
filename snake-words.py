import sys
import re
import requests
from collections import Counter
from bs4 import BeautifulSoup

def wordCount(text):
  count = 0
  for character in text:
    if character == ' ' or character == '\t' or character == '\n':
      count = count + 1
  return count

article = 'Lionel_Messi'
if len(sys.argv) > 1: article = sys.argv[1]
#stopWords = "the in a of to and his hers him he she her for as on"
#def analyze(r):
r = requests.get('https://en.wikipedia.org/w/index.php?title=%s&action=render'%article)
data = r.text
soup = BeautifulSoup(data, "html.parser")
regExSoup = re.findall(r'[A-Za-z]{4,}', soup.text)
                       

def main():
  print('analyze ->', Counter(regExSoup).most_common(10))
  print('wordCount ->', wordCount(data))
  #print(soup.text)
  #print(soup.find_all('a'))
main(