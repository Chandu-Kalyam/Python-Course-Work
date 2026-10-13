import pytest
import pandas as pd

#  create 2D array/ Matrix / DataFrame using pandas.

@pytest.fixture
def sample_data():
    df = pd.DataFrame({
        "Age": [22, 42, 16],
        "Salary": [10, 11, 100],
        "target": [0, 1, 0],
        
    })

    return df

# checking shape of data
def test_data1(sample_data):
    assert sample_data.shape == (3, 3)  # check shape of data
    
    # check if target is expected value or not
def test_data2(sample_data):
    expected_target = [0, 1, 0]
    assert sample_data["target"].tolist() == expected_target  # check if target is expected value or not
    

