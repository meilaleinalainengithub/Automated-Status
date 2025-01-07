import requests
from time import sleep

TIMER = 3  # In seconds
TOKEN = "your-token" # Replace with your Discord token
URL = "https://discord.com/api/v10/users/@me/settings"
headers = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

def update_status(status):
    status_json = {
        "custom_status": {
            "text": status
        }
    }
    
    response = requests.patch(URL, json=status_json, headers=headers)
    
    if response.status_code == 200:
        print(f"Status updated to: {status}")
    else:
        print(f"Failed to update status: {response.status_code}")
        print(response.text)

while True:
    with open("statuses.txt", "r") as file:
        statuses = file.readlines()

        for i, line in enumerate(statuses, 1):
            status = line.strip()
            update_status(status)
            
            next_line_index = i + 1
            if next_line_index < len(statuses):
                next_line = statuses[next_line_index].strip()
                statuses[i] = next_line + '\n'
            elif next_line_index == len(statuses):
                statuses[i] = statuses[0]
            
            sleep(TIMER)