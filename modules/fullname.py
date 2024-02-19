import requests
from bs4 import BeautifulSoup  # for parsing HTML

def search_full_name(fullname):
    """
    Fetch details for a given full name from a hypothetical or real web page.
    This function is structured to parse and return specific pieces of information.
    """
    # Placeholder for the URL, adjust as necessary
    url = f"https://www.eniro.se/{fullname.replace(' ', '+''')}/personer"
    print(url)
    response = requests.get(url)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        name_container = soup.find("h2", text=lambda text: fullname in text)
        if name_container:
            # Assuming the age is in a <p> immediately following the <h2> or within a close parent/child structure
            age_container = name_container.find_next_sibling("p", class_="text-base font-normal text-gray-600")
            age_text = age_container.get_text(strip=True) if age_container else "Age not found"
            # Extract the numeric part for the age, assuming the age is followed by "år"
            age = ' '.join(filter(str.isdigit, age_text))
        else:
            age = "Age not found"
        
        # Extract address
        address_container = soup.find("span", class_="flex flex-wrap")
        address = ' '.join(part.get_text(strip=True) for part in address_container.find_all("p")) if address_container else "Address not found"
        
        # Extract phone number
        phone_link = soup.find("a", href=lambda href: href and "tel:" in href)
        phone = phone_link.get_text(strip=True) if phone_link else "Phone number not found"
        
        return fullname.split()[0], fullname.split()[-1], age, address, phone
    else:
        return None, None, "Failed to retrieve information", "", ""

    return address, phone_number


# https://www.eniro.se/FULLNAME/personer