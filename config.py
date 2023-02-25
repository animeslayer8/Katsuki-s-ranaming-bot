import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("7165358", "")

API_HASH = os.environ.get("304228f1dc7b9c86ef1c8d83cdc5da85", "")

BOT_TOKEN = os.environ.get("6144893657:AAFtyY6jWx_-m7dYwNZgrAPfFmZhZIsVZ7I", "") 

FORCE_SUB = os.environ.get("https://t.me/+Tr51Cs7pcNdjNDUx", "") 

DB_NAME = os.environ.get("DB_NAME","")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('5347606696', '').split()]

PORT = os.environ.get("PORT", "8080")
