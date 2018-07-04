import requests
from bs4 import BeautifulSoup as soup

HEADERS = { 
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

WEBSITES = {
    'ptwc': 'https://ptwc.weather.gov',
    'ec': 'https://ec.europa.eu/echo/what/civil-protection/emergency-response-coordination-centre-ercc_en',
    'fema': 'https://www.fema.gov',
    'dfes': 'http://DFES.WA.GOV.AU',
    'floodlist': 'http://floodlist.com',
    'pnsn': 'http://pnsn.org',
    'geonet': 'http://geonet.org.nz',
    'sms-tsunami': 'http://sms-tsunami-warning.com',
    'jma': 'https://www.jma.go.jp/jma/en/Activities/eew.html',
    'skywarn': 'https://www.skywarn.org/news',
    'nhc':'https://www.nhc.noaa.gov',
    'emergency-cdc':'https://emergency.cdc.gov/han/index.asp',
    'ndwc':'http://www.ndwc.go.th'
}


def replace_all(text, replace_dict):
    for key in replace_dict:
        text = text.replace(key, replace_dict[key])
    return text

def crawl_page(url):
    response = requests.get(url, headers=HEADERS)
    page = soup(response.content, "html5lib")

    return page