import shelve
import string, random
import time
from dotenv import load_dotenv
import os

load_dotenv()
code_len = int(os.getenv('CODE_LEN', 6))
db_path = os.getenv('DB_PATH', 'url_mapping.db')

  
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