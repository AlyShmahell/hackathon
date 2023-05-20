def fibd(n, m):
    alive = [1, 1]
    for i in range(2, n):
        alive += [alive[i - 1] + alive[i - 2]]
        if i == m:
            alive[-1] = alive[-1] - 1
        if i > m:
            alive[-1] = alive[-1] - alive[i - m - 2]
    return alive[-1]

if __name__ == '__main__':
    with open('fibd.txt', 'r') as f:
        n, m = f.readline().split(" ")
        n, m = int(n), int(m)
        print(fibd(n, m))