# Integration + functional test
# Integration test: mutliple module together working fine or not.
# Functional test: check if the software is working as per the requirement or not.
# pip install scikit-learn
from sklearn.linear_model import LogisticRegression # ML Model for classification
from sklearn.preprocessing import StandardScaler   # convert large value to small
import numpy as np
import pandas as pd

# checking ML pipeline using integration testing
def pipeline(x,y):
    # 1. Data Preprocessing
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # 2. Model Training
    model = LogisticRegression()
    model.fit(x_scaled, y)

    return model, scaler


# Integration test: check if the pipeline is working fine or not.
def test_pipeline():
    # Sample data
    x = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])

    model, scaler = pipeline(x, y)

    # Check if the model is trained and scaler is fitted
    assert isinstance(model, LogisticRegression)
    assert isinstance(scaler, StandardScaler)

    # Check if the model can make predictions
    x_test = np.array([[5, 6]])
    x_test_scaled = scaler.transform(x_test)
    prediction = model.predict(x_test_scaled)
    assert prediction in [0, 1]  # prediction should be either 0 or 1
    
from sklearn.metrics import accuracy_score
# functional test: check if the software is working as per the requirement or not.
def test_functional():
    
    y_true = [0,1,0]
    y_pred = [0,1,0]
    acc = accuracy_score(y_true, y_pred)
    assert acc > 0.98  # check if the accuracy is as expected or not
        