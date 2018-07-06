import re

import utils

WEBSITE = 'ptwc'
URL = utils.WEBSITES[WEBSITE]
HEADERS = utils.HEADERS

def start_crawl(cnt=28, write_file=False, show_output=True):
    if(write_file):
        dict_list = []

    landing_page = utils.crawl_page(URL)
    data_rows = landing_page.findAll('tr', { "class": ["gr", "gr_even"] } )
    
    print('PTWC (Pacific Tsunami Warning Center) (Past 30 days)')
    print('URL:', URL)

    for idx, row in enumerate(data_rows):
        if(idx >= cnt):
            break

        datum_dict = {
            "time": row.findAll('td')[0].text,
            "region": row.findAll('td')[1].text,
            "type": row.findAll('td')[2].text,
            "details_link": row.findAll('td')[4].findAll('a')[1]['href']
        }

        details_page = utils.crawl_page(URL+datum_dict['details_link']).find('body').text

        evaluation_re = 'EVALUATION(\r\n|\r|\n){2}([ \w.]+(\r\n|\r|\n))+(\r\n|\r|\n)'
        evaluation_match = re.search(evaluation_re, details_page)
        if(evaluation_match):
            replace_dict = {
                "EVALUATION": '',
                "\r": '',
                "\n": '',
                "\t": ''
            }
            evaluation_match = utils.replace_all(evaluation_match.group(0), replace_dict)
            datum_dict['evaluation'] = evaluation_match
        else:
            print('NO EVALUATION FOUND')
        
        if(show_output):
            utils.print_dict(datum_dict)
        if(write_file):
            dict_list.append(datum_dict)
    
    if(write_file):
        utils.write_json_file(WEBSITE, dict_list)

        

