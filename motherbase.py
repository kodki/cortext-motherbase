from flask import Flask
from flask import request
import readabillity
from bs4 import BeautifulSoup
from api_keys import API_CONFIG
import flask

import cortext.text
import cortext.visualizer

app = Flask(__name__)


@app.route('/visualize_words/')
def visualize_words():
    url = request.args.get('url', '')
    data = readabillity.load(url)
    raw = BeautifulSoup(data['content']).get_text()
    text = cortext.text.Text(raw).parse()
    v = cortext.visualizer.Visualizer(text, API_CONFIG)
    words = [[to_data(obj) for obj in s] for s in v.visualize_words()]
    return flask.jsonify(**{'words': words, 'content': data['content'], 'title': data['title']})


def to_data(obj):
    out = {'word_type': type(obj).__name__}
    out.update(obj.__dict__)
    return out

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
