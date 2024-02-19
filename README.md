# Passive Information Gathering Tool

## Description

Passive is a tool designed for cybersecurity professionals and enthusiasts to perform passive information gathering. It allows users to query full names, IP addresses, and social media usernames to gather relevant information without actively engaging with the target systems or networks.

## Features

- Full Name Search: Look up addresses and phone numbers associated with a given full name.
- IP Lookup: Retrieve city, ISP, and other geolocation information for a given IP address.
- Username Check: Check the presence of a given username across multiple social networks.

## Installation

### Prerequisites

- Python3
- Requests
- BeautifulSoup4 (for HTML parsing)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/salam-github/Passive
   ```
2. Navigate to the project directory:
   ```sh
   cd passive
   ```
3. Install the required Python packages:
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage

To use Passive, run the following commands in your terminal:

- Full Name Search:
  ```sh
  ./passive -fn "John Doe"
  ```
- IP Lookup:
  ```sh
  ./passive -ip 123.45.67.89
  ```
- Username Check:
  ```sh
  ./passive -u "username123"
  ```

### Compiling to an Executable

To compile Passive into an executable, ensure you have PyInstaller installed and run:

```sh
pyinstaller --onefile --name passive main.py
```

The executable will be located in the `dist` directory.

## Contributing

We welcome contributions to Passive! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

## License

[MIT License](LICENSE)

## Disclaimer

Passive is intended for educational and ethical use only. Users are responsible for adhering to applicable laws and regulations. The developers assume no liability for misuse of this tool.