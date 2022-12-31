import pandas as pd 

def read_file():
    df = pd.read_csv("customerorders-201008-180523.csv", names=['id', 'post_code', 'price'])
    return df

def count_rows(df):
    total_rows = len(df)
    return total_rows
    

if __name__ == "__main__":
    file_res = read_file()  
    rows = count_rows(file_res)
    print(rows)