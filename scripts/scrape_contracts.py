from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

import pprint
pp = pprint.PrettyPrinter(indent=1)

output = {}

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0}: {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
    print(e)

def get_contract_index_pages():
    year_page_dict = {
        '2019': {
            'active': 15,
            'free-agents': 2
        }
    }

    for year in year_page_dict:
        for section in year_page_dict[year]:
            for page in range(1, year_page_dict[year][section] + 1):
                # have to iterate range up by one to include final page
                url = 'https://www.capfriendly.com/browse/{0}/{1}/caphit/all/all/all/desc/{2}'.format(section, year, str(page))
                get_player_pages(url)

def get_player_pages(url):
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        for tr in html.select('tbody tr'):
            player_page = tr.find('a')['href']
            scrape_player_data('https://www.capfriendly.com' + player_page)

    # raise Exception('Error retrieving contents at {}'.format(url))

def scrape_player_data(url):
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        # gets personal information at top of page
        for div in html.findAll('div', {'class': 'indx_b'}):
            find_deepest(div)

# method to get deepest nested divs
def find_deepest(beautiful_html):
    # print(beautiful_html)
    # print(len(beautiful_html.findAll('div')))

    if len(beautiful_html.findAll('div')):
        for div in beautiful_html.findChildren('div', recursive=False):
            find_deepest(div)
    else:
        process_span(str(beautiful_html))

# specific method to read a line of player information from a cap friendly page
def process_span(div):
    data = re.findall(">[A-Za-z0-9',\(\):\ ]+<", div)
    key = data[0].replace('>' , '').replace('<', '').replace(':', '').strip()
    value = data[1].replace('>' , '').replace('<', '').replace(':', '').strip()
    print(key)
    print(value)

# get_contract_index_pages()
scrape_player_data('https://www.capfriendly.com/players/connor-mcdavid')



