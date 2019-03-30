"""
保存cookies到本地
加载本地cookie
"""

from urllib import request
from http.cookiejar import MozillaCookieJar

# 创建一个cookiejar对象
cookiejar = MozillaCookieJar('cookies.txt')
cookiejar.load(ignore_discard=True)
# 1.2 使用COOKIEJAR创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)

# 1.3 使用上一步骤创建的handler创建一个opener
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies')

for cookie in cookiejar:
    print(cookie)

# 将cookies保存到本地
# cookiejar.save(ignore_discard=True)

#



