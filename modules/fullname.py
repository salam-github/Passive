import requests
from bs4 import BeautifulSoup  # for parsing HTML

def search_full_name(fullname):
    """Searches for a person's full name and returns the results."""
    # Placeholder for the URL, adjust as necessary
    url = f"https://radaris.com//p/{fullname.replace(' ', '/''')}"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        profiles_list = soup.select_one(".profiles-list")
        
        if profiles_list:
            results = []
            for card in profiles_list.select(".card.teaser-card"):
                full_name_text = card.select_one(".card-title").get_text(strip=True) if card.select_one(".card-title") else "Name not found"
                address = card.select_one(".res-in .many-links-item").get_text(strip=True) if card.select_one(".res-in .many-links-item") else "Address not found"
                phone_number = card.select_one(".teaser-card-item .ph").get_text(strip=True) if card.select_one(".teaser-card-item .ph") else "Phone number not found"
                age_text = card.select_one(".age-wr").get_text(strip=True) if card.select_one(".age-wr") else "Age not found"
                
                # Split the full name to first and last name, handling cases where there may be middle names or initials
                name_parts = full_name_text.split()
                first_name = " ".join(name_parts[:-1])
                last_name = name_parts[-1] if name_parts else ""
                
                # Extract age digits only
                age = age_text if age_text else "Age not found"
                
                results.append((first_name, last_name, age, address, phone_number))
                
            return results if results else [("No results found.", "", "", "", "")]
        else:
            return [("No profiles found.", "", "", "", "")]
    else:
        return [("Failed to retrieve information due to network or server error.", "", "", "", "")]

