import shelve
import string, random
from interval import interval
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
code_len = int(os.getenv('CODE_LEN', 6))
expiry = timedelta(days=float(os.getenv('EXPIRY_DAYS', 7)))
clean_interval = float(os.getenv('CLEAN_INTERVAL_DAYS', 1)) * 60 * 60 * 24  # 24 hours * value
db_path = 'url_mapping.db'

def clean_expired_entries():
    current_time = datetime.now()
    with shelve.open(db_path, writeback=True) as db:
        keys_to_delete = [key for key, value in db.items() if 'timestamp' in value and current_time - datetime.fromtimestamp(value['timestamp']) > expiry]
        print(f"Cleaning up {len(keys_to_delete)} expired entries.")
        for key in keys_to_delete:
            del db[key]
            
def read(code):
    with shelve.open(db_path) as db:
        if code in db:
            return db[code]['url']
        else:
            return None

def write(original_url):
    with shelve.open(db_path, writeback=True) as db:
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_len))
            if code not in db:
                break
        db[code] = {'url': original_url, 'timestamp': time.time()}
        return {'code': code}


def print_all_entries():
    with shelve.open(db_path) as db:
        for key, value in db.items():
            print(f"Code: {key}, URL: {value['url']}, Timestamp: {datetime.fromtimestamp(value['timestamp'])}")

print_all_entries()
interval(clean_expired_entries, clean_interval)  # Clean expired entries every 24 hours