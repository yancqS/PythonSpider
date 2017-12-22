# -*- coding: utf-8 -*-
import scrapy
import re
import random


class StockSpider(scrapy.Spider):
    name = 'stock'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']
    # 百度股票的反爬虫技术:是检测User-Agent,如果单纯的修改user-agentd,还是返回403，但是手动请求是可以链接的。
    # 可以通过构造不同的请求头部信息，来规避这种反爬虫技术。
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" 
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    def parse(self, response):
        ua = random.choice(self.user_agent_list)  # 随机抽取User-Agent
        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Referer': 'https://gupiao.baidu.com/',
            'User-Agent': ua
        }  # 构造请求头
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\d{6}', href)[0]
                url = 'http://www.gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock, headers=headers)
            except:
                continue

    @staticmethod
    def parse_stock(response):
        infodict = {}
        stockinfo = response.css('.stock-bets')
        name = stockinfo.css('.bets-name').extract()[0]
        keylist = stockinfo.css('dt').extract()
        valuelist = stockinfo.css('dd').extract()
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>', keylist[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>', valuelist[i])[0][0:-5]
            except:
                val = '--'
            infodict[key] = val
        infodict.update(
            {'股票名称': re.findall('\s.*\(', name)[0].split()[0] + re.findall('\>.*\<', name)[0][1:-1]}
        )
        yield infodict