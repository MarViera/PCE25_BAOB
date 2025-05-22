import requests
import json
#3er Parcial PC
def checarIP():
    #Código para consultar la API de Abuse IP BD
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': '52.123.250.32',
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': '1351d01769557d0f4f0e59265e9b3b401a122bac5c33b6fcbf15ac6f7a1d7e55b5d53ff5f43a287c'
    }
    response = requests.request(method='GET', url=url,
                                headers=headers, params=querystring)
    # Formatted output
    decodedResponse = json.loads(response.text)
    return json.dumps(decodedResponse, sort_keys=True, indent=4)

def main():
    #todo el codigo del proyecto estará aquí
    print("Hola mundo")
    print(checarIP())


if __name__ == "__main__":
    main()
