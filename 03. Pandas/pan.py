import pandas as pd

AUTHORS_DATASET = "/home/vadim/DataScience/03. Pandas/auth.csv"
BOOK_DATASET = "/home/vadim/DataScience/03. Pandas/book.csv"
IN_DATASET = "https://video.ittensive.com/python-advanced/internet-2017.csv"

dfa = pd.read_csv(IN_DATASET, na_values="NA", decimal=",")
dfu = pd.read_csv(AUTHORS_DATASET, skiprows=1)
dfb = pd.read_csv(BOOK_DATASET, skiprows=1)

print(dfu)
print(dfa)

data_indexed = pd.Series(dfu["author_name"].values, index=dfu["author_id"].values)
print(data_indexed)