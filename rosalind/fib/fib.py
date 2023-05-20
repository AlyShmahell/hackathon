def fib(i, c):
    if i == 1:
        return 1
    elif i == 2:
        return c
    p = fib(i - 1, c);
    g = fib(i - 2, c);
    if i <= 4:
        return g + p
    return p + (g * c)

if __name__ == '__main__':
    with open('fib.txt', 'r') as f:
        n, k = f.readline().split(" ")
        k, n = int(k), int(n)
        print(fib(n, k))
        