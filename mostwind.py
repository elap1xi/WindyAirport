import requests
import json
import airportsdata as air
airports = air.load()
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
a = [0]
'''
def fin(ic):
   try:
    airports[ic]
    headers = {
      'Authorization': 'KEY'
    }
    request = requests.get('https://avwx.rest/api/metar/{0}'.format(ic), headers=headers)
    response = json.loads(request.text)
    scmws = response['wind_speed']
    ws = int(scmws['repr'])  # wind speed
    if(a[0]<ws):
        a.append(ws)
        print(f"\nAppend : {ic} = {ws}")
    else:
        print(f"\nNot append : {ic}")
   except:
    print(f"No Station _ {ic}",end="\r")

def s():
    for i in list:
        for j in list:
            for k in list:
                for s in list:
                    ic = i+j+k+s
                    fin(ic)
s()
print(a)
'''
def fin():
 dop = 0
 for i in list:
  for j in list:
    for k in list:
      for s in list:
        ic = i+j+k+s
        try:
            airports[ic]
            headers = {
              'Authorization': 'KEY'
            }
            request = requests.get('https://avwx.rest/api/metar/{0}'.format(ic), headers=headers)
            response = json.loads(request.text)
            scmws = response['wind_speed']
            ws = int(scmws['repr'])  # wind speed
            if(a[0]<ws):
                a.append(ws)
                print(f"\nAppend : {ic} = {ws}")
            else:
                print(f"\nNot append : {ic}")

        except:
            # print(f"No Station _ {ic}",end="\r")
            dop += 1
            if(dop%500==0):
                if(dop%1000==0):
                 print(f"{dop} _ No station, of {ic}")
                 pass
                print(f"{dop} _ No Station")
fin()
print(a)
