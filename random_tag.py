from flask import Flask, redirect
import urllib
import codecs
import random

app = Flask(__name__)
tags = []

with codecs.open("bandcamp tags.txt", "r", "utf-8") as f:
    tags = f.readlines()


@app.route('/')
def index():
    tag = randtag()
    print tag
    return redirect("http://bandcamp.com/tag/" + tag)


def randtag():
    return urllib.quote(random.choice(tags).encode('utf-8').strip("\r\n"))

if __name__ == '__main__':
    app.run(port=8000)
