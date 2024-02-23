import requests
from bs4 import BeautifulSoup # for parsing HTML of the website

def lookup_ip(ip):
    url = f"https://ipinfo.io/{ip}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Geo Table Extraction
        geo_info = {item.find_all("td")[0].text: item.find_all("td")[1].text 
                    for item in soup.select(".geo-table tr")}

        city = geo_info.get("City", "City information not available")
        state = geo_info.get("State", "State information not available")
        country = geo_info.get("Country", "Country information not available")
        coordinates = geo_info.get("Coordinates", "Coordinates information not available")

        # Summary Section Extraction
        summary_section = soup.find('div', class_='card card-details mt-0')
        summary_info = {}
        if summary_section:
            for row in summary_section.find_all("tr"):
                key = row.find("td").text.strip()
                value = row.find("td").find_next_sibling("td").text.strip()
                summary_info[key] = value

        # Extracting specific details from the Summary section
        company = summary_info.get("Company", "Company information not available")
        asn_type = summary_info.get("ASN type", "ASN type information not available")
        # Assuming Abuse Contact is no longer needed, but you can add it similarly
        privacy = summary_info.get("Privacy", "Privacy information not available")

        return city, state, country, coordinates, asn_type, privacy, company
    else:
        return "Lookup failed due to network error", "", "", "", "", ""