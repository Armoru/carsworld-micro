import os
import requests
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)

if os.getenv('FLASK_ENV', 'development') == 'development':
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.ProductionConfig")

manager = Manager(app)

DRF_HOST = app.config['DRF_HOST']
DRF_PORT = app.config['DRF_PORT']

ROOT_DRF = f"http://{DRF_HOST}:{DRF_PORT}"


@app.route('/')
def index():
    news_list = requests.get(f'{ROOT_DRF}/api/v2/news/')
    news_list = news_list.json()
    news_list = sorted(news_list, key=lambda k: k['created_at'], reverse=True)
    print(news_list)

    categories = requests.get(f'{ROOT_DRF}/api/v2/categories/')
    categories = categories.json()
    print(categories)

    return render_template('index.html', news_list=news_list, categories=categories)


@app.route('/categories/<id_category>')
def categories(id_category):
    news_list = requests.get(f'{ROOT_DRF}/api/v2/news/')
    news_list = news_list.json()

    cat = requests.get(f'{ROOT_DRF}/api/v2/categories/')
    cat = cat.json()

    by_category = []
    for i in news_list:
        if i['category'] == int(id_category):
            by_category.append(i)

    return render_template('index.html', news_list=by_category, categories=cat)
