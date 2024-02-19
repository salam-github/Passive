import requests

def search_full_name(fullname):
    """
    Simulate fetching address and phone number for a given full name.
    This function uses the randomuser.me API for demonstration purposes.
    """
    # Split the fullname into first and last name assuming "First Last" format
    try:
        first_name, last_name = fullname.split()
    except ValueError:
        # Handle error if fullname doesn't split into two parts
        return "Invalid full name format. Please use 'First Last' format.", ""

    # Use the randomuser.me API to fetch a random user data
    url = f"https://randomuser.me/api/?inc=location,phone&nat=us&results=1"
    response = requests.get(url)
    data = response.json()

    # Extract a random address and phone number from the response
    if data['results']:
        user = data['results'][0]
        location = user['location']
        address = f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['postcode']}"
        phone_number = user['phone']
    else:
        address = "Address not found."
        phone_number = "Phone number not found."

    return address, phone_number
