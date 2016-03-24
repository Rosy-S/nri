from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, jsonify
from model import *

app = Flask(__name__)
app.secret_key = "someFancySecret"

app.jinja_env.undefined = StrictUndefined

app.route('/')
def index():
	return render_template("index.html")


if __name__ == "__main__":

	app.debug = True

	connect_to_db(app)

	app.run()