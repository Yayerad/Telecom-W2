def transform_data(df):
    """
    Applies transformations like aggregations and feature engineering.
    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        pd.DataFrame: Transformed dataframe
    """
    # Add a new column for session duration in minutes
    df['Duration (min)'] = df['Duration (ms)'] / (1000 * 60)

    # Create a new column for total retransmission volume
    df['Total Retrans. Vol (Bytes)'] = df['TCP DL Retrans. Vol (Bytes)'] + df['TCP UL Retrans. Vol (Bytes)']

    # Calculate ratio of downlink to uplink data
    df['DL/UL Ratio'] = df['Total Download (Bytes)'] / (df['Total Upload (Bytes)'] + 1)  # Avoid division by zero

    return df

# Example Usage
# df = pd.read_csv("data.csv")
# transformed_df = transform_data(df)