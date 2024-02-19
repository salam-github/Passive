import requests
from bs4 import BeautifulSoup  # for parsing HTML

    
def check_social_networks(username):
    networks = {
        'Facebook': ('https://www.facebook.com/{}', 'Sisältö ei ole käytettävissä tällä hetkellä'),  # Example text
        'reddit': ('https://www.reddit.com/user/{}', 'Sorry, nobody on Reddit goes by that name.'),
        'Twitter': ('https://www.twitter.com/{}', 'This account doesn’t exist'),
        'LinkedIn': ('https://www.linkedin.com/in/{}', 'This page doesn’t exist'),
        'Instagram': ('https://www.instagram.com/{}', 'Sorry, this page isn’t available.'),
        'Pinterest': ('https://www.pinterest.com/{}', 'Sorry! We couldn’t find that page.'),
        'GitHub': ('https://www.github.com/{}', 'There isn’t a GitHub Pages site here.'),
        'SoundCloud': ('https://www.soundcloud.com/{}', 'Oops! We can’t find that SoundCloud user.'),
        'Snapchat': ('https://www.snapchat.com/add/{}', 'Sorry! This user has not added any Snaps to their Story yet.'),
        'TikTok': ('https://www.tiktok.com/@{}', 'Sorry, this page isn’t available.'),
        'Steam': ('https://www.steamcommunity.com/id/{}', 'The specified profile could not be found.'),
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    results = {}
    for network, (url_template, not_found_text) in networks.items():
        url = url_template.format(username)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Parse the HTML response and search for not_found_text
                soup = BeautifulSoup(response.text, 'html.parser')
                page_text = soup.get_text().lower()  # Get all text from the page and make it lowercase for case-insensitive search
                if not_found_text.lower() in page_text:
                    results[network] = ('No', '')
                else:
                    results[network] = ('Yes', url)
            else:
                results[network] = ('No', '')
        except requests.exceptions.RequestException as e:
            print(f"Error checking {network}: {e}")
            results[network] = ('Error', '')

    return results