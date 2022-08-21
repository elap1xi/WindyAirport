import requests
import json
import airportsdata as air
airports = air.load()
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = [0]
def fin(icao):
   try:
    airports[icao]
    headers = {
      'Authorization': 'KEY'
    }
    request = requests.get('https://avwx.rest/api/metar/{0}'.format(icao), headers=headers)
    response = json.loads(request.text)
    scmws = response['wind_speed']
    ws = int(scmws['repr'])  # wind speed
    if(a[0]<ws):
        a.append(ws)
        print(f"\nAppend : {icao} = {ws}")
    else:
        print(f"\nNot append : {icao}")
   except:
    print(f"No Station _ {icao}",end="\r")

def s():
    for i in list:
        for j in list:
            for k in list:
                for s in list:
                    icao = i+j+k+s
                    fin(icao)
s()
print(a)
