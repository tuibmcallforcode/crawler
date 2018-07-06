# Crawler

### Introduction
Ken is going to craw some website ;)

### Website Check List
*(abbreviation) WebURL*
- [x] (ptwc)        https://ptwc.weather.gov/ **by N'Ken**
- [x] (ec) https://ec.europa.eu/echo/what/civil-protection/emergency-response-coordination-centre-ercc_en **by N'Ken**
- [ ] (fema)        https://www.fema.gov/
- [ ] (dfes)        http://DFES.WA.GOV.AU
- [ ] (floodlist)   http://floodlist.com
- [ ] (pnsn)        http://pnsn.org
- [ ] (geonet)      http://geonet.org.nz
- [ ] (sms-tsunami) http://sms-tsunami-warning.com
- [ ] (jma)         https://www.jma.go.jp/jma/en/Activities/eew.html
- [ ] (skywarn)     https://www.skywarn.org/news/
- [ ] (nhc)         https://www.nhc.noaa.gov/
- [ ] (emergency-cdc) https://emergency.cdc.gov/han/index.asp
- [ ] (ndwc)        http://www.ndwc.go.th/

### api เกี่ยวกับ disaster

- [ ] https://reliefweb.int/updates 

### How to run this project
**Docker**
- [ ] Dockerfile, docker-compose.yml

**Manually**
```
pip install -r requirements.txt
python main.py
```
According to main.py example code 
```
# import ptwc (website abbreviation)
# import ec (website abbreviation)

ptwc.start_crawl(cnt=2, write_file=True, 
show_output=True) # 2 record, write json file, show crawling output
twc.start_crawl(write_file=True, show_output=True) # write json file, show crawling output
```


**Example output** (*ptwc* website)
```
Time:    03 Jul 2018 12:24
Region:  In the Summit Region of Kilauea Volcano
Type:    Local Information Statement
Details Link: /ptwc/text.php?id=hawaii.TIBHWX.2018.07.03.1224
Evaluation:  NO TSUNAMI IS EXPECTED. REPEAT. NO TSUNAMI IS EXPECTED.
-----------------
```