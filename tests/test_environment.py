"""
As the code depends on environmental variables (Notion token, db_ids...) \
this file is used to mock them.
"""

import pytest
from unittest.mock import patch

@patch.dict('os.environ', {'NOTION_TOKEN': 'fake_token', 'DATABASE_IDS': 'db1,db2'})
def test_environment_variables():
    from src.main import load_environment_variables
    notion_token, database_ids = load_environment_variables()
    assert notion_token == 'fake_token'
    assert database_ids == ['db1', 'db2']