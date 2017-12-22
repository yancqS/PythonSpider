import requests


def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'https://item.jd.com/5352358.html'
    print(gethtmltext(url))