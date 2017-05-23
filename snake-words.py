import csv
import requests
from bs4 import BeautifulSoup

r = requests.get('http://lipsum.lipsum.com/feed/html')
#q = requests.get('http://colin.red')

data = r.text

soup = BeautifulSoup(data, "html.parser")


#for link in soup.find_all('a'):
#  print(link.get('href'))

def main():
  print(soup.prettify())
  print(soup.find_all('a'))
  #print(q.text)
main()
