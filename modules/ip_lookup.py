import requests

def lookup_ip(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}')
    if response.status_code == 200:
        data = response.json()
        # Check if the request was successful
        if data['status'] == 'success':
            # Return the relevant information
            return (data['isp'], data['city'], f"{data['lat']}, {data['lon']}")
        else:
            # Handle private range or other errors
            return (f"Error: {data.get('message', 'Unknown error')}", "", "")
    else:
        return ("Lookup failed due to network error", "", "")