import re

import constant as const

URL = const.WEBSITES['ptwc']
HEADERS = const.HEADERS

def start_crawl(cnt = 28):
    landing_page = const.crawl_page(URL)
    data_rows = landing_page.findAll('tr', { "class": ["gr", "gr_even"] } )
    
    print('PTWC (Pacific Tsunami Warning Center) (Past 30 days)')
    print('URL:', URL)

    for idx, row in enumerate(data_rows):
        if(idx >= cnt):
            break

        print('Time:\t', row.findAll('td')[0].text)
        print('Region:\t', row.findAll('td')[1].text)
        print('Type:\t', row.findAll('td')[2].text)
        details_link = row.findAll('td')[4].findAll('a')[1]['href']
        print('Details Link:', details_link)

        details_page = const.crawl_page(URL+details_link).find('body').text

        evaluation_re = 'EVALUATION(\r\n|\r|\n){2}([ \w.]+(\r\n|\r|\n))+(\r\n|\r|\n)'
        match = re.search(evaluation_re, details_page)
        if(match):
            replace_dict = {
                "EVALUATION": '',
                "\r": '',
                "\n": '',
                "\t": ''
            }
            match = const.replace_all(match.group(0), replace_dict)

            print('Evaluation:', match)
        else:
            print('NO EVALUATION FOUND')
        
        print('-----------------')


        

