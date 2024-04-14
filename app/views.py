from app import app, helpers, models
from flask import render_template, request, redirect, url_for

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        valor_aplicado = request.form['valor']
        dias = request.form['dias']
        cdi_pago = request.form['cdi']

        cdi_com_sobras = helpers.calcula_cdi_considerando_sobras(cdi_pago)
        rentabilidade_valor = helpers.calcula_rentabilidade_periodo_valor(dias, valor_aplicado, cdi_pago)
        valor_sobras = helpers.calcula_valor_sobras(valor_aplicado)
        rentabilidade_bruta_valor = helpers.calcula_rentabilidade_bruta_valor(valor_sobras, rentabilidade_valor)
        rentabilidade_bruta_porcentagem_aa = helpers.calcula_rentabilidade_bruta_porcentagem_aa(rentabilidade_bruta_valor, valor_aplicado)
        valor_resgate = helpers.calcula_valor_resgate(rentabilidade_bruta_valor, valor_aplicado)
        return render_template('index.html', 
                            rentabilidade_paga=rentabilidade_valor, 
                            cdi_considerando_sobras=cdi_com_sobras,
                            valor_sobras=valor_sobras,
                            rentabilidade_bruta_valor=rentabilidade_bruta_valor,
                            valor_resgate=valor_resgate,
                            rentabilidade_bruta_porcentagem_aa=rentabilidade_bruta_porcentagem_aa) 
    return render_template('index.html') 

@app.route('/salvar_simulacao', methods=['POST', ])
def salvar_simulacao():
    return None

@app.route('/deletar_simulacao')
def deletar_simulacao():
    return None