from flask import Flask, request, jsonify
import random
from dotenv import load_dotenv
from utils import create_headers, fetch_database_entries

app = Flask(__name__)

load_dotenv()

