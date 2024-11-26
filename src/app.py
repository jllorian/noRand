from flask import Flask, request, jsonify
from utils import create_headers, fetch_database_entries, get_random_page, display_random_page_info

app = Flask(__name__)

@app.route('/random-page', methods=['POST'])
def fetch_random_page():
    data = request.get_json()
    notion_token = data.get('notion_token')
    database_ids = data.get('database_ids')
    print(f"Received Notion Token: {notion_token}")
    print(f"Received Database IDs: {database_ids}")
    
    if not isinstance(database_ids, list):
        return jsonify({'error': 'Database IDs must be a list'}), 400

    headers = create_headers(notion_token)
    all_pages = []
    for db_id in database_ids:
        entries = fetch_database_entries(db_id, headers)
        all_pages.extend(entries)
    
    random_page = get_random_page(all_pages)
    result = display_random_page_info(random_page)
    print(f"Random Page Info: {result}")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)