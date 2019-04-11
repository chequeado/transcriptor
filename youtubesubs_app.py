# -*- coding: utf-8 -*-
import flask
from flask import Flask, jsonify, request
from flask import abort
from flask import make_response
from flask import render_template
from flask_cors import cross_origin

import download_video

# GLOBALS
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route("/")
def index():
    return render_template('index.html')
   
@app.route("/get_subs")
@cross_origin()
def get_subs():
    # Obtener el primero de los subtitlos
    response = download_video.get_subtitles(request.args['url'])[0]
    subtitles = response['text_with_stamps']
    # Pequeña modificación al título para mejor legibilidad
    title = response['title'].replace("_"," ")
    # Genero el json de respuesta
    return jsonify({'subtitles':subtitles,'title':title})


if __name__ == '__main__':
    app.run()
    #app.run(host="127.0.0.1",port=8585)

