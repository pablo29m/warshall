def warshall(matriz):
    n = len(matriz)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = matriz[i][j] or (matriz[i][k] and matriz[k][j])
    return matriz

def main():

# Aplicaremos el algoritmo a la siguient matriz de adyacencia
    matriz= [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
    ]
    print("Matriz de adyacencia:\n")
    for fila in matriz:
        print(fila)

    matrizwarshall = warshall(matriz)
    print("\nMatriz luego del algoritmo de Warshall:\n")
    for fila in matrizwarshall:
        print(fila)

main()