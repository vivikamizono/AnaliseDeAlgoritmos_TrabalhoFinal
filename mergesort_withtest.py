import random
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    metade = len(arr) // 2
    esquerda = merge_sort(arr[:metade])
    direita = merge_sort(arr[metade:])

    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    return resultado

def generate_list(tipo, tamanho):
    if tipo == 'aleatoria':
        return [random.randint(0, 10000) for _ in range(tamanho)]
    elif tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho, 0, -1))
    else:
        raise ValueError("Tipo desconhecido")

def medir_memoria(func, *args):
    mem_usage = memory_usage((func, args), max_usage=True)
    return mem_usage

def testar_merge_sort(tipo, tamanhos):
    tempos, memorias = [], []

    for tamanho in tamanhos:
        print(f"Testando Merge Sort com {tamanho} elementos...")

        arr = generate_list(tipo, tamanho)

        start_time = time.time()
        mem = medir_memoria(merge_sort, arr)
        duracao = time.time() - start_time

        tempos.append(duracao)
        memorias.append(mem)

    return tempos, memorias

def plotar_resultados(tamanhos, tempos, memorias, tipo):
    plt.figure(figsize=(14, 6))

    # Tempo
    plt.subplot(1, 2, 1)
    plt.plot(tamanhos, tempos, label="Tempo", marker='o', color='teal')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (segundos)")
    plt.title(f"Merge Sort - Tempo de Execução ({tipo})")
    plt.grid(True)

    # Memória
    plt.subplot(1, 2, 2)
    plt.plot(tamanhos, memorias, label="Memória", marker='o', color='darkred')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Uso de Memória (MiB)")
    plt.title(f"Merge Sort - Uso de Memória ({tipo})")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    tipo = 'aleatoria'  # pode mudar para 'ordenada' ou 'inversa'
    tamanhos = [100, 300, 500, 700, 1000, 1500, 2000]

    tempos, memorias = testar_merge_sort(tipo, tamanhos)

    plotar_resultados(tamanhos, tempos, memorias, tipo)

if __name__ == "__main__":
    main()
