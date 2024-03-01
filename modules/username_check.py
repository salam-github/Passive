import requests
from bs4 import BeautifulSoup  # for parsing HTML


def check_social_networks(username):
    networks = {
        'GitHub': ('https://www.github.com/{}', 'There isn’t a GitHub Pages site here.'),
        'GitLab': ('https://www.gitlab.com/{}', 'The page you are looking for does not exist.'),
        'Bitbucket': ('https://www.bitbucket.org/{}', 'The requested repository could not be found.'),
        'HackerOne': ('https://www.hackerone.com/{}', 'This page is gone'),
        'Facebook': ('https://www.facebook.com/{}', 'Sisältö ei ole käytettävissä tällä hetkellä'),  # bcs my browser is in finnish
        'reddit': ('https://www.reddit.com/user/{}', 'Sorry, nobody on Reddit goes by that name.'),
        'Twitter': ('https://twitter.com/{}', 'This account doesn’t exist'),
        'LinkedIn': ('https://www.linkedin.com/in/{}', 'This page doesn’t exist'),
        'Instagram': ('https://www.instagram.com/{}', 'Sorry, this page isn’t available.'),
        'YouTube': ('https://www.youtube.com/{}', 'This channel does not exist.'),
        'Pinterest': ('https://www.pinterest.com/{}', 'Sorry! We couldn’t find that page.'),
        'SoundCloud': ('https://www.soundcloud.com/{}', 'Oops! We can’t find that SoundCloud user.'),
        'Snapchat': ('https://www.snapchat.com/add/{}', 'Sorry, This content was not found.'),
        'TikTok': ('https://www.tiktok.com/@{}', "Couldn't find this account"),
        'Steam': ('https://www.steamcommunity.com/id/{}', 'The specified profile could not be found.'),
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)' #user agent to fool the servers(mainly twitter and instagram)
    }

    results = {}
    for network, (url_template, not_found_text) in networks.items():
        url = url_template.format(username)
        try:
            # Specify a timeout for the request (e.g., 2 seconds for now)
            response = requests.get(url, headers=headers, timeout=2)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                page_text = soup.get_text().lower()
                if not_found_text.lower() in page_text:
                    results[network] = ('No', '')
                else:
                    results[network] = ('Yes', url)
            else:
                results[network] = ('No', '')
        except requests.exceptions.Timeout:
            print(f"Request to {network} timed out.")
            results[network] = ('Timeout', '')
        except requests.exceptions.RequestException as e:
            print(f"Error checking {network}: {e}")
            results[network] = ('Error', '')

    return results


