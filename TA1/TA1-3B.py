n = 5
i = 1

while i <= n:

    j = 1
    while j <= (n - i):
        print(' ', end='')
        j += 1

    k = 1
    while k <= (2 * i - 1):
        print(i, end='')
        k += 1

    print()
    i += 1