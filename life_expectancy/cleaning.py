import argparse
import pandas as pd
import numpy as np

def load_data():
    data = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', sep='\t')
    return data

def clean_data(data):
    data[['unit', 'sex', 'age', 'region']] = data[r'unit,sex,age,geo\time'].str.split(
        ',', expand=True)

    data.drop(columns=data.columns[0], inplace=True)

    cleaned_data = pd.melt(data, id_vars=['unit', 'sex', 'age', 'region'], var_name='year',
                        value_name='value')

    cleaned_data['value'] = cleaned_data['value'].str.replace(r'[^0-9.]', '', regex=True)

    cleaned_data['value'] = cleaned_data['value'].replace('', np.nan)

    cleaned_data['year'] = cleaned_data['year'].astype(int)

    cleaned_data['value'] = cleaned_data['value'].astype(float)

    return cleaned_data

def save_data(cleaned_data, country):
    portugal_data = cleaned_data[cleaned_data['region'] == country]

    portugal_data = portugal_data.dropna(subset=['value'])

    portugal_data.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

def main():
    parser = argparse.ArgumentParser(description='Life expectancy data for a specific country.')
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()

    data = load_data()
    cleaned_data = clean_data(data)
    save_data(cleaned_data, args.country)

if __name__ == '__main__':  # pragma: no cover
    main()