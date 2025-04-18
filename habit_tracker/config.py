"""
config.py — Loads sensitive configuration from the .env file

This file provides access to:
- PIXELA_USERNAME: Your Pixela user ID
- PIXELA_TOKEN: Your Pixela personal token (used for authentication)
- PIXELA_GRAPH_ID: Default graph ID (optional, not used in current CLI)
"""

import os
from dotenv import load_dotenv

# Load .env variables into the environment
load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")
