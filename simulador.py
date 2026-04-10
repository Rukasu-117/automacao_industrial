# Simulador de produção de peças

import random
import time

from validador import validar_peca
from caixa import adicionar_na_caixa
from dados import pecas, aprovadas, reprovadas, caixas
import dados

modo_automatico = False


def gerar_peca():
    return {
        "id": dados.id,
        "peso": round(random.uniform(95, 110), 2),
        "cor": random.choice(["azul", "verde"]),  # vermelho gera erro
        "comprimento": round(random.uniform(10, 22), 2)
    }



def iniciar_simulacao():
    global modo_automatico
    modo_automatico = True

    print("\n🚀 Modo automático ATIVADO (Ctrl + C para parar)\n")

    try:
        while modo_automatico:
            peca = gerar_peca()
            
            dados.id += 1  # Incrementa o ID para a próxima peça

            pecas.append(peca)  # 👈 ADICIONE ESTA LINHA

            valido, mensagem = validar_peca(

                peca["peso"],
                peca["cor"],
                peca["comprimento"]
            )

            if valido:
                aprovadas.append(peca)
                fechou = adicionar_na_caixa(peca)

                print(f"✅ OK → {peca}")

                if fechou:
                    print("📦 Caixa fechada automaticamente!")

            else:
                reprovadas.append({
                    "peca": peca,
                    "motivo": mensagem
                })
                print(f"❌ ERRO → {peca} ({mensagem})")

            time.sleep(1)  # simula tempo de produção

    except KeyboardInterrupt:
        modo_automatico = False
        print("\n⛔ Modo automático DESATIVADO\n")