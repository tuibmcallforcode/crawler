# Crawler

### Introduction
Ken is going to craw some website ;)

### Website Check List

- [x] https://ptwc.weather.gov/ **by N'Ken**
- [x] https://ec.europa.eu/echo/what/civil-protection/emergency-response-coordination-centre-ercc_en **by N'Ken**
- [ ] https://www.fema.gov/
- [ ] http://DFES.WA.GOV.AU
- [ ] http://floodlist.com
- [ ] http://pnsn.org
- [ ] http://geonet.org.nz
- [ ] http://sms-tsunami-warning.com
- [ ] https://www.jma.go.jp/jma/en/Activities/eew.html
- [ ] https://www.skywarn.org/news/
- [ ] https://www.nhc.noaa.gov/
- [ ] https://emergency.cdc.gov/han/index.asp
- [ ] http://www.ndwc.go.th/

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
ptwc.start_crawl(cnt=2, write_file=True, show_output=True) # 2 record, write json file, show crawling output
```
result will be only first record of the web page.

**Example output** (*ptwc* website)
```
Time:    03 Jul 2018 12:24
Region:  In the Summit Region of Kilauea Volcano
Type:    Local Information Statement
Details Link: /ptwc/text.php?id=hawaii.TIBHWX.2018.07.03.1224
Evaluation:  NO TSUNAMI IS EXPECTED. REPEAT. NO TSUNAMI IS EXPECTED.
-----------------
```