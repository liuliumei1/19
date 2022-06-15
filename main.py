import re
import urllib.request


from lxml import etree
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
# url，网址
url = 'http://www.hkwb.net/node_32247.html'
# 通过request类来构造请求
res = urllib.request.Request(url,headers=headers)
# 通过urlopen方法访问页面并返回 HTTPResposne 对象
response = urllib.request.urlopen(res)
# 通过read()方法读取字节流并解码成字符串
html = response.read().decode('utf-8')
pattren1=re.compile(r'(?:<.+font-size:16px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#900;">)(.+)(?:</div>)')
confirmedCount=re.findall(pattren1,html)[0]
pattren2=re.compile(r'(?:<.+font-size:12px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#900;">)(.+)(?:</div>)')
confirmedCountIntr=re.findall(pattren2,html)[0]
pattren3=re.compile(r'(?:<.+font-size:16px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#C63;">)(.+)(?:</div>)')
curedCount=re.findall(pattren3,html)[0]
pattren4=re.compile(r'(?:<.+font-size:12px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#c63;">)(.+)(?:</div>)')
curedIncr=re.findall(pattren4,html)[0]
pattren5=re.compile(r'(?:<.+font-size:16px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#093;">)(.+)(?:</div>)')
pattren6=re.compile(r'(?:<.+font-size:12px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#093;">)(.+)(?:</div>)')
deadCount=re.findall(pattren5,html)[0]
deadIncr=re.findall(pattren6,html)[0]
pattren7=re.compile(r'(?:<.+font-size:13px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#333;">)(.+)(?:</div>)')
outsideInputCount=re.findall(pattren7,html)[0]
pattren8=re.compile(r'(?:<.+font-size:12px; height:30px; line-height:30px; tex'
                    r't-align:center; font-weight:bold; color:#333;">)(.+)(?:</div>)')
outsideInputIncr=re.findall(pattren8,html)[0]

asymptomaticInfectionCount=re.findall(pattren7,html)[1]
asymptomaticInfectionIncr=re.findall(pattren8,html)[1]

data={}
data["confirmedCountIntr"]=confirmedCountIntr
data["confirmedCount"]=confirmedCount
data["deadIncr"]=deadIncr
data["deadCount"]=deadCount
data["outsideInputCount"]=outsideInputCount
data["outsideInputIncr"]=outsideInputIncr
data["asymptomaticInfectionIncr"]=asymptomaticInfectionIncr
data["asymptomaticInfectionCount"]=asymptomaticInfectionCount
data["curedCount"]=curedCount
data["curedIncr"]=curedIncr

chinese=[]
chinese.append(data)
print(chinese)