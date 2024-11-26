import pytest
from unittest.mock import patch
from src.main import collect_all_pages, get_random_page

@patch('src.main.fetch_database_entries')
def test_collect_all_pages(mock_fetch):
    # Mock the API response
    mock_fetch.return_value = [{'id': 'page1'}, {'id': 'page2'}]
    
    # Test data
    database_ids = ['db1', 'db2']
    headers = {'Authorization': 'Bearer fake_token'}
    
    # Call the function
    all_pages = collect_all_pages(database_ids, headers)
    
    assert len(all_pages) == 4  # 2 pages per database
    mock_fetch.assert_called()  # Ensure mock was called
    assert mock_fetch.call_count == len(database_ids)

def test_get_random_page():
    pages = [{'id': 'page1'}, {'id': 'page2'}]
    random_page = get_random_page(pages)
    assert random_page in pages