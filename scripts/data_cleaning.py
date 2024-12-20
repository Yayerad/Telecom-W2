#### 1. Data Cleaning Script
import pandas as pd

def clean_data(df):
    """
    Cleans the input dataframe by handling missing values and removing duplicates.
    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Drop duplicate rows
    df = df.drop_duplicates()

    # Fill missing numeric values with 0
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Fill missing string values with 'Unknown'
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].fillna('Unknown')

    # Remove rows with invalid timestamps
    df = df[df['Start'] < df['End']]

    return df

# Example Usage
# df = pd.read_csv("data.csv")
# df = clean_data(df)