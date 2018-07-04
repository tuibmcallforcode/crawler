from bs4 import BeautifulSoup as soup
import requests
import re

import constant as const

URL = const.WEBSITES['ptwc']
HEADERS = const.HEADERS

def replace_all(text, replace_dict):
    for key in replace_dict:
        text = text.replace(key, replace_dict[key])
    return text

def crawl_page(url):
    response = requests.get(url, headers=HEADERS)
    page = soup(response.content, "html5lib")

    return page

def start_crawl(cnt = 28):
    landing_page = crawl_page(URL)
    data_rows = landing_page.findAll('tr', { "class": ["gr", "gr_even"] } )
    
    for idx, row in enumerate(data_rows):
        if(idx >= cnt):
            break

        print('Time:\t', row.findAll('td')[0].text)
        print('Region:\t', row.findAll('td')[1].text)
        print('Type:\t', row.findAll('td')[2].text)
        details_link = row.findAll('td')[4].findAll('a')[1]['href']
        print('Details Link:', details_link)

        details_page = crawl_page(URL+details_link).find('body').text

        evaluation_re = 'EVALUATION(\r\n|\r|\n){2}([ \w.]+(\r\n|\r|\n))+(\r\n|\r|\n)'
        match = re.search(evaluation_re, details_page)
        if(match):
            replace_dict = {
                "EVALUATION": '',
                "\r": '',
                "\n": '',
                "\t": ''
            }
            match = replace_all(match.group(0), replace_dict)

            print('Evaluation:', match)
        else:
            print('NO EVALUATION FOUND')
        
        print('-----------------')


        

