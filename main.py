import random
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

users = ["user1", "user2", "user3", "user4", "user5"]

selected_users = []

def select_random_users(n):
    global users, selected_users
    
    if len(users) - len(selected_users) < n:
        selected_users = []

    available_users = [user for user in users if user not in selected_users]
    chosen_users = random.sample(available_users, n)
    selected_users.extend(chosen_users)

    return chosen_users

def send_to_api(endpoint, auth_token, chosen_users):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {auth_token}"
    }
    response = requests.post(endpoint, data=json.dumps(chosen_users), headers=headers)
    
    if response.status_code == 200:
        print("Users sent successfully!")
    else:
        print(f"Failed to send users. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    number_of_users = int(os.getenv("NUMBER_OF_USERS"))
    api_endpoint = os.getenv("API_ENDPOINT")
    auth_token = os.getenv("AUTH_TOKEN")

    chosen_users = select_random_users(number_of_users)
    print(f"Chosen users: {chosen_users}")
    
    send_to_api(api_endpoint, auth_token, chosen_users)
