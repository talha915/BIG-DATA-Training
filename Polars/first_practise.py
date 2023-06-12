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


def filter_rows(df, column_name, threshold):
    """
    Input: Dataframe, column_name, threshold
    Action: Filter the DataFrame to include only rows where the value in column "A" is greater than 2.
    Output: Filtered rows
    """
    filtered_rows = df.filter(pl.col(column_name) > threshold)
    return filtered_rows

filtered_rows = filter_rows(df, "A", 2)

print(filtered_rows)

grouped_rows = df.groupby(pl.col("fruits")).agg(pl.mean("B"))
print(grouped_rows)

def aggregate_rows(df, column_name, threshold):
    """
    Input: Dataframe, column_name, threshold
    Action: Group the DataFrame by the "fruits" column and calculate the average value of column "B" for each fruit.
    Output: Filtered rows
    """