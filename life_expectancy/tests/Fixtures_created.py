import argparse
import pandas as pd 
import numpy as np 
from life_expectancy.cleaning import load_data, clean_data

def create_input_fixture():
    data = load_data()
    sample_data = data.sample(n=300, random_state=42)
    sample_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_raw.tsv', sep='\t', index=False)
    return sample_data

def create_expected_fixture(input_fixture):
    cleaned_data = clean_data(input_fixture, 'PT')
    cleaned_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_expected.csv', index=False)
    return cleaned_data

def main():
    input_fixture = create_input_fixture()
    output_fixture = create_expected_fixture(input_fixture)
    return output_fixture

if __name__ == '__main__': #It means that when this script is imported elsewhere, 
    #the main() function won't automatically run.
    main()