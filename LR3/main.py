print("Завдання 1\nчастина перша\n")
b = "aeiouy"
A = "if two witches were watching two watches, which witch would watch which watch?"
B = "abcdefghijklmnopqrstuvwxyz"

test = "abba free"

def swap_vowels_to_number(a):
    for i in range(len(a)):
        if b.find(a[i]) != -1:
            k = B.find(a[i])+1
            a = a[:i] + "%d" % k + a[i+1:]

    return a

A = swap_vowels_to_number(A)

print("Результат:",A)

print("\nЧастина друга")

X = [[-10, 5, 3, 9, 5],
     [-4, 8, 10, -7, 2],
     [-3, 1, -5, 7, 3],
     [7, 0, -4, -1, 3],
     [-9, 9, 0, 7, -3]]

Y = [[-1, -5, 5, 6, 2],
    [6, -2, -4, 5, 3],
    [3, -4, -6, 3, -10],
    [-3, 7, 9, -10, -2],
    [7, 0, -5, 10, 9]]

Z = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(X[i][j] + Y[i][j])
    Z.append(row)

print("Результат:")
for i in range(5):
    print(Z[i])

