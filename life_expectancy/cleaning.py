import argparse
import pandas as pd
import numpy as np
from enum import Enum



class Region(Enum): 
    PT = 'PT'
    BE = 'BE'
    BG = 'BG'
    AT = 'AT'
    CH = 'CH'
    CY = 'CY'
    CZ = 'CZ'
    DK = 'DK'
    EE = 'EE'
    EL = 'EL'
    ES = 'ES'
    EU = 'EU'
    FI = 'FI'
    FR = 'FR'
    HR = 'HR'
    HU = 'HU'
    IS = 'IS'
    IT = 'IT'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    MT = 'MT'
    NL = 'NL'
    NO = 'NO'
    PL = 'PL'
    RO = 'RO'
    SE = 'SE'
    SI = 'SI'
    SK = 'SK'
    DE = 'DE'
    AL = 'AL'
    EA = 'EA'
    EF = 'EF'
    IE = 'IE'
    ME = 'ME'
    MK = 'MK'
    RS = 'RS'
    AM = 'AM'
    AZ = 'AZ'
    GE = 'GE'
    TR = 'TR'
    UA = 'UA'
    BY = 'BY'
    UK = 'UK'
    XK = 'XK'
    FX = 'FX'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'
    EA18 = 'EA18'
    EA19 = 'EA19'
    EFTA = 'EFTA'
    EEA30_2007 = 'EEA30_2007'
    EEA31 = 'EEA31'
    EU27_2007 = 'EU27_2007'
    EU28 = 'EU28'
    
    @classmethod
    def get_actual_countries(cls):
         """Return a list of all actual countries."""
         exclude_values = ['EU', 'EFTA', 'EA18', 'EA19', 'EEA30_2007', 'EEA31', 'EU27_2007', 'EU28']
         return [region.value for region in cls if region.value not in exclude_values]

def load_data(file_path: str = 'life_expectancy/data/eu_life_expectancy_raw.tsv') -> pd.DataFrame:
    """Load raw life expectancy data from a file."""
    df = pd.read_csv(file_path, sep='\t')
    #print("Original DataFrame:")
    #print(df.head())
    return df 

def clean_data(data: pd.DataFrame, country: Region) -> pd.DataFrame:
    """Clean and process life expectancy data."""
    if country.name not in Region.get_actual_countries():
        raise ValueError(f"Invalid country: {country.name}")

    if 'unit,sex,age,geo\\time' in data.columns:
        data[['unit', 'sex', 'age', 'region']] = data['unit,sex,age,geo\\time'].str.split(',', expand=True)
        data.drop(columns=data.columns[0], inplace=True)
    else:
        print("Column 'unit,sex,age,geo\\time' not found in data.")

    df = pd.melt(data, id_vars=['unit', 'sex', 'age', 'region'], var_name='year', value_name='value')
    df['value'] = df['value'].str.replace(r'[^0-9.]', '', regex=True)
    df['value'] = df['value'].replace('', np.nan)
    df['year'] = df['year'].astype(int)
    df['value'] = df['value'].astype(float)
    df = df[df['region'] == country.name]
    df = df.dropna(subset=['value'])

    #print("Cleaned DataFrame:")
    #print(df.head(10)) 

    return df

def save_data(df: pd.DataFrame, filename: str = 'life_expectancy/data/pt_life_expectancy.csv'):
    """Save cleaned life expectancy data to a file."""
    df.to_csv(filename, index=False)

def main() -> None:
    parser = argparse.ArgumentParser(description='Life expectancy data for all countries.')
    parser.add_argument('--output-dir', type=str, default='data/', help='Specify the output directory for cleaned data')
    args = parser.parse_args()

    raw_data = load_data()

    for country in Region:
        if country.name in Region.get_actual_countries():
            cleaned_data = clean_data(raw_data, country)
            save_data(cleaned_data, f"{args.output_dir}/{country.value.lower()}_life_expectancy.csv")

if __name__ == '__main__':
    main()
