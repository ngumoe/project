import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Pinterest token from .env
access_token = os.getenv('PINTEREST_ACCESS_TOKEN')
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

print("🔍 Fetching your Pinterest boards...")

# Get all boards
response = requests.get("https://api.pinterest.com/v5/boards", headers=headers)

if response.status_code == 200:
    boards = response.json()
    print("✅ Success! Here are your boards:\n")
    
    for board in boards.get('items', []):
        print(f"📌 Board Name: {board['name']}")
        print(f"🆔 Board ID: {board['id']}")
        print(f"📝 Description: {board.get('description', 'No description')}")
        print("─" * 50)
        
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)