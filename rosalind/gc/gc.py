from collections import defaultdict

def gc(dic):
    res = []
    for k in dic:
        res += [(k, sum([1 for x in dic[k] if x in 'CG'])/len(dic[k])*100)]
    return sorted(res, key=lambda x: x[1])[-1]

if __name__ == '__main__':
    dic = defaultdict(str)
    c   = ''
    with open('gc.txt', 'r') as f:
        for line in f.readlines():
            if '>' in line:
                c = line.strip('>\t\n\r')
                continue
            dic[c] += line.strip()
        print(*gc(dic))