import shodan
def buscar_shodan(api_key):
    sites=[]
    try:
        #api_key="jsYZ968byb9RN4a0sHcwKrMqrag38MH5" INgresada por el usuario para mayor flexibilidad
        objShodan=shodan.Shodan(api_key)
        resultados=objShodan.search("Port: 21, Anonymous user logged in")
        print("Hosts encontrados: ",len(resultados["matches"]))

        #Obtener detalles
        for match in resultados['matches']:
            ip=match.get('ip_str')
            org=match.get('org','N/A')
            isp=match.get('ISP',"N/A")
            country=match.get('location',{}.get('country_name','N/A'))
            city=match.get("location", {}.get('city','N/A'))
            hostnames=match.get('hostnames',[])
            hostname = hostnames[0] if hostnames else 'N/A'
            os=match.get('os','N/A')

            #Mostrar detalles
            print(f"IP: {ip}")
            print(f"Organizacion: {org}")
            print(f"ISP: {isp}")
            print(f"Pais: {country}")
            print(f"Ciudad: {city}")
            print(f"Nombre del host: {hostname}")
            print(f"Sistema Operativo: {os}")
            print("-"*50)
            sites.append({
                'ip': ip,
                'organization': org,
                "country":country,
                'city':city,
                'hostname':hostname,
                'os':os
            })
    except shodan.APIError as e:
        print(f"Error: {e}")
        return
    return sites