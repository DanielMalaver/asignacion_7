import requests
from pprint import pprint
import json
import time

while(1):
    response = requests.post(
        'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
        headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
    response.raise_for_status()
    payload=response.json()
    pprint(payload)

    response2 = requests.get(
        'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
        headers={'X-Auth-Token':payload['Token']})
    payload2 = response2.json()['response']
    Output = []
    for i in range(len(payload2)):
        Output.append([payload2[i]['family'],payload2[i]['hostname'],payload2[i]['managementIpAddress'],payload2[i]['lastUpdated'],payload2[i]['reachabilityStatus']])
    pprint(Output)

    data = {}
    data['Equipos'] = []

    for i in range(len(payload2)):
        data['Equipos'].append({
        'hostname': payload2[i]['hostname'],
        'status': payload2[i]['reachabilityStatus']})

    with open('list.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Proxima petición en 5 minutos")
    time.sleep(60*5)
