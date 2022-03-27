import requests
from bs4 import BeautifulSoup
from notebook import extract_info
import csv

file = open('thursdaywebtoon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "author", "rating"])

webtoon_url = f'https://comic.naver.com/webtoon/weekdayList?week=thu'
webtoon_html = requests.get(webtoon_url)

webtoon_SOUP = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_SOUP.find("ul",{"class": "img_list"})
webtoon_list = webtoon_list_box.find_all("li")
print (webtoon_list)

final_result=[]
final_result += extract_info(webtoon_list)

for result in final_result :
        row=[]
        row.append(result['title'])
        row.append(result['author'])
        row.append(result['rating'])
        writer.writerow(row)