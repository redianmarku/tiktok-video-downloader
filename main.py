from bs4 import BeautifulSoup
import requests
import urllib.request


url_video='https://www.tiktok.com/@_vip.meme.al_/video/7100127466974481669'
#open and read page
page=urllib.request.urlopen(url_video)
html=page.read()
#create BeautifulSoup parse-able "soup"
print(html)
soup = BeautifulSoup(html, "html.parser")

lst_url_video=[]
print(soup.body)


# headers = {
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
# }
# here = requests.get("https://www.tiktok.com/@_vip.meme.al_/video/7100127466974481669", headers=headers)


# # soup = BeautifulSoup(here.text, 'html.parser')


# with open("file.txt", "w",  encoding="utf-8") as f:
#     f.write(str(here.text))




