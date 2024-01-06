import argparse
import pandas as pd 
import numpy as np 
from life_expectancy.cleaning import load_data, clean_data, Region 

def create_input_fixture():
    data = load_data()
    sample_data = data.sample(n=300)
    sample_data.to_csv('life_expectancy/tests/fixtures/eu_life_expectancy_raw.tsv', sep='\t', index=False)

def create_expected_fixture(input_fixture, country=Region.PT):
    cleaned_data = clean_data(input_fixture, country)
    cleaned_data.to_csv('life_expectancy/tests/fixtures/pt_life_expectancy_expected.csv', index=False)

def main():
    input_fixture = create_input_fixture()
    output_fixture = create_expected_fixture(input_fixture)
    return output_fixture

if __name__ == '__main__': #It means that when this script is imported elsewhere, 
    #the main() function won't automatically run.
    main()