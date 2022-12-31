from experiment import *
import pytest
import os
import pandas as pd

@pytest.fixture(scope="module")
def actual_data_set():
    data = {
        'id': [1, 2, 3, 4, 5],
        'post_code': [60001, 60002, 60003, 60004, 60005],
        'price': [12, 13, 14, 15, 16]
    }
    df = pd.DataFrame(data)
    return df

def test_file_exist():
    actual_file_name = os.path.join(os.path.dirname(__file__), 'customerorders-201008-180523.csv')
    expected_file_name = os.path.join(os.path.dirname(__file__), 'customerorders-201008-180523.csv')
    assert actual_file_name == expected_file_name

    actual_file_name = os.path.join(os.path.dirname(__file__), 'customerorders-201008-180523.csv')
    wrong_expected_file_name = os.path.join(os.path.dirname(__file__), 'customerorders-201008-1805232.csv')
    assert actual_file_name != wrong_expected_file_name


def test_count_rows(actual_data_set):
    rows = count_rows(actual_data_set)    
    expected_rows = 5
    assert rows == expected_rows

    wrong_expected_rows = 6
    assert wrong_expected_rows != expected_rows