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

        # get player name
        player_name = html.find('div', {'class': 'p10'}).find('div', {'class': 'ofh'}).find('h1', {'class': 'c'})
        process_personal(player_name, url, 'name')

        # gets personal information at top of page
        for div in html.findAll('div', {'class': 'indx_b'}):
            find_deepest_personal(div, url)

        # get contract information (assumes url already exists in output)
        i = 0 # represents index of contract in output[url][contracts]
        for div in html.findAll('div', {'class': 'table_c'}):
            find_contract_info(div, url, i)
            i+= 1

# method to get deepest nested divs
def find_deepest_personal(beautiful_html, url):
    if len(beautiful_html.findAll('div')):
        for div in beautiful_html.findChildren('div', recursive=False):
            find_deepest_personal(div, url)
    else:
        process_personal(beautiful_html, url)

# specific method to read a line of player information from a cap friendly page
def process_personal(html, url, key=None):
    string = str(html)
    data = re.findall(">[A-Za-z0-9',\(\):\ ]+<", string)
    if key:
        piece = data[0].replace('>' , '').replace('<', '').replace(':', '').strip().title()
        add_to_output(key, piece, url)
    else:
        key = data[0].replace('>' , '').replace('<', '').replace(':', '').strip().title()
        value = data[1].replace('>' , '').replace('<', '').replace(':', '').strip()
        add_to_output(key, value, url)

# method to find contract tables and pass divs without contract tables
def find_contract_info(div, url, i):
    # ignore non-contract table divs, such as salary progression charts
    if len(div.findAll('div', {'class': 'cntrct'})):
        find_deepest_contract_summary(div.find('div', {'class': 'column_head3 rel cntrct'}), url, i)

# method to find lowest level divs in contract summary section
def find_deepest_contract_summary(beautiful_html, url, i):
    if len(beautiful_html.findAll('div')):
        for div in beautiful_html.findChildren('div', recursive=False):
            find_deepest_contract_summary(div, url, i)
    else:
        process_contract_summary(beautiful_html, url, i)

# method to process contract summary information
def process_contract_summary(div, url, i):
    contract = {}
    string = str(div)
    # not interested in source, not saving to output
    if 'SOURCE' not in string:
        data = re.findall(">[A-Za-z0-9',\(\):\ ]+<", string)
        if len(data) == 1:
            piece = data[0].replace('>' , '').replace('<', '')
            key_value = piece.split(':')
            if len(key_value) == 2:
                key = key_value[0].title().strip()
                value = key_value[1].title().strip()
                add_to_contracts(key, value, url, i)
            else:
                raise Exception('Contract section formatted inconsistent with others')
        elif len(data) > 1:
            raise Exception('Page formatted inconsistent with others')

# simple method to add key value pair to output
def add_to_output(key, value, url):
    if url in output:
        output[url][key] = value
    else:
        output[url] = {key: value,
                       'contracts': [],
                       'contract year': []}

# method to add to a contract
def add_to_contracts(key, value, url, i):
    if len(output[url]['contracts']) <= i:
        output[url]['contracts'].append({
                                       key: value
                                       })
    else:
        output[url]['contracts'][i][key] = value

# get_contract_index_pages()
scrape_player_data('https://www.capfriendly.com/players/connor-mcdavid')
pp.pprint(output)



