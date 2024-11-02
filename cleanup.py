import os
import shelve
import time
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
clean_interval = float(os.getenv('CLEAN_INTERVAL_DAYS', 1)) * 60 * 60 * 24  # 24 hours * value
db_path = os.getenv('DB_PATH', 'url_mapping.db')
expiry = timedelta(days=float(os.getenv('EXPIRY_DAYS', 7)))

def clean_expired_entries():
    current_time = datetime.now()
    with shelve.open(db_path, writeback=True) as db:
        keys_to_delete = [key for key, value in db.items() if 'timestamp' in value and current_time - datetime.fromtimestamp(value['timestamp']) > expiry]
        if keys_to_delete:
            print(f"Cleaning up {len(keys_to_delete)} expired entries.")
        for key in keys_to_delete:
            del db[key]
          
          
while True:
    clean_expired_entries()
    time.sleep(clean_interval)  # Sleep for the specified interval before running again