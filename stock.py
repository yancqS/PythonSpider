import requests
import re
from bs4 import BeautifulSoup
import io


def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getstocklist(lst, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        listinfo = soup.find_all(id='quotesearch')
        soupinfo = BeautifulSoup(str(listinfo), 'html.parser')
        listshsz = soupinfo.find_all('ul')
        listsh = listshsz[0]
        soupsh = BeautifulSoup(str(listsh), 'html.parser')
        sh = soupsh.find_all('li')
        listsz = listshsz[1]
        soupsz = BeautifulSoup(str(listsz), 'html.parser')
        sz = soupsz.find_all('li')
        for i in range(len(sh)):
            contentsh = sh[i].string
            token = re.search(r'\d{6}', contentsh).group(0)
            lst.append(token)
        for n in range(len(sz)):
            contentsz = sz[n].string
            token = re.search(r'\d{6}', contentsz).group(0)
            lst.append(token)
        return [len(sh), len(sz)]
    except:
        return ""


def getstockinfo(lst, stockurl, fpath, lenarr):
    f = io.open(fpath, 'a', encoding='utf-8')
    f.write('<================沪市股票:================>\n')
    f.write('{0:^8}\t\t{1:^8}\t\t{2:^6}\n'.format('股票名称', '股票代码', '股票价格'))
    shlen = lenarr[0]
    szlen = lenarr[1]
    countsh = 0
    countsz = 0
    for i in range(shlen):
        try:
            url = stockurl + 'sh' + str(lst[i]) + '.html'
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            name = soup.find_all(class_='bets-name')[0]
            price = soup.find_all(class_='_close')[0].string
            realname = name.text.split()[0]
            f.write('{0:^8}\t\t{1:^8}\t\t{2:^6}\n'.format(realname, str(lst[i]), price))
            countsh = countsh + 1
            print('\r沪市股票进度:{0:.2f}%'.format((countsh*100) / shlen), end='')
        except:
            countsh = countsh + 1
            print('\r沪市股票进度:{0:.2f}%'.format((countsh * 100) / shlen), end='')
            continue
    f.write('<================深市股票:================>\n')
    for n in range(shlen, len(lst)):
        try:
            print(n)
            url = stockurl + 'sz' + str(lst[n]) + '.html'
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            name = soup.find_all(class_='bets-name')[0]
            price = soup.find_all(class_='_close')[0].string
            realname = name.text.split()[0]
            f.write('{0:^8}\t\t{1:^8}\t\t{2:^6}\n'.format(realname, str(lst[n]), price))
            countsz = countsz + 1
            print('\r深市股票进度:{0:.2f}%'.format((countsz * 100) / szlen), end='')
        except:
            countsz = countsz + 1
            print('\r深市股票进度:{0:.2f}%'.format((countsz * 100) / szlen), end='')
            continue
    f.close()
    print('success write in files')


def main():
    stock_list_info = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://pics//StockInfo.txt'
    slist = []
    html = gethtmltext(stock_list_info)
    lenarr = getstocklist(slist, html)
    getstockinfo(slist, stock_info_url, output_file, lenarr)


main()