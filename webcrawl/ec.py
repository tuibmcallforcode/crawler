import re

import utils

WEBSITE = 'ec'
URL = utils.WEBSITES[WEBSITE]
HEADERS = utils.HEADERS

NEWS_LANDING_URL = ['https://ec.europa.eu/echo/news/more/314/402_en', 'https://ec.europa.eu/echo/news/more/314/402_en?page=']

def start_crawl(cnt=10000, write_file=False, show_output=True):
    try:
        news_end_points = crawl_news_end_point(cnt, write_file, show_output)
        # news_end_points = ['/echo/news/sahel-crisis-eu-gives-%E2%82%AC142-million-humanitarian-aid-2014_en']
        if(write_file):
            dict_list = []
            cnt_down = len(news_end_points)

        for end_point in news_end_points:
            page = utils.crawl_page(URL+end_point)

            date_re = '(\d){2}/(\d){2}/(\d){4}'
            publication_date = page.find('div', { "class": "row c_left field field-field_news_publication_date last" }).text
            publication_date = re.search(date_re, publication_date).group(0)

            image_url = page.find('div', { "class": "field-item even" }).img
            if image_url:
                image_url = image_url['src'].strip()
            else:
                image_url = ''
                
            datum_dict = {
                "title": page.find('h1', { "class": "title" }).text.strip(),
                "image": image_url,
                "content": page.find('div', { "class": "row c_left field field-body" }).text.strip(),
                "publication_date": publication_date.strip()
            }

            if(show_output):
                utils.print_dict(datum_dict)
                print('cnt left:', cnt_down)
                cnt_down = cnt_down - 1
            if(write_file):
                dict_list.append(datum_dict)

        if(write_file):
            utils.write_json_file(WEBSITE, dict_list)

    except Exception as e:
        print('err:', e)

    
def crawl_news_end_point(cnt=10000, write_file=False, show_output=True):
    if show_output:
        print('collecting endpoint for a while...')

    news_end_points = []

    try:
        landing_url = NEWS_LANDING_URL[0]
        landing_page = utils.crawl_page(landing_url)
        data_rows = landing_page.findAll('h3', { "class": "field-content" })

        for idx, row in enumerate(data_rows):
            if(idx >= cnt):
                break
            
            news_end_points.append(row.a['href']) #collect endpoint

    except Exception as e:
        print('err:', e)

    try:
        landing_url = NEWS_LANDING_URL[1]

        for i in range(1, cnt):
            landing_page = utils.crawl_page(landing_url+str(i))
            data_rows = landing_page.findAll('h3', { "class": "field-content" } )

            if data_rows == []: #no more content on landing page
                break

            for idx, row in enumerate(data_rows):
                if(idx >= cnt):
                    break
            
                news_end_points.append(row.a['href']) #collect endpoint

    except Exception as e:
        print('err:', str(e))
    
    print(news_end_points)
    return news_end_points
        

