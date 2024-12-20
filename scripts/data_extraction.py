#### 2. Data Extraction Script
import pandas as pd

def extract_relevant_columns(df):
    """
    Extracts relevant columns from the dataframe.
    Args:
        df (pd.DataFrame): Input dataframe
    Returns:
        pd.DataFrame: Dataframe with selected columns
    """
    relevant_columns = [
        'bearer id', 'Dur. (ms)', 'Start', 'End', 'IMSI', 'MSISDN/Number', 'IMEI',
        'Avg RTT DL (ms)', 'Avg RTT UL (ms)', 'Avg Bearer TP DL (kbps)',
        'Avg Bearer TP UL (kbps)', 'Total DL (Bytes)', 'Total UL (Bytes)',
        'Handset Manufacturer', 'Handset Type'
    ]
    return df[relevant_columns]

# Example Usage
# df = pd.read_csv("data.csv")
# extracted_df = extract_relevant_columns(df)