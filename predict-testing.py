import requests

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
