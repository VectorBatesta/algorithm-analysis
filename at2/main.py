import numpy as np # type: ignore
import time

def printadorArquivasso(texto):
    with open("out_at2.txt", "a") as arq:
        arq.write(texto)

def ordena(vetor, tam, escolhateste):
    for iteracao in range(10):
        vetor_temp = vetor.copy()

        begin = time.time()
        ####
        
        ####
        end = time.time()
        temposGastos[iteracao] = end - begin
        printadorArquivasso(f'\n iteração {iteracao} terminada, gasto: {temposGastos[iteracao]:.5f} segundos;')
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
            [funcoes aqui]
            #
            printadorArquivasso(f'\n  gastou-se {sum(temposGastos):.5f} segundos no total;')
            printadorArquivasso(f'\n  gastou-se {np.mean(temposGastos):.5f} segundos em média;')



    #desnecessario
    tempofinalprograma = time.time()
    tempoUtilizadoprograma = tempofinalprograma - tempoinicialprograma
    printadorArquivasso(f'\n####################################################\nTempo gasto total do programa: {tempoUtilizadoprograma:.4f}.\n####################################################')
    #
    