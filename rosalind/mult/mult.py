import numpy as np

import numpy as np

def needleman_wunsch(x, y, match=1, mismatch=-1, gap=-1):
    n = x.size
    m = y.size
    score = np.zeros((n, m))
    score[:, 0] = range(n)
    score[0, :] = range(m)
    score[:, 0] *= gap
    score[0, :] *= gap
    for i in range(1, n):
        for j in range(1, m):
            score[i,j] = max(
                int(x[i]==y[j]) + score[i-1,j-1],
                gap        + score[i-1,j],
                gap        + score[i,j-1]
            )
    arrow = np.argwhere(score==score.max())[-1]
    road = []
    ds   = np.array(
        [
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    )
    while any(z>1 for z in arrow) :
        road += [
            [
                x[arrow[0]],
                y[arrow[1]]
            ]
        ]
        arrow = arrow - ds[np.argmax(
            [
                score[arrow - d]
                for d in ds
            ]
        )]
            
                
    




if __name__ == '__main__':
    seqs = [
    "GCATGCG",
    "GATTACA"
    ]
    seqs = [
        np.array([' '] + list(seq))
        for seq in seqs
    ]
    needleman_wunsch(seqs[0], seqs[1])