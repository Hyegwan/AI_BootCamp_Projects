import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline, make_pipeline
from category_encoders import OrdinalEncoder 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, accuracy_score

import pickle

data = pd.read_csv('/Users/hyegwan/codestates/project3/heart.csv')

train, test = train_test_split(data, test_size=0.2, random_state=2)

def divide_data(df):

    target = 'HeartDisease'

    X = df.drop(columns = target)
    y = df[target]

    return X, y

X_train, y_train = divide_data(train)
X_test, y_test = divide_data(test)

def fit(X_train, y_train):
    
    pipeline = make_pipeline(
        OrdinalEncoder(), 
        LogisticRegression()
    )

    dists = {
        'logisticregression__C': [0.01, 0.1, 1, 10, 100],
        'logisticregression__penalty':['l1','l2']
    }


    clf = RandomizedSearchCV(
        pipeline, 
        param_distributions = dists, 
        random_state = 2, 
        n_iter = 2, 
        cv = 3,
        scoring = 'f1', 
        verbose = 1, 
        n_jobs = -1
    )
    
    clf.fit(X_train, y_train)
    print("Optimal Hyperparameter:", clf.best_params_)
    print("f1 score:", clf.best_score_)

    return clf

clf = fit(X_train, y_train)

y_test_pred = clf.best_estimator_.predict(X_test)

with open('model.pkl', 'wb') as pickle_file:
    pickle.dump(clf.best_estimator_, pickle_file)