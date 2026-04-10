# Função para adicionar peças na caixa, verificando se a caixa atingiu a capacidade máxima.
# Se sim, a caixa é adicionada à lista de caixas e o contador de caixa é incrementado.

from dados import caixa_atual, caixas
import dados

CAPACIDADE_CAIXA = 10

def adicionar_na_caixa(peca):

    # Cadastra o numero da caixa no produto.
    peca["caixa"] = dados.contador_caixa

    # Adiciona o produto na caixa atual.
    caixa_atual.append(peca)

    if len(caixa_atual) == CAPACIDADE_CAIXA:
        caixas.append(caixa_atual.copy())
        caixa_atual.clear()

        # Adicionar o contador de caixa.
        dados.contador_caixa += 1  

        return True

    return False