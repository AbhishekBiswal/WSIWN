import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory

import requests

from wsiwn import app

# app controllers
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
	genreone = str(request.args.get("genreone"));
	genretwo = str(request.args.get("genretwo"));
	firstgenre = str(request.args.get("firstgenre"));
	secondgenre = str(request.args.get("secondgenre"));
	geturl = 'https://api.themoviedb.org/3/discover/movie?api_key=745b7b9f524c578b4ac8d055cdcd441d&sort_by=popularity.desc&with_genres='+genreone+','+genretwo
	movies = requests.get(geturl).json()
	#return str(movies['results'])
	movie = []
	i = 0
	while i < 5:
		mov_id = movies['results'][i]['id']
		mov_id = str(mov_id)
		url = 'https://api.themoviedb.org/3/movie/'+mov_id+'?api_key=745b7b9f524c578b4ac8d055cdcd441d'
		test = requests.get(url).json()
		movie.append(test)
		i = i + 1
	return render_template("list.html", movies=movies, movie=movie, firstgenre=firstgenre, secondgenre=secondgenre);

@app.route('/about')
def about():
	return render_template('about.html')

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# error handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
