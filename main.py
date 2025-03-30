# importando as bibliotecas
import numpy as np 
import sys

# função que cria uma matriz a partir de um arquivo txt. 
def criaMatriz(instancia):
    caminho = rf'C:\Users\gugut\Desktop\Aulas\GRAFOS\prototipo\instancias\{instancia}.txt' # aqui deve estar o caminho do arquivo a ser interpretado como uma matriz
    try: 
        with open(caminho, 'rb') as f:
            mat = np.loadtxt(f)
        return mat
    except FileNotFoundError: # caso haja algum erro na hora de encontrar o arquivo
        print(f"Erro: Arquivo {caminho} não encontrado.")
        sys.exit(1)

# função que retorna as dimensões da matriz
def resultado(instancia, matriz):
    return f"{instancia} {matriz.shape[0]} {matriz.shape[1]}"

# função que recebe o resultado das dimensões da matriz e armazena em um arquivo de texto chamado resultado.txt
def salvaResultado(r):
    with open(rf'C:\Users\gugut\Desktop\Aulas\GRAFOS\prototipo\resultado.txt', 'w') as arq:
        arq.write(r + "\n")

if __name__ == "__main__": # testa se o parâmatro foi informado na execução do programa
    if len(sys.argv) < 2:
        print("Erro: Nenhuma instância informada. Uso: python main.py <nome_da_instancia>")
        sys.exit(1)

# chamando as funções
    instancia = sys.argv[1]
    matriz = criaMatriz(instancia)
    res = resultado(instancia, matriz)
    print(res)  # Mostra o resultado na tela, como pedido no enunciado
    salvaResultado(res)
