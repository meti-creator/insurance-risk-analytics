# src/data_quality.py
import pandas as pd

def summarize_data(df):
    """Returns descriptive statistics and data types."""
    summary = df.describe().transpose()
    dtypes = df.dtypes
    return summary, dtypes

def check_missing_values(df):
    """Returns the count and percentage of missing values."""
    missing = df.isnull().sum()
    percentage = (missing / len(df)) * 100
    return pd.DataFrame({'Missing_Count': missing, 'Missing_Percentage': percentage})

def handle_missing_values(df, strategy='median'):
    """Handles missing values based on a specified strategy."""
    if strategy == 'median':
        for col in df.select_dtypes(include=['number']).columns:
            df[col] = df[col].fillna(df[col].median())
    elif strategy == 'drop':
        df = df.dropna()
    return df