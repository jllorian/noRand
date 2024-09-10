# NoRad
> Notion Random Page Fetcher

This project is a Python script that interacts with the [Notion API](https://developers.notion.com/reference/intro) to fetch entries from specified databases and select a random page. It's designed to help users explore their Notion content in a dynamic and engaging way.

## Features
1. **Fetch Notion Database Entries**: Connects to the Notion API to retrieve entries from specified databases.
2. **Get a Random Page**: Randomly selects a page from the fetched entries and displays its title and URL.

## Getting Started
### Prerequisites
- Python 3.x
- Virtual environment (optional but highly recommended)
- [Notion API integration token](https://www.notion.so/profile/integrations)
### Installation
1. Clone the Repository
   ```
   git clone https://github.com/yourusername/NotionRandomPageFetcher.git
   cd NotionRandomPageFetcher
   ```
2. Create a Virtual Environment (I tend to do so in the inmediate upper folder)
   ```
   python -m venv ../venv
   source ../venv/bin/activate # On Windows, use `venv\Scripts\activate`
```
3. Install Required Packages


## Token and .env file
Replace your_integration_token with your actual Notion integration token, and list the database IDs you want to include, separated by commas and **whithout blank spaces**
```
NOTION_TOKEN=your_integration_token
DATABASE_IDS=database_id1,database_id2,database_id3
````
