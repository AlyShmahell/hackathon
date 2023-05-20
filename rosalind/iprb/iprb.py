from scipy.special import  comb

if __name__ == '__main__':
    with open('iprb.txt', 'r') as f:
        dom, het, rec = f.read().split(" ")
        dom, het, rec = int(dom), int(het), int(rec)
        pop = 4 * comb(dom + het + rec, 2)
        dom = 4 * comb(dom, 2) + 4 * dom * het + 4 * dom * rec + 3 * comb(het, 2) + 2 * het * rec
        print(dom/pop)