selic_meta = 10.75
sobras_sobre_saldo_medio_deposito_ultimo_exercicio = 0.87

cdi_meta_atual = selic_meta - 0.1


def calcula_cdi_considerando_sobras(cdi_pago):
    rentabilidade_aa = float(cdi_meta_atual)*(float(cdi_pago)/100)
    rentabilidade_com_sobras_porcentagem = float(rentabilidade_aa) + float(sobras_sobre_saldo_medio_deposito_ultimo_exercicio)
    cdi_considerando_sobras = float(rentabilidade_com_sobras_porcentagem)/float(cdi_meta_atual)*100
    return cdi_considerando_sobras

def calcula_valor_sobras(valor):
    ## TO DO: Colocar uma forma de ter saldo médio
    valor_sobras = float(valor) * sobras_sobre_saldo_medio_deposito_ultimo_exercicio/100
    return valor_sobras

def calcula_rentabilidade_periodo_valor(dias, valor_aplicado, cdi_pago):
    rentabilidade_aa = float(cdi_pago)/100 * float(cdi_meta_atual)
    rentabilidade_periodo_porcentagem = ((1 + (rentabilidade_aa/100))**(float(dias)/365)-1)
    rentabilidade_periodo_valor = rentabilidade_periodo_porcentagem * float(valor_aplicado)
    return rentabilidade_periodo_valor