from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.player import Player
from models.team import Team
from models.contract import Contract

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = []
    # if request.method == "POST":
    #     try:
    #         url = request.form['url']
    #         r = requests.get(url)
    #         print(r.text)
    #     except:
    #         errors.append(
    #             "Unable to get URL. Please make sure it's valid and try again."
    #         )
    if request.method == "GET":
        for instance in db.session.query(Team).order_by(Team.id):
            results.append(instance.name)
        return render_template('index.html', errors=errors, results=results)

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()