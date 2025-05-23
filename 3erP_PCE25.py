import requests
import json
#3er Parcial PC
def checarIP(ip, apikey):
    #Código para consultar la API de Abuse IP BD
    url = 'https://api.abuseipdb.com/api/v2/check'
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': apikey
    }
    response = requests.request(method='GET', url=url,
                                headers=headers, params=querystring)
    # Formatted output
    decodedResponse = json.loads(response.text)
    return json.dumps(decodedResponse, sort_keys=True, indent=4)

#Analisis de la API

    if response.status_code == 200:
        score = data['abuseConfidenceScore']
        domain = data.get('domain', 'Dominio no encontrado')
        country = data.get('countryCode', 'Desconocido')
        total_reports = data['totalReports']
   
#Verificar la actividad de la IP para corroborar si es peligrosa o no

    if score == 0:
        return['La IP {ip} no tiene reportes de abuso y se considera segura']
    elif score < 50:
        return ['La IP {ip} tiene algunos reportes ({totalReports}), pero no se considera maliciosa']
    else:
        return['La IP {ip} tiene un alto nivel de reportes ({totalReports}) y se considera maliciosa']

def main():
    apikey = 'e91328a52e454203e996f806aa803356bd725d7e35fce8424c9a0439c853fa4c94ec4c0d26c33b22'
    lista_ips = ['52.123.250.32', '103.172.204.220', '69.98.208.120', '185.93.89.118']

    print("Verificando solo las primeras 3 IPs por límite de la API:\n")

    for ip in lista_ips[:3]:
        resultado = checarIP(ip, apikey) 
        print(resultado)
        print("=" * 50)

if __name__ == "__main__":
    main()


 








