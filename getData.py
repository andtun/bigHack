import requests
from bighack.core.models import Building


API_KEY = "48f3e592a2e05752f4d6a94b4e4cdca8"
MAIN_URL = "https://apidata.mos.ru/v1/datasets/1022/"

DATA_URL = MAIN_URL + "rows?projection=null&api_key=%s&$top=%s&$skip=%s"
NUMBER_URL = MAIN_URL + "count?api_key=%s"


def get_data():

    # get offers number
    url = NUMBER_URL % API_KEY
    r = requests.get(url)
    print(r.status_code)
    if r.status_code == 200:
        number = int(r.text)
    else:
        number = 0

    # get offers by packs of 500
    for offset in range(0, number, 500):
        url = DATA_URL % (API_KEY, 500, offset)
        r = requests.get(url)
        if r.status_code == 200:
            allData = r.json()
            for d in allData:
                data = d['Cells']
                b = Building()
                b.address = data['Address']
                b.license = data['EGRPLicenceNumber']
                b.square = data['ObjectArea']
                b.historic = (data['HistoricalAndCulturalHeritageCategory'] is not None)
                b.latitude = data['geoData']['coordinates'][1]
                b.longtuide = data['geoData']['coordinates'][0]
                b.save()
        else:
            print("fail")
