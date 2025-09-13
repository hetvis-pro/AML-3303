## Refactored Code (With Principles)

import pandas as pd
from typing import List


# Load CSV
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

def print_average_sepal_length(data: List[int])-> int:
    """Print Avg Sepal Length"""
    avg = data['sepal_length'].mean()
    if avg==None:
      raise ValueError("Invalid data.")
    return avg

def print_max_petal_width(data: List[int])-> int:
    """Print Max Petal Width"""
    mx = data['petal_width'].max()
    if mx==None:
      raise ValueError("Invalid data.")
    return mx

if __name__ == "__main__":
  # Print average sepal length and max petal length
    avg_sepal_length= print_average_sepal_length(df)
    max_petal_length = print_max_petal_width(df)
    print("Average Sepal Length:", avg_sepal_length)
    print("Maximum Petal Length:", max_petal_length)
    # Filter rows where species is setosa
    print(df[df['species'] == 'setosa'].head())    
