from urllib import request, parse


url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&gm=15-50%E4%BA%BA&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Referer": "https://www.lagou.com/jobs/list_Python?px=default&gm=15-50%E4%BA%BA&city=%E5%B9%BF%E5%B7%9E",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",

}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}


req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf8'))  # 报错：请求太频繁