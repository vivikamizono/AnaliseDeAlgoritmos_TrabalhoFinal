import random
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

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

def testar_heapsort(tipo, tamanhos):
    tempos, memorias = [], []

    for tamanho in tamanhos:
        print(f"Testando Heap Sort com {tamanho} elementos...")

        arr = generate_list(tipo, tamanho)

        start_time = time.time()
        mem = medir_memoria(heapsort, arr)
        duracao = time.time() - start_time

        tempos.append(duracao)
        memorias.append(mem)

    return tempos, memorias

def plotar_resultados(tamanhos, tempos, memorias, tipo):
    plt.figure(figsize=(14, 6))

    # Tempo
    plt.subplot(1, 2, 1)
    plt.plot(tamanhos, tempos, label="Tempo", marker='o', color='purple')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (segundos)")
    plt.title(f"Heap Sort - Tempo de Execução ({tipo})")
    plt.grid(True)

    # Memória
    plt.subplot(1, 2, 2)
    plt.plot(tamanhos, memorias, label="Memória", marker='o', color='orange')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Uso de Memória (MiB)")
    plt.title(f"Heap Sort - Uso de Memória ({tipo})")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    tipo = 'aleatoria'  # pode ser 'ordenada' ou 'inversa'
    tamanhos = [100, 300, 500, 700, 1000, 1500, 2000]

    tempos, memorias = testar_heapsort(tipo, tamanhos)

    plotar_resultados(tamanhos, tempos, memorias, tipo)

if __name__ == "__main__":
    main()
