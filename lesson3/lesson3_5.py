import json
from pprint import pprint
class Site:
    def __init__(self,
                 sitename,
                 county,
                 aqi,
                 pollutant,
                 status,
                 pm2_5,
                 pm2_5_avg,
                 latitude,
                 longitude,
                 datacreationdate):   
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.pm2_5_avg = pm2_5_avg
        self.latitude = latitude
        self.longitude = longitude
        self.datacreationdate = datacreationdate

def parse_sites_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    site_list = []
    for record in data['records']:
        site = Site(
            sitename=record['sitename'],
            county=record['county'],
            aqi=record['aqi'],
            pollutant=record['pollutant'],
            status=record['status'],
            pm2_5=record['pm2.5'],
            pm2_5_avg=record['pm2.5_avg'],
            latitude=record['latitude'],
            longitude=record['longitude'],
            datacreationdate=record['datacreationdate']
        )
        site_list.append(site)
    return site_list

parsed_sites = parse_sites_from_json('aqx_p_488.json')
for site in parsed_sites:
    print(f"站點名稱: {site.sitename}, 所在縣市: {site.county}, AQI: {site.aqi}, 主要污染物: {site.pollutant}")