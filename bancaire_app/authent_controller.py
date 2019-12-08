#!/usr/local/bin/python3.7
#-*-coding:Utf-8 -*

from . import app
from . import compte_static_model, gestion_compte
from flask import render_template

@app.route('/')
@app.route('/sign_in.html')
def show_connexion():
    return render_template('sign_in.html')


@app.route('/sign_up.html')
def show_inscription():
    return render_template('sign_up.html')

