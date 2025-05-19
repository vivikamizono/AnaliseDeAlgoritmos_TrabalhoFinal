import random
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

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

def testar_insertion_sort(tipo, tamanhos):
    tempos, memorias = [], []

    for tamanho in tamanhos:
        print(f"Testando Insertion Sort com {tamanho} elementos...")

        arr = generate_list(tipo, tamanho)

        start_time = time.time()
        mem = medir_memoria(insertion_sort, arr)
        duracao = time.time() - start_time

        tempos.append(duracao)
        memorias.append(mem)

    return tempos, memorias

def plotar_resultados(tamanhos, tempos, memorias, tipo):
    plt.figure(figsize=(14, 6))

    # Tempo
    plt.subplot(1, 2, 1)
    plt.plot(tamanhos, tempos, label="Tempo", marker='o', color='blue')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (segundos)")
    plt.title(f"Insertion Sort - Tempo de Execução ({tipo})")
    plt.grid(True)

    # Memória
    plt.subplot(1, 2, 2)
    plt.plot(tamanhos, memorias, label="Memória", marker='o', color='green')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Uso de Memória (MiB)")
    plt.title(f"Insertion Sort - Uso de Memória ({tipo})")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    tipo = 'aleatoria'  # pode trocar por 'ordenada' ou 'inversa'
    tamanhos = [100, 300, 500, 700, 1000]  # ajuste conforme necessário

    tempos, memorias = testar_insertion_sort(tipo, tamanhos)

    plotar_resultados(tamanhos, tempos, memorias, tipo)

if __name__ == "__main__":
    main()
