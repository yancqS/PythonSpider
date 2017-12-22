import os
import requests
url = input("请输入一个url链接:")
root = 'D://pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
            print("files saved successfully")
        else:
            print(r.status_code)
    else:
        print('files has existed')
except:
    print('爬取失败')