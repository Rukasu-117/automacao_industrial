# Inicializador do sistema de automação industrial, apresentando um menu para o usuário interagir com as funcionalidades do sistema,
# como cadastrar peças, listar peças, remover peças, listar caixas, gerar relatórios e iniciar simulações.

from menu import (
    cadastrar_peca,
    listar_pecas,
    remover_peca,
    listar_caixas
)
from relatorio import gerar_relatorio
from simulador import iniciar_simulacao

def menu():
    while True:
        print("\n=== SISTEMA INDUSTRIAL ===")
        print("1 - Cadastrar peça")
        print("2 - Listar peças")
        print("3 - Remover peça")
        print("4 - Listar caixas")
        print("5 - Relatório")
        print("6 - Modo automático")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            iniciar_simulacao()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()
