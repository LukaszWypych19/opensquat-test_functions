"""
A function named "save_screenshot" captures the screenshot
taken by the "url2png" function and saves it under the name
"{domain_name}+{date}+{time}" in the "screenshots" directory.
"""

import datetime
import os
import hashlib
import urllib.parse
import requests


# Type your domain name here
url = 'google.com'


def save_screenshot(url2png_func):

    # Get the content of screenshot
    url_screenshot = url2png_func(url, apikey, secret)
    get_screenshot = requests.get(url_screenshot).content

    # Saving a file under a specific name
    try:
        current_date_and_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        dir_path = "D:\\Python\\Moje projekty\\opensquat\\url2png\\"
        file_name = f"{url}_{current_date_and_time}.png"
        full_file_path = os.path.join(dir_path, file_name)

        with open(full_file_path, 'wb') as file:
            file.write(get_screenshot)
            return True
    except Exception as e:
        return str(e)


def url2png(url, apikey, secret, fullpage=None, max_width=None,
            unique=None, viewport_width=1024, viewport_height=800):

    data = {
      'url': url,
      'fullpage': 'true' if fullpage else 'false',
      'thumbnail_max_width': max_width,
      'unique': unique,
      'viewport': '{}x{}'.format(viewport_width, viewport_height),
    }
    filtered_data = dict((opt, data[opt]) for opt in data if data[opt])

    query_string = urllib.parse.urlencode(filtered_data)

    token = hashlib.md5('{}{}'.format(query_string, secret).encode('utf-8')).hexdigest()
    return "http://api.url2png.com/v6/{}/{}/png/?{}".format(apikey, token, query_string)


apikey = "P8D9EB90ADA83E3"
secret = "S_4F5D3BCF2AF68"
print(url2png(url, apikey, secret))


result = save_screenshot(url2png)
if result is True:
    print("The function was executed successfully.")
else:
    print(f"There was an error: {result}")
