from bs4 import BeautifulSoup
import requests 
import csv
import django.utils.timezone as tz
import datetime
headers = {
                "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
            }
URL = 'https://mentalhealthmatch.com/articles/anxiety/inspiring-mental-health-quotes'
r = requests.get(URL,headers=headers) 
soup = BeautifulSoup(r.content, 'html.parser')
allNews = soup.find(class_="entry-content")
allP = allNews.find_all('ul')
print(len(allP))

date = datetime.date.today()+datetime.timedelta(days=-1)
print(date)
# for p in allP:
#     try:
#         with open('qoutes1.csv', mode='a',encoding='utf-8') as f:
#             qoutes_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             date+= datetime.timedelta(days=1)
#             if p.text!='':
#                 qoutes_writer.writerow([p.text,date])
#     except:
#         print("error")


with open('qoutes1.csv',mode='r',encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    date =str(datetime.date.today())
    print(date)
    for index,row in enumerate(csv_reader):
        # print(row)
        if row[1] == date:
            print(index,row)
        