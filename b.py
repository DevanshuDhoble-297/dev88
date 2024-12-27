import requests

api_key = "AIzaSyDSw5Gz4gwI2PW36JzuYBgZRrJTBZAwemk"
url = "https://generativelanguage.googleapis.com/v1/models"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers)
print(response.json())
