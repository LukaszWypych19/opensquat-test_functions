import datetime
import os
# import hashlib
# import urllib.parse

# url = 'google.com'

# apikey, secret


def save_screenshot(url='google.com'):
    try:
        current_date_and_time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        dir_path = "D:\\Python\\Moje projekty\\opensquat\\url2png\\"
        file_name = f"{url}_{current_date_and_time}.png"
        full_file_path = os.path.join(dir_path, file_name)

        with open(full_file_path, 'x'):
            return True
    except Exception as e:
        return str(e)


result = save_screenshot()
if result == True:
    print("The function was executed successfully.")
else:
    print(f"There was an error: {result}")


"""
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


apikey = "PXXXX"
secret = "SXXXX"

print(url2png("http://google.com/", apikey, secret))


"""