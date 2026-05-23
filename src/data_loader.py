# src/data_loader.py
import pandas as pd
import os

def load_insurance_data(filepath):
    """Loads and performs initial type enforcement on insurance data."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at {filepath}")
    
    df = pd.read_csv(filepath)
    
    # 1. Date conversion
    if 'TransactionDate' in df.columns:
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
        
    # 2. Type enforcement (ensure categorical vs numerical)
    # List categorical columns to enforce
    cat_cols = ['Gender', 'Province', 'VehicleType', 'CoverType', 'AutoMake', 'AutoModel']
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')
            
    # 3. Boolean enforcement
    if 'Claimed' in df.columns:
        df['Claimed'] = df['Claimed'].astype(bool)
        
    return df