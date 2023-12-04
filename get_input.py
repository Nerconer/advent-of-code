import sys
import os
import requests
from datetime import datetime

year = datetime.now().year

try:
    day = sys.argv[1]
except IndexError:
    print('Usage: python get_input.py <day>')
    sys.exit(1)

url = f'https://adventofcode.com/2023/day/{day}/input'

cookie_session = str(os.environ.get('AOC_COOKIE'))

response = requests.get(url, cookies={'session': cookie_session})

# If folder not exists, create it
if not os.path.exists(f'./{year}/day_{day}'):
    print(f'Creating folder for day {day}...')
    os.makedirs(f'./{year}/day_{day}')
    # create empty file main.py
    open(f'./{year}/day_{day}/main.py', 'a').close()
else:
    print(f'Folder for day {day} already exists.')

print(f'Writing input.txt for day {day}...')
with open(f'./{year}/day_{day}/input.txt', 'w') as f:
    f.write(response.text)
print('Done!')
