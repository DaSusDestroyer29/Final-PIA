import requests
def buscar_datos(api_key,ip_address):    
    url = f'https://api.abuseipdb.com/api/v2/check'    
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Resultados del IP:")
        print(f"IP Address: {data['data']['ipAddress']}")
        print(f"Is Public: {data['data']['isPublic']}")
        print(f"IP Version: {data['data']['ipVersion']}")
        print(f"Is Whitelisted: {data['data']['isWhitelisted']}")
        print(f"Abuse Confidence Score: {data['data']['abuseConfidenceScore']}")
        print(f"Country Code: {data['data']['countryCode']}")
        print(f"Usage Type: {data['data']['usageType']}")
        print(f"ISP: {data['data']['isp']}")
        print(f"Domain: {data['data']['domain']}")
        print(f"Total Reports: {data['data']['totalReports']}")
        print(f"Last Reported At: {data['data']['lastReportedAt']}")
    else:
        print(f'Error: {response.status_code} - {response.text}')
if __name__=="main":
    api_key=input("Ingresa tu api key: \n")
    ip_address = input("Inserta la IP que quieres consultar:\n")
    buscar_datos(api_key,ip_address)