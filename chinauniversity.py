import requests
from bs4 import BeautifulSoup
import bs4
print("<========================生源质量排名========================>")
num = int(input('查看大学排名:'))


def gethtmltext(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Error'


def fillunivlist(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printunivlist(ulist, num):
    print('{0:^10}\t{1:{4}^8}\t{2:^20}\t{3:^5}'.format('排名','学校名称','地址','分数',chr(12288)))  # chr(12288)是中文空格
    for i in range(num):
        u = ulist[i]
        print('{0:^10}\t{1:{4}^8}\t{2:^20}\t{3:^5}'.format(u[0], u[1], u[2], u[3],chr(12288)))


def main(num):
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2019.html'
    html = gethtmltext(url)
    fillunivlist(uinfo, html)
    printunivlist(uinfo, num)


main(num)