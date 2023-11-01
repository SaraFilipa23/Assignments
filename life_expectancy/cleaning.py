import argparse
import pandas as pd
import numpy as np

def clean_data(country):
    """
    Clean and process life expectancy data for a specific country.

    Args:
        country (str): The country code for the specific country.

    This function reads raw data, cleans and reshapes it, and saves the cleaned data to a CSV file.
    """
    data = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')

    data[['unit', 'sex', 'age', 'region']] = data['unit,sex,age,geo\\time'].str.split(
        ',', expand=True)

    data.drop(columns=data.columns[0], inplace=True)

    melted_df = pd.melt(data, id_vars=['unit', 'sex', 'age', 'region'], var_name='year',
                        value_name='value')

    melted_df['value'] = melted_df['value'].str.replace(r'[^0-9.]', '', regex=True)

    melted_df['value'] = melted_df['value'].replace('', np.nan)

    melted_df['year'] = melted_df['year'].astype(int)

    melted_df['value'] = melted_df['value'].astype(float)

    portugal_data = melted_df[melted_df['region'] == country]

    portugal_data = portugal_data.dropna(subset=['value'])

    portugal_data.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

def main():
    """
    Main function to run the data cleaning process.

    This function parses command-line arguments and calls the clean_data function.
    """
    parser = argparse.ArgumentParser(description='Life expectancy data for a specific country.')
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()

    clean_data(args.country)

if __name__ == '__main__':  # pragma: no cover
    main()

