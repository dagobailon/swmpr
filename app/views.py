# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

@app.route('/')
def index():
	day_post = Post("Hello World", "Dago", "Today is a rainy day not to much to do traffic sucks!")
	some_post = Post("Today was a good day", "Dagolyn", "Despite the rain life is great")
	night_post = Post("Time for Bed", "DagoB", "After all that is done let me now rest!" )
	return render_template('index.html', posts = [some_post, day_post, night_post])


