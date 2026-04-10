# Função para gerar o relatório final do sistema de controle de qualidade

from dados import aprovadas, reprovadas, caixas

def gerar_relatorio():
    print("\n===== RELATÓRIO FINAL =====")

    print(f"Total aprovadas: {len(aprovadas)}")
    print(f"Total reprovadas: {len(reprovadas)}")
    print(f"Caixas fechadas: {len(caixas)}")

    # contagem por motivo
    motivos = {}

    for r in reprovadas:
        motivo = r["motivo"]

        if motivo not in motivos:
            motivos[motivo] = 0

        motivos[motivo] += 1

    print("\n--- REPROVAÇÕES POR MOTIVO ---")

    for motivo, qtd in motivos.items():
        print(f"{motivo}: {qtd}")