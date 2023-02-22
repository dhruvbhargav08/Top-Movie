from bs4 import BeautifulSoup
import requests
response=requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup=BeautifulSoup(response.text,'html.parser')
name=soup.find_all(name='h3' ,class_='title')
with open('movie.txt','w',encoding='utf8') as file :
    for i in range(len(name)-1,-1,-1):
        file.write(f"{name[i].text}\n")
