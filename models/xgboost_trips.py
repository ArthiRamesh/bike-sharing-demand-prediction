import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import pickle

trips = pd.read_csv("C:/Workspace/bike-sharing/datasets/trips_data.csv")
X_trips = trips.iloc[:, 0:4].values
y_trips = trips.iloc[:,4].values
X, y = shuffle(X_trips, y_trips, random_state=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.8)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

params = {'n_estimators': 500, 'max_depth': 15, 'min_samples_split': 10,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

xgboost_trips = clf.fit(X_train, y_train)


pickle.dump(clf, open('models/xgboost_trips.pkl','wb'))

model = pickle.load(open('models/xgboost_trips.pkl','rb'))
