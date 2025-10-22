## Refactored Code (With Principles)

import pandas as pd
from typing import List

# Load CSV
def load_dataset(url: str) -> pd.DataFrame:
    """Load a CSV dataset from a given URL."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading dataset: {e}")

#Calculate the mean of a column
def column_mean(df: pd.DataFrame, column: str) -> float:
    """Return the mean of a column."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")
    return df[column].mean()

#Calculate the maximum of a column
def column_max(df: pd.DataFrame, column: str) -> float:
    """Return the maximum value of a column."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")
    return df[column].max()

#Filter funct to filter the data as per given species
def filter(df: pd.DataFrame, species: str) -> pd.DataFrame:
    """Filter the dataset for a given species."""
    if 'species' not in df.columns:
        raise ValueError("Dataset does not contain 'species' column.")
    return df[df['species'] == species]

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    iris_df = load_dataset(url)
    
    print("Average sepal length:", column_mean(iris_df, 'sepal_length'))
    print("Max petal width:", column_max(iris_df, 'petal_width'))
    print("Setosa sample:", filter(iris_df, 'setosa').head())
