
if __name__ == '__main__':
    with open('hamm.txt', 'r') as f:
        inp = [line.strip() for line in f.readlines()]
    print(
        sum(x != y for x,y in zip(*inp) )
    )