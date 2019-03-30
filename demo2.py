from urllib import parse

url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'

result = parse.urlparse(url)
result1 = parse.urlsplit(url)
print(result)
print(result1)  # params