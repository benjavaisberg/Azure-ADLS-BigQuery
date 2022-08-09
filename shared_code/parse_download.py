import pandas as pd
from io import StringIO

def bytes_to_df(bytes):
    s = str(bytes,'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data, index_col=False)
    return df