def encaixa(A, B):
    if len(B) > len(A):
        return False
    return A[-len(B):] == B

# Lendo o número de casos de teste
N = int(input())

for _ in range(N):
    # Lendo os valores de A e B
    A, B = input().split()

    # Verificando se B corresponde aos últimos dígitos de A
    if encaixa(A, B):
        print("encaixa")
    else:
        print("nao encaixa")