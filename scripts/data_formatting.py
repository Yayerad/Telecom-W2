#### 3. Data Formatting Script
import pandas as pd

def format_data(df):
    """
    Formats columns for better usability (e.g., renaming, converting units).
    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        pd.DataFrame: Formatted dataframe
    """
    # Rename columns for clarity
    df = df.rename(columns={
        'bearer id': 'Bearer ID',
        'Dur. (ms)': 'Duration (ms)',
        'Start': 'Start Time',
        'End': 'End Time',
        'Avg RTT DL (ms)': 'Avg RTT Downlink (ms)',
        'Avg RTT UL (ms)': 'Avg RTT Uplink (ms)',
        'Total DL (Bytes)': 'Total Download (Bytes)',
        'Total UL (Bytes)': 'Total Upload (Bytes)'
    })

    # Convert duration from ms to seconds
    df['Duration (s)'] = df['Duration (ms)'] / 1000

    return df