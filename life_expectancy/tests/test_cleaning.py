"""Tests for the cleaning module"""

import pandas as pd
import pytest
from life_expectancy.tests.Fixtures_created import create_input_fixture, create_expected_fixture
from life_expectancy.cleaning import clean_data

@pytest.fixture
def input_fixture():
    return create_input_fixture()

@pytest.fixture
def expected_fixture(input_fixture):
    return create_expected_fixture(input_fixture)

def test_clean_data(input_fixture, expected_fixture):
    cleaned_data = clean_data(input_fixture, 'PT')
    pd.testing.assert_frame_equal(cleaned_data, expected_fixture)