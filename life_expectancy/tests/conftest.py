"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR



@pytest.fixture(scope="session")
def eu_life_expectancy_input() -> pd.DataFrame:
    """Fixture to load the input data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.tsv")

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")

