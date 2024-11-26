import os
from dotenv import load_dotenv
from utils import create_headers, fetch_database_entries, get_random_page, display_random_page_info

def load_environment_variables():
    NOTION_TOKEN = os.getenv('NOTION_TOKEN')
    DATABASE_IDS = os.getenv('DATABASE_IDS')
    if NOTION_TOKEN is None or DATABASE_IDS is None:
        raise ValueError("Environment variables must be set")
    return NOTION_TOKEN, DATABASE_IDS.split(',')

def collect_all_pages(database_ids, headers):
    all_pages = []
    for db_id in database_ids:
        entries = fetch_database_entries(db_id, headers)
        all_pages.extend(entries)
    return all_pages

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
    
    page_info = display_random_page_info(random_page)
    if 'error' in page_info:
        print(page_info['error'])
    else:
        print(f"Random page selected: {page_info['title']}")
        print(f"Page URL: {page_info['url']}")

if __name__ == "__main__":
    main()