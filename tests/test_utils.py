import pytest
from unittest.mock import patch, MagicMock
from src.utils import create_headers, fetch_database_entries, get_random_page, display_random_page_info

def test_create_headers():
    token = "test_token"
    headers = create_headers(token)
    assert headers["Authorization"] == f"Bearer {token}"
    assert headers["Content-Type"] == "application/json"
    assert headers["Notion-Version"] == "2022-06-28"

@patch("src.utils.requests.post")
def test_fetch_database_entries(mock_post):
    # Mock successful response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": [{"id": "page1"}, {"id": "page2"}]}
    mock_post.return_value = mock_response

    headers = {"Authorization": "Bearer fake_token"}
    entries = fetch_database_entries("test_db_id", headers)
    assert len(entries) == 2

    # Mock failed response
    mock_response.status_code = 400
    mock_post.return_value = mock_response
    entries = fetch_database_entries("test_db_id", headers)
    assert entries == []

def test_get_random_page():
    pages = [{"id": "page1"}, {"id": "page2"}]
    random_page = get_random_page(pages)
    assert random_page in pages

    # Edge case: empty list
    random_page = get_random_page([])
    assert random_page is None

def test_display_random_page_info():
    page = {
        "properties": {
            "Name": {"title": [{"plain_text": "Test Page"}]}
        },
        "url": "http://example.com"
    }
    result = display_random_page_info(page)
    assert result["title"] == "Test Page"
    assert result["url"] == "http://example.com"

    # Edge case: missing properties
    result = display_random_page_info(None)
    assert result["error"] == "No pages found"