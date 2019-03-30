"""
requests库
"""

import requests

# response = requests.get("http://www.baidu.com/")
# print(type(response.text))
# print(response.text)
# print(type(response.content))
# print(response.content.decode('utf-8'))

# data = {
#     'first': 'true',
#     'pn': '1',
#     'kd': 'python'
# }
#
# headers = {
#     "Referer": "https://www.lagou.com/zhaopin/Java/?labelWords=label",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# }

# 发送post请求
# response = requests.post("https://www.lagou.com/jobs/list_python?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput=", data=data, headers=headers)
# print(response.text)
#
# # 使用代理
# proxy = {
#     'http': '111.177.170.148: 9999'
# }
#
# response = requests.get("http://httpbin.org.ip", proxies= proxy)
# print(response.text)

# 处理cookie信息
# response = requests.get("http://www.baidu.com/")
# print(response.cookies.get_dict())

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

data = {
    "email": '15692036272',
    "password": "951218/lucky",

}

login_url = "http://www.renren.com/ajaxLogin/login"
san_url = "http://www.renren.com/968939174/profile"

def session():
    session = requests.Session()
    session.post(login_url, data=data, headers=headers)

    resp = session.get(san_url)
    with open('renren1.html', 'w') as f:
        f.write(resp.content.decode('utf8'))

if __name__ == '__main__':
    session()