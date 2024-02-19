import argparse
from modules.fullname import search_full_name  # Placeholder import
from modules.ip_lookup import lookup_ip  # Placeholder import
from modules.username_check import check_social_networks
import os

def write_result(filename_prefix, data):
    """Writes data to a file, ensuring unique filenames."""
    counter = 0
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
    """Handles full name search and output."""
    address, phone_number = search_full_name(fullname)  # Implement this function in fullname.py
    result = f"First name: {fullname.split()[0]}\nLast name: {fullname.split()[-1]}\nAddress: {address}\nNumber: {phone_number}"
    print(result)
    write_result("result", result)

def handle_ip(ip):
    isp, city, location = lookup_ip(ip)  # This now correctly handles errors
    if isp.startswith("Error"):
        print(isp)  # Prints the error message
    else:
        result = f"ISP: {isp}\nCity: {city}\nLocation (Lat/Lon): {location}"
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
