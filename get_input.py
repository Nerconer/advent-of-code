import sys
import os
import requests
from datetime import datetime

year = datetime.now().year

day = sys.argv[1]

url = f'https://adventofcode.com/2023/day/{day}/input'

cookie_session = '...'

response = requests.get(url, cookies={'session': cookie_session})

# If folder not exists, create it
if not os.path.exists(f'./{year}/day_{day}'):
    os.makedirs(f'./{year}/day_{day}')
    # create empty file main.py
    open(f'./{year}/day_{day}/main.py', 'a').close()
    
with open(f'./{year}/day_{day}/input.txt', 'w') as f:
    f.write(response.text)
    
print('Script successfully executed!')