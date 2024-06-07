
## IMPORT BIBLIOTEK
from sklearn.linear_model import Perceptron
import numpy as np
import pickle

## MACIERZE
x = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y = np.array([1, 0, 1, 0])

model = Perceptron()

model.fit(x, y)

## PICKLE
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)