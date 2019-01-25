import pandas as pd

DOC_PH = '../data/documenten_ph/DB_V2.TXT'

if __name__ == '__main__':
    doc_ph = pd.read_csv(DOC_PH, encoding='latin_1', sep='\t')
    print(doc_ph.head(5))
