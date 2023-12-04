"""Tests for the cleaning module"""

import pandas as pd
import pytest
from unittest.mock import patch
from life_expectancy.tests.Fixtures_created import create_input_fixture, create_expected_fixture
from life_expectancy.cleaning import clean_data, save_data

# Fixture for input data
@pytest.fixture
def input_fixture():
    return create_input_fixture()

# Fixture for expected output
@pytest.fixture
def expected_fixture(input_fixture):
    return create_expected_fixture(input_fixture)

# Test for clean_data function
def test_clean_data(input_fixture, expected_fixture):
    cleaned_data = clean_data(input_fixture, 'PT')
    pd.testing.assert_frame_equal(cleaned_data, expected_fixture)

# Test for save_data function using mocking
@patch('pandas.DataFrame.to_csv')
def test_save_data(mock_to_csv, input_fixture):
    # Call the function that saves the data
    save_data(input_fixture)

    # Assert that the to_csv method was called
    mock_to_csv.assert_called_once_with('life_expectancy/data/pt_life_expectancy.csv', index=False)
