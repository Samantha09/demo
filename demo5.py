from urllib import request

url = 'http://www.renren.com/968939174'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Cookie": "anonymid=jthfi4xaizq13; depovince=GW; _r01_=1; JSESSIONID=abcsusVqBSZlN4PbNRGMw; ick_login=8593070a-66ce-4afe-8b91-1972a28bb869; _de=77D643A898E5555AC956BF95757E8671; ick=c43ccd65-2756-47e2-96a3-9c3e3ad443e3; __utma=151146938.1730582754.1553180050.1553180050.1553180050.1; __utmc=151146938; __utmz=151146938.1553180050.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=151146938.4.10.1553180050; jebecookies=665c107b-716b-41bc-84b1-6f37ca8bef47|||||; p=8778ff82e5edd014b7752f91770fe9114; ap=968939174; first_login_flag=1; ln_uact=15692036272; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=ad39c657301167f420a983b59953bcd74; societyguester=ad39c657301167f420a983b59953bcd74; id=968939174; xnsid=5f40111c; ver=7.0; loginfrom=null; jebe_key=b2c7ec45-1d4f-42c4-84dc-a68a3ebb3b56%7C45e167594daf00efc6488fe0f5b472e6%7C1553180128210%7C1%7C1553180127873; wp_fold=0"
}

req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read().decode('utf8'))

