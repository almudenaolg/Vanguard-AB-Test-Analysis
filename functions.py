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


def convert_steps_to_number(df, column):
    step_mapping = {
        'start': 0,
        'step_1': 1,
        'step_2': 2,
        'step_3': 3,
        'confirm': 4}

    # Aply mapping to the values in the column
    df[column] = df[column].map(step_mapping)
    
    return df


def calculate_centrality(df,column):
    mean =df[column].mean().round(2)
    median = df[column].median()
    mode = df[column].mode()[0]
    return{
        'Mean': mean,
        'Median': median,
        'Mode': mode
    }

def calculate_dispersion(df, column):
    variance = round(df[column].var(), 2)
    std_dev = round(df[column].std(), 2)
    min_value = df[column].min()
    max_value = df[column].max()
    range_value = max_value - min_value
    quantiles = df[column].quantile([0.25, 0.5, 0.75]).to_dict()  
    
    return {
        'Variance': variance,
        'Standard Deviation': std_dev,
        'Min': min_value,
        'Max': max_value,
        'Range': range_value,
        'Quantiles': quantiles
    }
def calculate_skewness_kurtosis(df, column):
    skewness = round(df[column].skew(), 2)
    kurtosis = round(df[column].kurtosis(), 2)
    
    return {'Skewness': skewness,
        'Kurtosis': kurtosis}

def plot_histogram(df, column, bins=30):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(12, 8))
    sns.histplot(df[column], kde=True, bins=bins, color="salmon")  # Histograma con KDE
    plt.title(f'Histogram of {column}')  
    plt.xlabel(column)  
    plt.ylabel('Frequency') 
    plt.tight_layout()  
    plt.show() 


def plot_boxplot(df, column):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(8, 10))  
    sns.boxplot(data=df[column], color="lightblue") 
    plt.title(f'Box Plot of {column}') 
    plt.xlabel(column) 
    plt.tight_layout()
    plt.show()


def plot_barplot(df, column):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(10, 8))
    sns.countplot(x=column, data=df, palette="pastel")  
    plt.title(f'Bar Plot of {column}')
    plt.xlabel(column) 
    plt.ylabel('Count') 
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.show()


def chi_results(crosstab):
    # Chi-square test for significance
    from scipy.stats import chi2_contingency
    chi2, p, dof, ex = chi2_contingency(crosstab)
    print(f"Chi2: {chi2}, p-value: {p}")

def cramer_result(crosstab):
    from scipy.stats.contingency import association
    # Computing the association between variables in 'crosstab_result' using the "cramer" method
    return association(crosstab, method="cramer")

