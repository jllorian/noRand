import requests
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for Notion API accesss
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_IDS = os.getenv('DATABASE_IDS')

if not NOTION_TOKEN or not DATABASE_IDS:
    raise ValueError("Environment variables must be set")
DATABASE_IDS = DATABASE_IDS.split(',')

# Headers
# Manually updated: 'Notion-Version' is declare to avoid breaking changes that might occur if the API were updated without the client being aware.
headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

def fetch_database_entries(database_id):
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error fetching database {database_id}:{response.status_code} - {response.text}")
        return None
    
def get_random_page():
    all_pages = []
    for db_id in DATABASE_IDS:
        entries = fetch_database_entries(db_id)
        if entries:
            all_pages.extend(entries)
            
    if all_pages:
        random_page = random.choice(all_pages)
        return random_page
    else:
        return None
    
def main():
    random_page = get_random_page()
    if random_page:
        page_id = random_page['id']
        page_title = random_page['properties'].get('Name', {}).get('title', [{}])[0].get('plain_text', 'Untitled')
        page_url = random_page['url']
        print(f"Random page selected: {page_title}")
        print(f"Page URL: {page_url}")
    else:
        print("No pages found in the specified databases.")
        
if __name__ == "__main__":
    main()