import argparse
from modules.fullname import search_full_name 
from modules.ip_lookup import lookup_ip 
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
    results = search_full_name(fullname)
    all_results = ""  # Initialize an empty string to accumulate all results

    if results:
        for result in results:
            first_name, last_name, age, address, phone_number = result
            if first_name == "No results found." or first_name == "Failed to retrieve information due to network or server error.":
                print(first_name)  # Print the error or no results message
                break
            else:
                result_str = f"First name: {first_name}\nLast name: {last_name}\nAge: {age}\nAddress: {address}\nNumber: {phone_number}\n\n"
                all_results += result_str  # Accumulate all results into one string
        
        if all_results:
            print(all_results)  # Print all accumulated results
            write_result("result", all_results)  # Write all accumulated results to file
    else:
        print("Failed to retrieve information for the specified name.")
        
def handle_ip(ip):
    try:
        # Attempt to unpack the returned values from lookup_ip
        city, state, country, coordinates, asn_type, privacy, company = lookup_ip(ip)
        # If successful, proceed to print or use the extracted values
        result = f"City: {city}\nState: {state}\nCountry: {country}\nCoordinates: {coordinates}\nASN Type: {asn_type}\nPrivacy: {privacy}\nCompany: {company}"
        print(result)
        write_result("result", result)
    except ValueError as e:
        # Handle the case where unpacking fails due to an unexpected number of values, eg. error page
        print("An error occurred while processing the IP address. Please ensure it is valid and try again.")



def handle_username(username):
    print(f"Searching for {username} please wait...")
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

    parser.add_argument('-fn', '--fullname', metavar='', help='Perform a search using a full name (e.g., "John Doe") and retrieve relevant information.')
    parser.add_argument('-ip', metavar='', help='Perform a search using an IP address to retrieve geolocation information, including city, ISP, and other details.')
    parser.add_argument('-u', '--username', metavar='', help='Check the presence of a username across multiple social networks.')

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
