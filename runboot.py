import sys

import requests
from bs4 import  BeautifulSoup as bs
import  time
import  pymysql # 报错时,点击"install..."自动下载

# BeautifulSoup解析

# 1 发送请求
url = "https://www.runoob.com/python/python-100-examples.html"
headersr= {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
response = requests.get(url,headersr).text
# 2 解析结果
example_html = bs(response,"lxml")
# 3.获取二级请求标签
a_html_list = example_html.find(id="content").find_all("a")
##print(response)
print(a_html_list) # a标签
print(len(a_html_list))
# attrs 指定属性名,其实是一个字典
print(a_html_list[0].attrs["href"])
print("*"*30)
#  for 循环
# list = []
# for i in a_html_list :
# #
# # #########    print(a_html_list[i].attrs["href"])
# #     #
#    list.append("https://www.runoob.com"+i.attrs["href"])
# print(list)
print("$"*30)
# https://www.runoob.com
# 列表推导式
a_url_list = ["https://www.runoob.com"+i.attrs["href"] for i in a_html_list]
print(a_url_list)

# 7. 获取数据库连接,游标
try:
    db = pymysql.connect("localhost","root","root","pydb")
    print("数据库连接成功")
except Exception as e:
    print(e)
    print("数据库连接失败")
    sys.exit(1)
cursor = db.cursor()


for url in a_url_list[2:4]:
    #i_response = requests.get(a_url_list[i],headersr).text
    #print(bs(i_response, "lxml"))


# 4 请求二级页面
    a_response = requests.get(url,headersr).text
#print(a_response)
# 5 解析二级页面
    info_html = bs(a_response,"lxml")
#print(info_html)
# 6. 获取目标数据
    info_content = info_html.find(id="content")
    title = info_content.find("h1").text
        #info_content.h1,text
   # print(title,end="---")
    question1 = info_content.find_all("p")[1].text
   # print(question1)
    # 8. 插入数据库
    sql = "insert into pyquestion values (NULL,'%s','%s')"%(title,question1)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("%s:插入成功"%title)
        # 若插入数据库数据乱码 可执行 set names gbk;
    except Exception as e:
        print(e)
        print("%s:插入失败"%title)
        db.rollback()


    time.sleep(1)
    # 关闭数据连接
db.close()
"""
F12--network--python-100-examples--
request-header:
  cookies
  user-agent:
  Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36



 1,必须遵守Robots协议
  2.放慢速度
 3.不突破反爬
  4.对于爬虫项目或者爬虫任务要认真评估风险
  https://www.runoob.com/robots.txt
  --基本流程
1.发送请求
2.获取内容
3.解析数据
4.保存数据 
--基础知识
java:jsoup/WebMagic/Nutch
scrapy/Splash
 
User-agent: *

Disallow: /wp-admin/
Disallow: /feed/
Disallow: /*/feed/
Disallow: /trackback/
Disallow: /*/trackback/
Disallow: /page/
Disallow: /try/
Disallow: /wp-*.php
Disallow: /wp-includes/
Disallow: /?s=*

"""
