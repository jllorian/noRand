import requests
import random

def create_headers(notion_token):
    return {
        'Authorization': f'Bearer {notion_token}',
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }

def fetch_database_entries(database_id, headers):
    url = f'https://api.notion.com/v1/databases/{database_id}/query'
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
    
def get_random_page(pages):
    if pages:
        return random.choice(pages)
    else:
        return None
    
def display_random_page_info(page):
    if page:
        page_title = page['properties'].get('Name', {}).get('title', [{}])[0].get('plain_text', 'Untitled')
        page_url = page.get('url', 'No URL available')
        return {'title': page_title, 'url': page_url}
    else:
        return {'error': 'No pages found'}