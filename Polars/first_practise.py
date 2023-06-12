import polars as pl

df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

print(df)


def filter_rows(df):
    """
    Input: Dataframe
    Action: Filter the DataFrame to include only rows where the value in column "A" is greater than 2.
    Output: Filtered rows
    """
    filtered_rows = df.filter(pl.col("A") > 2)
    return filtered_rows

filtered_rows = filter_rows(df)

print(filtered_rows)