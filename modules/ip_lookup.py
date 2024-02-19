import requests

def lookup_ip(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    if response.status_code == 200:
        data = response.json()
        # Return multiple values as needed
        return (data['isp'], data['city'], f"{data['lat']}, {data['lon']}")
    else:
        return ("Lookup failed", "", "")
