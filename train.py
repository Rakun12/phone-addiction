#!/usr/bin/env python
# coding: utf-8

# ## Project Description

# This project classify the phone user behavior based on the usage scaling from 1 to 5. The bigger the number, the more user use the phone. The features inside this dataset is:
# - User ID
# - Device Model
# - Operating System
# - App Usage Time (min/day)
# - Screen On Time (hours/day)
# - Battery Drain (mAh/day)
# - Number of Apps Installed
# - Data Usage (MB/ day)
# - Age
# - Gender
# - User Behavior Class
# 
# The dataset used is from kaggle, link: https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.naive_bayes import GaussianNB

import pickle

df = pd.read_csv('data/user_behavior_dataset.csv')

def preprocessing(df):
    # Turn the column names into lowercase
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df.gender = df.gender.str.lower()
    # mapping the user_behavior_class from 0 to 4
    df.user_behavior_class = df.user_behavior_class.map({1:0, 2:1, 3:2, 4:3, 5:4})
    # Mapping the gender into number 
    df.gender = df.gender.map({'female': 0, 'male': 1})

    del df['user_id']

    df_clean = df.drop(['age', 'operating_system', 'device_model'], axis=1)
    
    return df_clean

df_clean = preprocessing(df)

df_full_train, df_test = train_test_split(df_clean, test_size=0.2, random_state=12)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=12)


y_train = df_train.user_behavior_class.values
y_val = df_val.user_behavior_class.values
y_test = df_test.user_behavior_class.values
y_full_train = df_full_train.user_behavior_class.values

del(df_train['user_behavior_class'])
del(df_val['user_behavior_class'])
del(df_test['user_behavior_class'])
del(df_full_train['user_behavior_class'])

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)
df_full_train = df_full_train.reset_index(drop=True)


train_dict = df_train.to_dict(orient='records')
val_dict = df_val.to_dict(orient='records')
test_dict = df_test.to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X_train = dv.fit_transform(train_dict)
X_val = dv.transform(val_dict)
X_test = dv.transform(test_dict)



# ### Modeling with naive bayes
clf = GaussianNB(var_smoothing=0.01)
clf.fit(X_train, y_train)

y_pred = clf.predict_proba(X_val)
roc_auc_score(y_val, y_pred, multi_class='ovr')


output_file = 'model_nbgaussian.bin'
output_file

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, clf), f_out)
