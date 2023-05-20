import numpy as np

class RevC:
    def __init__(self):
        self.complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    def __call__(self, string):
        dna = np.array(list(string))
        return "".join(np.vectorize(self.complement.get)(dna)[::-1].tolist())
    
if __name__ == '__main__':
    revc = RevC()
    with open('revc.txt', 'r') as f:
        print(revc(f.read()))