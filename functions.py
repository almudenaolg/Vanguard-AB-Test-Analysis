import pandas as pd

# Function to explore dataframes
def explore(dataframe):
    """
    Explore the dataframe

    Parameters
    ---------- 
    dataframe : pandas.DataFrame
        The dataframe to explore
    """
    print(dataframe.shape)
    print(dataframe.head(10))
    print(dataframe.info())

# Function to remove rows with many null and duplicate values
def remove_nulls_and_duplicates(df, threshold=0.8):
    """
    Remove rows with many null and duplicate values

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to clean
    threshold : float
        The threshold for null values
    """
    # Calcular el número mínimo de valores no nulos
    min_non_nulls = max(2, int(threshold * df.shape[1]))
    
    # Delete rows that do not have the minimum number of non-zero values
    df_cleaned = df.dropna(thresh=min_non_nulls)
    
    # Remove duplicate rows
    df_cleaned.drop_duplicates(inplace=True)
    
    return df_cleaned


def rename_columns_1(df):
    """
    Rename columns in df_demo

    Parameters
    ---------- 
    df : pandas.DataFrame
        The dataframe to clean
    """
    df.rename(columns={
        'clnt_age': 'client_age',
        'clnt_tenure_yr': 'client_tenure_years',
        'clnt_tenure_mnth': 'client_tenure_months',
        'gendr': 'gender',
        'num_accts': 'num_accounts',
        'bal': 'balance',
        'calls_6_mnth': 'calls_last_6_months',
        'logons_6_mnth': 'logons_last_6_months'}, inplace=True)
    return df

def mean_fill_missing_values(df, column):
    df[column] = df[column].fillna(df[column].mean())
    return df

def convert_to_datetime(df, column):
    """
    Convert a column to datetime format.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the column.
    column : str
        The name of the column to convert.
    
    Returns
    -------
    df : pandas.DataFrame
        The dataframe with the column converted to datetime.
    """
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def convert_to_categorical(df, column):
    df[column] = df[column].astype('category')
    return df
