from app import app, helpers, models
from flask import render_template, request, redirect, url_for

simulacoes_lista = []

@app.route('/', methods=['POST', 'GET'])
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
        saldo_total = helpers.calcula_saldo_total(rentabilidade_bruta_valor, valor_aplicado)
        return render_template('index.html', 
                            simulacoes_lista=simulacoes_lista,
                            valor_aplicado=valor_aplicado,
                            dias=dias,
                            rentabilidade_paga=rentabilidade_valor, 
                            cdi=cdi_pago,
                            cdi_considerando_sobras=cdi_com_sobras,
                            valor_sobras=valor_sobras,
                            rentabilidade_bruta_valor=rentabilidade_bruta_valor,
                            saldo_total=saldo_total,
                            rentabilidade_bruta_porcentagem_aa=rentabilidade_bruta_porcentagem_aa) 
    return render_template('index.html', simulacoes_lista=simulacoes_lista) 

@app.route('/salvar_simulacao', methods=['POST', ])
def salvar_simulacao():
    descricao = request.form['descricao']
    valor_aplicado = request.form['valor_aplicado']
    cdi = request.form['cdi']
    cdi_sobras = request.form['cdi_considerando_sobras']
    dias = request.form['dias']
    rentabilidade_bruta = request.form['rentabilidade_bruta_valor']
    saldo_total = request.form['saldo_total']

    simulacao = models.Simulacao(descricao=descricao, valor_aplicado=valor_aplicado, cdi=cdi, cdi_sobras=cdi_sobras, dias=dias, rentabilidade_bruta=rentabilidade_bruta, saldo_total=saldo_total)

    simulacoes_lista.append(simulacao)

    return redirect(url_for('index'))

@app.route('/deletar_simulacao')
def deletar_simulacao():
    return None