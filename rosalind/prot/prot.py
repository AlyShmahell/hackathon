import pandas as pd
from io import StringIO
tbl = """
codon,protein,codon,protein,codon,protein,codon,protein 
UUU,F,CUU,L,AUU,I,GUU,V
UUC,F,CUC,L,AUC,I,GUC,V
UUA,L,CUA,L,AUA,I,GUA,V
UUG,L,CUG,L,AUG,M,GUG,V
UCU,S,CCU,P,ACU,T,GCU,A
UCC,S,CCC,P,ACC,T,GCC,A
UCA,S,CCA,P,ACA,T,GCA,A
UCG,S,CCG,P,ACG,T,GCG,A
UAU,Y,CAU,H,AAU,N,GAU,D
UAC,Y,CAC,H,AAC,N,GAC,D
UAA,Stop,CAA,Q,AAA,K,GAA,E
UAG,Stop,CAG,Q,AAG,K,GAG,E
UGU,C,CGU,R,AGU,S,GGU,G
UGC,C,CGC,R,AGC,S,GGC,G
UGA,Stop,CGA,R,AGA,R,GGA,G
UGG,W,CGG,R,AGG,R,GGG,G 
"""
if __name__ == '__main__':
    with open('prot.txt', 'r') as f:
        inp = f.read()
    df = pd.read_csv(StringIO(tbl), sep=",")
    proteins = df.filter(like='protein').to_numpy().T.flatten().tolist()
    codons = df.filter(like='codon').to_numpy().T.flatten().tolist()
    print(proteins)
    print(codons)
    z = 