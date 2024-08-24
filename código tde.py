# NOME: Leticia Maria Maia de Andrade Vieira
# TURMA: B
 
# U = UNIAO
# I = INTERSEÇÃO
# D = DIFERENÇA
# C = CARTESIANO

#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados. O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#4
#U
#3, 5, 67, 7
#1, 2, 3, 4
#I
#1, 2, 3, 4, 5
#4, 5
#D
#1, A, C, 34
#A, C, D, 23
#C
#3, 4, 5, 5, A, B, R
#1, B, C, D, 1
#Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
#{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U). A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:
#União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4} 
#Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.

###############################################################################################################################################################

def aprender_operacoes(file_path): #vai entender oq ta no arquivo
    try:
        with open(file_path, 'r') as file:
            linhas = file.readlines()

        quantidade_operacoes = int(linhas[0].strip())  # saber quantas operacoes
        
        resultado = []
        index_linha = 1

        def processar_operacao(tipo, conjunto1, conjunto2): #oq cada operaçao significa e como resolver
            if tipo == 'U':  # uniao
                return conjunto1.union(conjunto2)
    
            elif tipo == 'I':  # interseção
                return conjunto1.intersection(conjunto2)
    
            elif tipo == 'D':  # diferença
                return conjunto1.difference(conjunto2)
    
            elif tipo == 'C':  #cartesiano
                return C(conjunto1, conjunto2)
    
        def C(conjunto1, conjunto2):
            resultado = []  # pares dos conjuntos
            for i in conjunto1:
                for j in conjunto2:
                    par = (i, j)
                    resultado.append(par)
            return resultado

        def ler_conjunto(linha): #vai ler linha por linha
            return set(map(str.strip, linha.strip().split(',')))

        for _ in range(quantidade_operacoes): #evitar algum loop
            operacao = linhas[index_linha].strip()
            conjunto1 = ler_conjunto(linhas[index_linha + 1])
            conjunto2 = ler_conjunto(linhas[index_linha + 2])
            index_linha += 3

            resultado_operacao = processar_operacao(operacao, conjunto1, conjunto2)

            if operacao == 'U': #'legenda' 
                nome_operacao = "União"
            elif operacao == 'I':
                nome_operacao = "Interseção"
            elif operacao == 'D':
                nome_operacao = "Diferença"
            elif operacao == 'C':
                nome_operacao = "Produto Cartesiano"

            print(f'{nome_operacao}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado_operacao}') #imprime o resultado
    
    except FileNotFoundError: #evitar q o código quebre caso de problema no txt
        print(f"Arquivo {file_path} não encontrado.")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

aprender_operacoes('TDE 01\conjuntos.txt') #chama a funcao e o codigo roda
