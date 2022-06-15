import requests
from lxml import etree
from xml.etree import ElementTree


# 使用xpath 爬取二手房信息

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
url = 'https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1'
page_text = requests.get(url,headers=headers).text
tree = etree.HTML(page_text)
div_list = tree.xpath('//*[@id="map_block"]/div/div[4]/div[2]/div[1]/h4')




for div in div_list:
  #返回一个bytes类型的HTML文件。
  html_bytes=etree.tostring(div,encoding="utf-8")
  print(html_bytes)
  print(type(html_bytes))

  #将bytes类型转换成字符串，字符串可以用正则表达式
  #转换的过程当中会将残缺的标签自动补齐
  html_str=html_bytes.decode("utf-8")
  print(html_str)
  print(type(html_str))

