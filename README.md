# Phone Addiction Classifier

### Table of Contents
- [Problem Statement](#problem-statement)
- [About The Repository](#about-the-repository)
- [The Data Used](#the-data-used)
- [How to Run This Project](#how-to-run-this-project)

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


## How to Run This Project

1. Prequisites:\
   First, you need to install [pipenv](https://pipenv.pypa.io/en/latest/) and [docker](https://www.docker.com/products/docker-desktop/).
   
2. Clone this repository:
   ```bash
   git clone https://github.com/Rakun12/phone-addiction.git
   ```
3. Set up the environment\
   Make sure that `pipenv` and `docker` already installed.
   - If `pipenv` didn't install yet, you can run this code:
     ```bash
     pip install pipenv
     ```
4. Build the dockerfile inside:
   ```bash
   docker build -t phone-addiction .
   ```
5. Run the docker image:
   ```bash
   docker run -it phone-addiction
   ```
7. You can access the app through a web browser or API requests, If you have deployed the project using Docker or With the Flask application.
   ```python
   url = 'http://localhost:1212/predict'

   client = {"app_usage_time_(min/day)": 183,
           "screen_on_time_(hours/day)": 4.1,
           "battery_drain_(mah/day)": 1210,
           "number_of_apps_installed": 45,
           "data_usage_(mb/day)": 738,
           "gender": 1,
           "user_behavior_class": 2}
   
   response = requests.post(url, json=client).json()
   print(response)
   ```
