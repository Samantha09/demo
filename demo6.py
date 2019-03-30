"""
爬虫自动登录访问授权界面

"""

from urllib import request, parse
from http.cookiejar import CookieJar


# 1.1 创建一个CookieJar对象
cookiejar = CookieJar()

# 1.2 使用COOKIEJAR创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)

# 1.3 使用上一步骤创建的handler创建一个opener
opener = request.build_opener(handler)

# 1.4 使用opener发送登录请求（账号和密码）
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
}

data = {
    "email": '15692036272',
    "password": "951218/lucky",

}

login_url = "http://www.renren.com/ajaxLogin/login"
req = request.Request(login_url, headers=headers, data=parse.urlencode(data).encode('utf8'))
resp = request.urlopen(req)
print(resp.read().decode('utf8'))
opener.open(req)

# 访问主页
san_url = "http://www.renren.com/968939174/profile"
# 使用之前的opener登录，因为之前的opener已经包含了cookies信息
resp = opener.open(san_url)
with open('renren.html', 'w', encoding='utf8') as f:
    f.write(resp.read().decode('utf8'))


