import os
import random
import requests
from dotenv import load_dotenv

# Load and return environment variables.
def load_environment_variables():
    NOTION_TOKEN = os.getenv('NOTION_TOKEN')
    DATABASE_IDS = os.getenv('DATABASE_IDS')
    if NOTION_TOKEN is None or DATABASE_IDS is None:
        raise ValueError("Environment variables must be set")
    return NOTION_TOKEN, DATABASE_IDS.split(',')

# Headers for Notion API requests.
# Manually updated: 'Notion-Version' is declare to avoid breaking changes that might occur if the API were updated without the client being aware.
def create_headers(notion_token):
    return {
        'Authorization': f'Bearer {notion_token}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }

# Fetch entries from a Notion database and returns them.
def fetch_database_entries(database_id, headers):
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Error fetching database {database_id}:{response.status_code} - {response.text}")
        return []

# List all pages from the specified databases
def collect_all_pages(database_ids, headers):
    all_pages = []
    for db_id in database_ids:
        entries = fetch_database_entries(db_id, headers)
        all_pages.extend(entries)
    return all_pages


# Select and return a random page from the list of pages.
def get_random_page(pages):
    if pages:
        return random.choice(pages)
    else:
        return None

# Display the title and URL of the selected random page
def display_random_page_info(page):
    if page:
        page_id = page['id']
        page_title = page['properties'].get('Name', {}).get('title', [{}])[0].get('plain_text', 'Untitled')
        page_url = page['url']
        print(f"Random page selected: {page_title}")
        print(f"Page URL: {page_url}")
    else:
        print("No pages found in the specified databases.")

# Main function to execute the script
def main():
    load_dotenv()
    try:
        notion_token, database_ids = load_environment_variables()
    except ValueError as e:
        print(e)
        return
    
    headers = create_headers(notion_token)
    all_pages = collect_all_pages(database_ids, headers)
    random_page = get_random_page(all_pages)
    display_random_page_info(random_page)

if __name__ == "__main__":
    main()