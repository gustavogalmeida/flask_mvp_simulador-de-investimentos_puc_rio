from app import app, helpers
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST', ])
def calcular():
    valor = request.form['valor']
    dias = request.form['dias']
    cdi_pago = request.form['cdi']
    cdi_com_sobras = helpers.calcula_cdi_considerando_sobras(cdi_pago)
    rentabilidade_valor = helpers.calcula_rentabilidade_periodo_valor(dias, valor, cdi_pago)
    valor_sobras = helpers.calcula_valor_sobras(valor)
    return render_template('index.html', 
                           rentabilidade_paga=rentabilidade_valor, 
                           cdi_considerando_sobras=cdi_com_sobras,
                           valor_sobras=valor_sobras)

@app.route('/salvar_simulacao')
def salvar_simulacao():
    return None

@app.route('/deletar_simulacao')
def deletar_simulacao():
    return None