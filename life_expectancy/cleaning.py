import argparse
import pandas as pd
import numpy as np

def load_data():
    """
    Load raw life expectancy data from a file.

    Returns:
        pd.DataFrame: The loaded raw data.
    """
    return pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')

def clean_data(data,country):
    """
    Clean and process life expectancy data.

    Args:
        data (pd.DataFrame): The raw data.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    data[['unit', 'sex', 'age', 'region']] = data['unit,sex,age,geo\\time'].str.split(
            ',', expand=True)
    data.drop(columns=data.columns[0], inplace=True)

    melted_df = pd.melt(data, id_vars=['unit', 'sex', 'age', 'region'], 
var_name='year', value_name='value')
    melted_df['value'] = melted_df['value'].str.replace(r'[^0-9.]', '', regex=True)
    melted_df['value'] = melted_df['value'].replace('', np.nan)
    melted_df['year'] = melted_df['year'].astype(int)
    melted_df['value'] = melted_df['value'].astype(float)
    melted_df = melted_df[melted_df['region'] == country]
    melted_df = melted_df.dropna(subset=['value'])

    return melted_df

def save_data(melted_df, filename='life_expectancy/data/pt_life_expectancy.csv'):
    """
    Save cleaned life expectancy data to a file.

    Args:
        data (pd.DataFrame): The cleaned data.
        filename (str): The filename to save the data to.
    """
    melted_df.to_csv(filename, index=False)

def main():
    """
    Main function to run the data cleaning process.

    This function loads, cleans, and saves the data.
    """
    parser = argparse.ArgumentParser(description='Life expectancy data for a specific country.')
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()

    raw_data = load_data()
    cleaned_data = clean_data(raw_data,args.country)
    save_data(cleaned_data)

if __name__ == '__main__':  # pragma: no cover
    main()


## vou por isto aqui para poder fazer commit e a Ines rever o meu codigo ##