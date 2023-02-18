import os
from dotenv import load_dotenv

load_dotenv()


def get_db_url():
    return os.getenv('DB_CONNECTION_URL')
