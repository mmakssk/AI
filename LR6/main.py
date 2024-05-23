import numpy as np

target = True

while target:
    N = input("Введіть значення N:\t")
    if N.isdigit():
        N = int(N)
        target = False
    else:
        print("Введено невірний формат даних.\n")

target = True

while target:
    M = input("Введіть значення M:\t")
    if M.isdigit():
        M = int(M)
        target = False
    else:
        print("Введено невірний формат даних.\n")

target = True

while target:
    K = input("Введіть значення K:\t")
    if K.isdigit() and int(K) != N:
        K = int(K)
        target = False
    else:
        print("Введено невірний формат даних або значення співпадає зі значенням N.\n")

X = np.random.randint(-5, 5, (N, M))
Y = np.random.randint(-5, 5, (M, K))
Z = np.dot(X,Y)

print("Матриця Х:\n", X, end="\n\n")
print("Матриця Y:\n", Y, end="\n\n")
print("Матриця Z=X*Y:\n", Z, end="\n\n")

dg_null = Z.diagonal()
dg = dg_null[dg_null != 0]
pr = np.prod(dg)

print("Діагональ без нульових елементів:\t", dg, end="\n\n")
print("Добуток ненульових елементів на головній діагоналі прямокутної матриці:\t", pr)
