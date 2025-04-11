import os
from dotenv import load_dotenv
from simple_salesforce import Salesforce

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')+os.getenv('SECURITY_TOKEN')

def get_salesforce_connection():
    return Salesforce(
        username=USERNAME,
        password=PASSWORD,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET
    )

sf = get_salesforce_connection()