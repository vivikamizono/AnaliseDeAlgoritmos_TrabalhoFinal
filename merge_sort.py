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


def main():
    arr = [int(x) for x in input("Insira os elementos separados por espaço: ").split()]
    print("Array original:", arr)
    arr = merge_sort(arr)
    print("Array ordenado:", arr)


if __name__ == "__main__":
    main()
