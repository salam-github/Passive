import argparse
from modules.fullname import search_full_name  # Placeholder import
from modules.ip_lookup import lookup_ip  # Placeholder import
from modules.username_check import check_social_networks
import os

def write_result(filename_prefix, data):
    """Writes data to a file, ensuring unique filenames."""
    counter = 1
    filename = f"{filename_prefix}.txt"
    while os.path.exists(filename):
        filename = f"{filename_prefix}{counter}.txt"
        counter += 1
    with open(filename, 'w') as file:
        if isinstance(data, dict):
            for network, (found, url) in data.items():
                if found == 'Yes':
                    file.write(f"{network}: Found at {url}\n")
                else:
                    file.write(f"{network}: Not Found\n")
        else:
            file.write(data)  # Handles non-dict data (for IP and fullname)
    print(f"Saved in {filename}")

def handle_fullname(fullname):
    """Handles full name search and outputs the result, including age."""
    first_name, last_name, age, address, phone_number = search_full_name(fullname)
    
    if not first_name and not last_name:  # Search failed
        print("Failed to retrieve information for the specified name.")
    else:
        result = f"First name: {first_name}\nLast name: {last_name}\nAge: {age if age else 'Age not found'}\nAddress: {address if address else 'Address not found'}\nNumber: {phone_number if phone_number else 'Phone number not found'}"
        print(result)
        write_result("result", result)
        
def handle_ip(ip):
    city, state, country, coordinates, asn_type, privacy, company = lookup_ip(ip)
    if city.startswith("Lookup failed"):
        print(city)  # Print the error message
    else:
        result = f"IPS: {company}\nCity: {city}\nState: {state}\nCountry: {country}\nCoordinates Lat/Long: {coordinates}\nASN Type: {asn_type}\nPrivacy: {privacy}"
        print(result)
        write_result("result", result)


def handle_username(username):
    """Handles username search across social networks and output."""
    results = check_social_networks(username)
    for network, (found, url) in results.items():
        # Print formatted result for each network
        if found == 'Yes':
            print(f"{network}: Found at {url}")
        else:
            print(f"{network}: Not Found")
    write_result("result", results) 


def main():
    parser = argparse.ArgumentParser(description='Welcome to passive v1.0.0')
    parser.add_argument('-fn', '--fullname', help='Search with full-name')
    parser.add_argument('-ip', help='Search with IP address')
    parser.add_argument('-u', '--username', help='Search with username')

    args = parser.parse_args()

    if args.fullname:
        handle_fullname(args.fullname)
    elif args.ip:
        handle_ip(args.ip)
    elif args.username:
        handle_username(args.username)
    else:
        print("Please provide a valid argument.")
        parser.print_help()

if __name__ == '__main__':
    main()
