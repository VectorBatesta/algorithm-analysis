import numpy as np # type: ignore
import time
import sys

sys.setrecursionlimit(99999999)

def printadorArquivasso(texto):
    with open("out_at2.txt", "a") as arq:
        arq.write(texto)
        print(texto, end='')

def mergesorto(vetor, inicio, fim):
    if inicio < fim:
        meio = int(np.floor((inicio + fim) / 2))
        mergesorto(vetor, inicio, meio)
        mergesorto(vetor, meio + 1, fim)
        mergium(vetor, inicio, meio, fim)
    return

def mergium(vetor, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio

    vetoraux1 = [0 for _ in range(n1)]
    vetoraux2 = [0 for _ in range(n2)]
    
    for i in range(n1):
        vetoraux1[i] = vetor[inicio + i]
    
    for j in range(n2):
        vetoraux2[j] = vetor[meio + 1 + j]

    i = j = 0
    k = inicio

    while i < n1 and j < n2:
        if vetoraux1[i] <= vetoraux2[j]:
            vetor[k] = vetoraux1[i]
            i += 1
        else:
            vetor[k] = vetoraux2[j]
            j += 1
        k += 1

    while i < n1:
        vetor[k] = vetoraux1[i]
        i += 1
        k += 1
    while j < n2:
        vetor[k] = vetoraux2[j]
        j += 1
        k += 1
        
    return




if __name__ == '__main__':
    tempoinicialprograma = time.time()

    for escolhatam in range(6):
        printadorArquivasso("\n\n")
        match escolhatam:
            case 0:
                tam = 50000
            case 1:
                tam = 100000
            case 2:
                tam = 150000
            case 3:
                tam = 200000
            case 4:
                tam = 250000
            case 5:
                tam = 300000
        
        #if processador.qualidade = ruim:
        tam = int(tam / 10)
        #comentar /\ caso pc for bom

        printadorArquivasso(f'\n[[[[[[[[[[[[[[[ {tam} mil elementos ]]]]]]]]]]]]]]]')

        #alocacao de ram
        vetor = [0 for _ in range(tam)]

        for escolhateste in range(3):
            match escolhateste:
                case 0: #Melhor caso: vetor já ordenado em ordem crescente;
                    printadorArquivasso(f'\nMelhor caso: ')
                    vetor = [i for i in range(tam)]
                case 1: #Caso médio: vetor aleatório;
                    printadorArquivasso(f'\nCaso médio: ')
                    vetor = np.random.randint(0, tam, tam)
                case 2: #Pior caso: vetor já ordenado em ordem decrescente;
                    printadorArquivasso(f'\nPior caso: ')
                    vetor = [i for i in reversed(range(tam))]
            
            temposGastos = [0 for _ in range(10)]
            #
            for iteracao in range(10):
                inicio = 0
                fim = tam - 1
                vetor_temp = vetor.copy()

                #####
                begin = time.time()
                mergesorto(vetor_temp, inicio, fim)
                end = time.time()
                #####

                temposGastos[iteracao] = end - begin
                printadorArquivasso(f'\n iteração {iteracao} terminada, gasto: {temposGastos[iteracao]:.5f} segundos;')
            #
            printadorArquivasso(f'\n  gastou-se {sum(temposGastos):.5f} segundos no total;')
            printadorArquivasso(f'\n  gastou-se {np.mean(temposGastos):.5f} segundos em média;')



    #desnecessario
    tempofinalprograma = time.time()
    tempoUtilizadoprograma = tempofinalprograma - tempoinicialprograma
    printadorArquivasso(f'\n####################################################\nTempo gasto total do programa: {tempoUtilizadoprograma:.4f}.\n####################################################\n')
    #
    