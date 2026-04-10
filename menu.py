# Funções para o menu de opções do sistema de controle de qualidade

from dados import pecas, aprovadas, reprovadas, caixas
from validador import validar_peca
from caixa import adicionar_na_caixa
import dados

def cadastrar_peca():
    peso = float(input("Peso (g): "))
    cor = input("Cor (azul/verde): ")
    comprimento = float(input("Comprimento (cm): "))

    peca = {
        "id":dados.id,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    dados.id += 1

    pecas.append(peca)

    valido, mensagem = validar_peca(peso, cor, comprimento)

    if valido:
        aprovadas.append(peca)
        fechou = adicionar_na_caixa(peca)

        print("✅ Aprovada!")

        if fechou:
            print("📦 Caixa fechada automaticamente!")

    else:
        reprovadas.append({
            "peca": peca,
            "motivo": mensagem
        })
        print(f"❌ Reprovada: {mensagem}")


def listar_pecas():
    print("\n--- APROVADAS ---")
    for p in aprovadas:
        print(p)

    print(f"ID: {p['id']} | Caixa: {p.get('caixa', 'N/A')}")

    print("\n--- REPROVADAS ---")
    for r in reprovadas:
        p = r["peca"]
        print(f"ID: {p['id']} | Motivo: {r['motivo']}")
    
def peca_em_caixa_fechada(peca):
    from dados import caixas

    for caixa in caixas:
        if peca in caixa:
            return True
    return False

def remover_peca():
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    # filtra apenas peças removíveis
    pecas_removiveis = [p for p in pecas if not peca_em_caixa_fechada(p)]

    if not pecas_removiveis:
        print("Nenhuma peça disponível para remoção.")
        return

    print("\n--- PEÇAS DISPONÍVEIS PARA REMOÇÃO ---")

    for p in pecas_removiveis:
        print(f"ID: {p['id']} | Peso: {p['peso']} | Cor: {p['cor']}")

    id_remover = int(input("Digite o ID da peça: "))

    removida = None

    for p in pecas_removiveis:
        if p["id"] == id_remover:
            removida = p
            break

    if not removida:
        print("ID inválido ou peça não pode ser removida.")
        return

    # remove da lista principal
    pecas.remove(removida)

    if removida in aprovadas:
        aprovadas.remove(removida)

    if removida in reprovadas:
        reprovadas.remove(removida)

    if removida in caixa_atual:
        caixa_atual.remove(removida)

    print(f"Peça ID {id_remover} removida com sucesso.")



from dados import caixas, caixa_atual

CAPACIDADE_CAIXA = 10

from dados import caixas, caixa_atual
from caixa import CAPACIDADE_CAIXA

def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")

    if not caixas:
        print("Nenhuma caixa fechada ainda.")
    else:
        for i, caixa in enumerate(caixas):
            ids = [p["id"] for p in caixa]
            print(f"Caixa {i+1}: {len(caixa)} peças | IDs: {ids}")

    print("\n--- CAIXA EM ANDAMENTO ---")

    if caixa_atual:
        restante = CAPACIDADE_CAIXA - len(caixa_atual)
        ids = [p["id"] for p in caixa_atual]

        print(f"Peças na caixa atual: {len(caixa_atual)}")
        print(f"IDs na caixa atual: {ids}")
        print(f"Faltam {restante} peça(s) para fechar a caixa")

        # EXTRA 🔥 (progresso)
        percentual = (len(caixa_atual) / CAPACIDADE_CAIXA) * 100
        print(f"Progresso: {percentual:.1f}%")

    else:
        print("Nenhuma caixa em andamento.")
