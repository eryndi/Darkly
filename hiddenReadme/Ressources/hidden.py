# !~/usr/local/bin/python3.7

import io
import requests


def has_numbers(string):
    return any(char.isdigit() for char in string)


def get_list(r):
    urls = []
    buf = io.StringIO(r.text)
    while True:
        line = buf.readline()
        if "href" in line:
            urls.append(line[9:36])
        if not line:
            break;
    urls = urls[1:-1]
    return urls


def recursion(urls, url):
    readme = "{}{}".format(url, "README")
    response = requests.get(readme)
    if has_numbers(response.text):
        print("I found a flag", response.text, "here:", readme)
        return
    else:
        for each in urls:
            new_url = "{}{}".format(url, each)
            new_r = requests.get(new_url)
            new_urls = get_list(new_r)
            if not new_urls:
                readme = "{}{}".format(new_url, "README")
                response = requests.get(readme)
                if has_numbers(response.text):
                    print("I found a flag", response.text, "here:", new_url)
                    return
                else:
                    continue
            else:
                recursion(new_urls, new_url)


def hidden():


#   url = "http://10.12.1.111/.hidden/"
    url = "http://10.11.200.225/.hidden/"
    try:
        r = requests.get(url)
    except TimeoutError:
        print("Website is not online")
        exit(1)
    except Exception as error:
        print("Something is wrong ¯\_(ツ)_/¯ most probably this:\n", error)
        exit(1)
    if r.status_code != 200:
        print("Website is not working properly")
        exit(1)

    urls = get_list(r)
    recursion(urls, url)


if __name__ == "__main__":
    hidden()
