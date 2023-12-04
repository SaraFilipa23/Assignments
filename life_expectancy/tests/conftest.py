"""Pytest configuration file"""

import pandas as pd
import pytest

from . import OUTPUT_DIR
from life_expectancy.tests.Fixtures_created import create_input_fixture, create_expected_fixture


@pytest.fixture(scope="session")
def eu_life_expectancy_raw_fixture() -> pd.DataFrame:
    """Fixture to load the input raw data for the cleaning script"""
    return create_input_fixture()

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    input_fixture = create_input_fixture()
    return create_expected_fixture(input_fixture)
