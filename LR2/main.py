def first_function(x):
    index_first = -1
    index_last = -1
    length = 0
    max_len = 0
    end_index_first = -1
    end_index_last = -1
    target = False

    for i in range(len(x)):
        if x[i] == 0:
            if not target:
                target = True
                length = 1
                index_first = i
            else:
                length += 1
        else:
            target = False
            index_last = i
            if max_len < length:
                max_len = length
                end_index_first = index_first
                end_index_last = index_last

    print('\nДовжина серії:',max_len, '\nІндекс першого елементу серії:' ,end_index_first, '\nІндекс останього елементу серії:' ,end_index_last)


def second_function(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    return x


third_function = lambda x, y, z: 3*x * y ** 2 - 9 * z


def factorial_function(x):
    if x == 0:
        return 1
    else:
        return x * factorial_function(x-1)


x_arr = [0, 0, 1, 2, 45, 0, 24, 354, 43523, 12, 0, 0, 0, 0, 24, 253, 35, 0]

print('\nМасив x:', x_arr)

first_function(x_arr)

sort_function(x_arr)

print("\nВідсортованний масив:",x_arr)

print("\nВиконання анонімної функції:",third_function(2,3,4))

print("\nРекурсія факторіалу:",factorial_function(5))

