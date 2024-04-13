from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return 'teste'

@app.route('/calcular')
def calcular():
    return None

@app.route('/salvar_simulacao')
def salvar_simulacao():
    return None

@app.route('/deletar_simulacao')
def deletar_simulacao():
    return None