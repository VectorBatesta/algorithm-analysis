import numpy as np # type: ignore
import time

def ordena(vetor, tam, escolhateste):
    match escolhateste:
        case 0:
            print(f'Melhor caso: ')
        case 1:
            print(f'Caso médio: ')
        case 2:
            print(f'Pior caso: ')

    for iteracao in range(10):
        match escolhateste:
            case 0: #Melhor caso: vetor já ordenado em ordem crescente;
                vetor = [i for i in range(tam)]
            case 1: #Caso médio: vetor aleatório;
                vetor = np.random.randint(0, tam, tam)
            case 2: #Pior caso: vetor já ordenado em ordem decrescente;
                vetor = [i for i in reversed(range(tam))]

        begin = time.time()
        ####
        for j in range(2, tam):
            chave = vetor[j]

            i = j - 1
            while i >= 1 and vetor[i] > chave:
                vetor[i+1] = vetor[i]
                i = i - 1
            vetor[i+1] = chave
        ####
        end = time.time()
        temposGastos[iteracao] = end - begin
        print(f' iteração {iteracao} terminada, gasto: {temposGastos[iteracao]:.5f} segundos;')

    print(f'  gastou-se {sum(temposGastos):.5f} segundos no total;')
    print(f'  gastou-se {np.mean(temposGastos):.5f} segundos em média;')
    return


if __name__ == '__main__':
    tempoinicialprograma = time.time()

    for escolhatam in range(5):
        print("\n\n")
        match escolhatam:
            case 0:
                tam = 50000
                print("[[[[[[[[[[[[[[[ 50 mil elementos ]]]]]]]]]]]]]]]")
            case 1:
                tam = 100000
                print("[[[[[[[[[[[[[[[ 100 mil elementos ]]]]]]]]]]]]]]]")
            case 2:
                tam = 150000
                print("[[[[[[[[[[[[[[[ 150 mil elementos ]]]]]]]]]]]]]]]")
            case 3:
                tam = 200000
                print("[[[[[[[[[[[[[[[ 200 mil elementos ]]]]]]]]]]]]]]]")
            case 4:
                tam = 250000
                print("[[[[[[[[[[[[[[[ 250 mil elementos ]]]]]]]]]]]]]]]")
            case 5:
                tam = 300000
                print("[[[[[[[[[[[[[[[ 300 mil elementos ]]]]]]]]]]]]]]]")

        #alocacao de ram
        vetor = [0 for _ in range(tam)]

        for escolhateste in range(3):
            temposGastos = [0 for _ in range(10)]
            ordena(vetor, tam, escolhateste)

    tempofinalprograma = time.time()
    tempoUtilizadoprograma = tempofinalprograma - tempoinicialprograma
    print(f"""\n##########################
          Tempo gasto total do programa: {tempoUtilizadoprograma:.4f}.
          ##########################""")