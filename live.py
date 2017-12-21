import requests
import json
import time
import pymysql

#create an mysql connection
conn = pymysql.connect(host='localhost',port=3307,user='root',password='usbw',db='zhihu',charset='utf8')
#create an 游标 cursor
cursor = conn.cursor()

Cookie=''''''    #write your own Cookie
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Cookie": Cookie
        }
html = requests.get("https://api.zhihu.com/lives/homefeed?limit=200&offset=0&includes=live",headers=header)
html = json.loads(html.text)["data"]
num = len(html)#live数量
count = 0
for i in range(num):
        count += 1
        #live名,主讲人,评分，感兴趣的人,参与的人,描述,评价人数，价格,开始时间
        live_name = html[i]["live"]["subject"]
        people_name = html[i]["live"]["speaker"]["member"]["name"]
        score = html[i]["live"]["review"]["score"]
        liked_num = html[i]["live"]["liked_num"]
        taken_num = html[i]["live"]["seats"]["taken"]
        description = html[i]["live"]["speaker"]["description"]
        score_people_num = html[i]["live"]["review"]["count"]
        price = html[i]["live"]["fee"]["original_price"]
        start_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(str(html[i]["live"]["starts_at"])[:10])))
        alldatadict = {"live":live_name,"主讲人":people_name,"评分":score,"评分人数":score_people_num,"感兴趣的人数":liked_num,"参与的人":taken_num,"价格":price,"开始时间":start_time,"描述":description}
        print(count,alldatadict)
        #插入多行数据
        cursor.execute("INSERT INTO live(live_name,people_name,score,score_people_num,liked_num,taken_num,price,start_time,description)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}');".format(live_name,people_name,score,score_people_num,liked_num,taken_num,price,start_time,description))
        #提交执行
        conn.commit()
#关闭连接
cursor.close()
conn.close()
print("All is OK!")
