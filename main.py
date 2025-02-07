import time
import logging
from itertools import cycle
import requests

# Configuration
TIMER = 5  # In seconds
TOKEN = "your-token"  # Replace with your Discord token
URL = "https://discord.com/api/v10/users/@me/settings"
STATUSES_FILE = "statuses.txt"

# Setup logging with a fancy lil' library
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_statuses(file_path):
    """Load statuses from a file, skipping blank lines."""
    try:
        with open(file_path, "r") as file:
            statuses = [line.strip() for line in file if line.strip()]
            if not statuses:
                logging.warning("No statuses found in '%s'.", file_path)
            return statuses
    except FileNotFoundError:
        logging.error("File '%s' not found. Please create it with some statuses.", file_path)
        return []

def update_status(session, status):
    """Send a PATCH request to update the custom status."""
    payload = {"custom_status": {"text": status}}
    try:
        response = session.patch(URL, json=payload)
        if response.ok:
            logging.info("Status updated to: %s", status)
        else:
            logging.error("Failed to update status (%s): %s", response.status_code, response.text)
    except requests.RequestException as e:
        logging.error("An error occurred: %s", e)

def main():
    statuses = load_statuses(STATUSES_FILE)
    if not statuses:
        return

    # Create a session cause thats more efficicente
    with requests.Session() as session:
        session.headers.update({
            "Authorization": TOKEN,
            "Content-Type": "application/json"
        })
        for status in cycle(statuses):
            update_status(session, status)
            time.sleep(TIMER)

if __name__ == "__main__":
    main()
