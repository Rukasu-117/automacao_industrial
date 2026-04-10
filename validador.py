# Regra de validação para peças de fabricação

def validar_peca(peso, cor, comprimento):
    if not (95 <= peso <= 105):
        return False, "Peso fora do padrão"

    if cor.lower() not in ["azul", "verde"]:
        return False, "Cor inválida"

    if not (10 <= comprimento <= 20):
        return False, "Comprimento fora do padrão"

    return True, "Peça aprovada"
