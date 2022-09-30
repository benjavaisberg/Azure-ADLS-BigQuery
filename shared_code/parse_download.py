import pandas as pd
from io import StringIO

def bytes_to_df(bytes):
    s = str(bytes,'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data, index_col=False)
    # Replace spaces, special characters in column names with _ as BigQuery doesn't allow spaces in column names
    df.columns = df.columns.str.replace(' ', '')
    # df.columns = df.columns.str.replace('.', '')
    return df