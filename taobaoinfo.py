# 淘宝搜索接口:https://s.taobao.com/search?q=
import requests
import re
import io
goods = input('输入你想要的商品:')
num = int(input('输入搜索范围:'))


def gethtmltext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parserpage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        title = re.findall(r'\"raw_title\"\:\".*?\"',html)  # 第一次爬取得范围过小是因为 正则表达式:[\u4e000-\u9fa5]+(匹配汉字)
        loc = re.findall(r'\"item_loc\"\:\".*?\"',html)
        for i in range(len(plt)):
            plts = re.split(r'\"view_price\"\:', plt[i])[1]
            titles = re.split(r'\"raw_title\"\:', title[i])[1]
            locs = re.split(r'\"item_loc\"\:', loc[i])[1]
            ilt.append([plts, titles, locs])
    except:
        return ''


def printgoodslist(ilr):
    f = io.open('D://pics//info.txt', 'a', encoding='utf-8')
    f.write('<----------------------------------------------Information---------------------------------------------->')
    f.write('{0:{2}^30}\t\t{1:{2}^3}\t{3:{2}^20}\n'.format('标题', '价格', chr(12288), '地址'))
    for i in range(len(ilr)):
        f.write('{0:{2}^30}\t\t{1:{2}^3}\t{3:{2}^12}\n'.format(ilr[i][1], ilr[i][0], chr(12288), ilr[i][2]))
    f.close()
    print('success write in files')


def main(goods, num):
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(num):
        try:
            url = start_url + '&s=' + str(44*i)
            html = gethtmltext(url)
            parserpage(infolist, html)
        except:
            continue
    printgoodslist(infolist)


main(goods, num)