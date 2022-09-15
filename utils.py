from cgi import test
from symbol import test_nocond
import joblib
import numpy as np
from symbol import test_nocond

def preprocess(Open, High, Low, Volume):
    test_data = np.array([[Open, High, Low, Volume]], dtype=float)
    trained_model = joblib.load("model.pkl")
    prediction = trained_model.predict(test_data)

    return prediction