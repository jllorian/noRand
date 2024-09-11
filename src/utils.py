import requests

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