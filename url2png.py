"""
A class named "URLScreenshot" captures the screenshot of url
(url2png function) and saves it under the name "{domain_name}+{date}+{time}"
in the "screenshots" directory (save_screenshot function).
"""

import datetime
import os
import hashlib
import urllib.parse
import requests


class URLScreenshot:
    def __init__(self):
        self.url = "google.com"
        self.apikey = "P8D9EB90ADA83E3"
        self.secret = "S_4F5D3BCF2AF68"

    def save_screenshot(self):
        # Get the content of screenshot
        url_screenshot = self.url2png()
        get_screenshot = requests.get(url_screenshot).content

        # Saving a file under a specific name
        try:
            current_date_and_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
            dir_path = "D:\\Python\\Moje projekty\\opensquat\\url2png\\"
            file_name = f"{self.url}_{current_date_and_time}.png"
            full_file_path = os.path.join(dir_path, file_name)

            with open(full_file_path, 'wb') as file:
                file.write(get_screenshot)
                return True
        except Exception as e:
            return str(e)

    def url2png(self,
                fullpage=None,
                max_width=None,
                unique=None,
                viewport_width=1024,
                viewport_height=800):

        data = {
          'url': self.url,
          'fullpage': 'true' if fullpage else 'false',
          'thumbnail_max_width': max_width,
          'unique': unique,
          'viewport': '{}x{}'.format(viewport_width, viewport_height),
        }
        filtered_data = dict((opt, data[opt]) for opt in data if data[opt])

        query_string = urllib.parse.urlencode(filtered_data)

        token = hashlib.md5('{}{}'.format(query_string, self.secret).encode('utf-8')).hexdigest()
        return "http://api.url2png.com/v6/{}/{}/png/?{}".format(self.apikey, token, query_string)


def main():
    screenshot = URLScreenshot()
    result = screenshot.save_screenshot()

    if result is True:
        print("The function was executed successfully.")
    else:
        print(f"There was an error: {result}")


if __name__ == "__main__":
    main()
