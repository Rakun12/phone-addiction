# Phone Addiction Classifier

### Table of Contents
- [Problem Statement](### Problem Statement)
- [About The Repository](### About the repository)
- [The Data Used](### The Data Used)
- [How to Run The Project]

### Problem Statement
This project about phone addiction classifier. The goal for this project is model that can classify the addiction level of the user. The level scaled from 0 to 4, the bigger the number, the more addiction the user is.
The data used is from kaggle and can be download from this link: 
https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset

The features inside this dataset is:
- User ID
- Device Model
- Operating System
- App Usage Time (min/day)
- Screen On Time (hours/day)
- Battery Drain (mAh/day)
- Number of Apps Installed
- Data Usage (MB/ day)
- Age
- Gender
- User Behavior Class

### About the repository

This folder include some file:
- `Mobile Device Usage and User Behavior.ipynb` : the notebook used to preprocess the data, modeling, and doin EDA
- `train.py` : Exactly same as the ipynb file, but simple version of it. Modeling used inside this file is Naive Bayes Gaussian only, rather than using KNN and XGBoost like in the ipynb file.
- `predict.py` : File used to predict and serving with Flask
- `model_nbgaussian.bin` : Pickle file that includes inside `dv` (DictVectorizer), and the `model` using NBGaussian
- `Pipfile` and `Pipfile.lock` : pipenv file, inside this library used for this project
- `Dockerfile` : Docker file to run docker with it

### The Data Used

After doing EDA, the data used is only:
App Usage Time (min/day)
- Screen On Time (hours/day)
- Battery Drain (mAh/day)
- Number of Apps Installed
- Data Usage (MB/ day)
- Gender (female:0, male: 1)
- User Behavior Class (turn it into (0 to 4), rather than 1 to 5 like in the dataset)
