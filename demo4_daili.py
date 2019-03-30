from urllib import request


url = 'http://httpbin.org/ip'

# 没有使用代理
resp = request.urlopen(url)
print(resp.read())

# 使用代理
# 1.使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({"http": "1.197.204.220:9999"})
# 2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener发送一个请求
resp = opener.open(url)
print(resp.read())
