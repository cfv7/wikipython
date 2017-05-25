from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
  return "<h1>Hello World!</h1>"

if __name__ == "__main__":
  app.run()