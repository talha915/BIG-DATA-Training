import polars as pl

df = pl.DataFrame(
    {
        "A": [1, 2, 3, 4, 5],
        "fruits": ["banana", "banana", "apple", "apple", "banana"],
        "B": [5, 4, 3, 2, 1],
        "cars": ["beetle", "audi", "beetle", "beetle", "beetle"],
    }
)

df2 = pl.DataFrame(
    {
        "A": [1, 2, 3],
        "fruits": ["banana", "apple", "mango"]
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


def aggregate_rows(df, grouped_col, action_col):
    """
    Input: Dataframe, grouped_col, action_col
    Action: Group the DataFrame by the "fruits" column and calculate the average value of column "B" for each fruit.
    Output: Aggregated rows
    """
    grouped_rows = df.groupby(pl.col(grouped_col)).agg(pl.mean(action_col))
    return grouped_rows

aggregrated_rows = aggregate_rows(df, "fruits", "B")
print("Aggregated Rows: ", aggregrated_rows)


def sort_rows(df, column_name, action):
    """
    Input: Dataframe, column_name, "descending True or False: Boolean"
    Action: Sort the DataFrame in descending order based on the values in column "A"
    Output: Aggregated rows
    """
    try:
        sorted_df = df.sort(by=column_name, descending=action)
        return sorted_df
    except Exception as e:
        return e 

sorted_rows = sort_rows(df, "A", True)
print(sorted_rows)       


# Join DataFrames: Create a second DataFrame and join it with the original DataFrame based on a common column.
# Apply a function: Apply a custom function to a column and create a new column with the results.


def joined_rows(df, df2, column_name):
    """
    Input: Dataframe, Dataframe, column name
    Action: Create a second DataFrame and join it with the original DataFrame based on a common column.
    Output: joined rows
    """
    try:
        df_join = df.join(df2, on="A")
        return df_join
    except Exception as e:
        return e 

df_joined = joined_rows(df, df2, "A")
print(df_joined)