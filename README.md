# 🏭 Sistema de Automação Industrial - Inspeção de Peças

## 📌 1. Explicação do funcionamento

Este projeto simula um sistema de automação industrial responsável por substituir a inspeção manual em uma linha de produção.

O sistema realiza as seguintes etapas:

1. Cadastro de peças  
As peças podem ser inseridas manualmente pelo usuário ou geradas automaticamente pelo modo de simulação.

2. Validação de qualidade  
Cada peça é validada com base nas seguintes regras:
- Peso entre 95g e 105g  
- Cor: azul ou verde  
- Comprimento entre 10cm e 20cm  

Caso a peça não atenda aos critérios, ela é reprovada e o motivo é registrado.

3. Separação de peças  
- Peças aprovadas são armazenadas  
- Peças reprovadas são registradas com o motivo da falha  

4. Armazenamento em caixas  
- A cada 10 peças aprovadas, uma caixa é automaticamente fechada  
- O sistema também mostra o progresso da caixa atual  

5. Rastreabilidade  
- Cada peça possui um ID único  
- Peças aprovadas são associadas à caixa em que foram armazenadas  

6. Relatórios  
O sistema gera um relatório contendo:
- Total de peças aprovadas  
- Total de peças reprovadas  
- Quantidade de caixas fechadas  
- Motivos de reprovação  

---

## ▶️ 2. Como rodar o programa

### ✅ Pré-requisitos
- Python 3 instalado (versão 3.8 ou superior recomendada)

### 📥 Passo a passo

1. Baixe ou clone o projeto:
```bash
git clone https://github.com/Rukasu-117/automacao_industrial.git