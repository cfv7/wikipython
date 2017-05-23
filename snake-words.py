import requests
from collections import Counter
from bs4 import BeautifulSoup

def wordCount(text):
  count = 0
  for character in text:
    if character == ' ' or character == '/t' or character == '/n':
      count = count + 1
  return count

#def analyze(r):
r = requests.get('https://en.wikipedia.org/wiki/Lionel_Messi')
data = r.text
soup = BeautifulSoup(data, "html.parser")

def main():
  print('analyze ->', Counter(soup.text.split()).most_common)
  print('wordCount ->', wordCount(data))
  #print(soup.text)
  #print(soup.find_all('a'))
main()
