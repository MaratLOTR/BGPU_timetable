import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL_CONFIG = os.environ.get('DATABASE_URL')