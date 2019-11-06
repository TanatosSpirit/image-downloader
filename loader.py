# from html.parser import HTMLParser
# from urllib.request import urlopen
#
# class MyHTMLParser(HTMLParser):
#     def __init__(self, site_name, *args, **kwargs):
#         # список ссылок
#         self.links = []
#         # имя сайта
#         self.site_name = site_name
#         # вызываем __init__ родителя
#         super().__init__(*args, **kwargs)
#         # при инициализации "скармливаем" парсеру содержимое страницы
#         self.feed(self.read_site_content())
#         # записываем список ссылок в файл
#         self.write_to_file()
#
#     def handle_starttag(self, tag, attrs):
#         # проверяем является ли тэг тэгом ссылки
#         if tag == 'div':
#         # if tag == 'a':
#             # находим аттрибут адреса ссылки
#             for attr in attrs:
#                 print(attr)
#                 if attr[0] == 'href':
#                     # проверяем эту ссылку методом validate() (мы его еще напишем)
#                     if not self.validate(attr[0]):
#                         # вставляем адрес в список ссылок
#                         self.links.append(attr[1])
#
#     def validate(self, link):
#         """ Функция проверяет стоит ли добавлять ссылку в список адресов.
#         В список адресов стоит добавлять если ссылка:
#              1) Еще не в списке ссылок
#              2) Не вызывает javascript-код
#              3) Не ведет к какой-либо метке. (Не содержит #)
#          """
#         return link in self.links or '#' in link or 'javascript:' in link
#
#     def read_site_content(self):
#         return str(urlopen(self.site_name).read())
#
#
#     def write_to_file(self):
#         # открываем файл
#         f = open('links.txt', 'w')
#         # записываем отсортированный список ссылок, каждая с новой строки
#         f.write('\n'.join(sorted(self.links)))
#         # закрываем файл
#         f.close()
#
#
#
# parser = MyHTMLParser("http://vma.muar.ru/ru/subjects/dvorec-truda-konkursnyy-proekt-perspektiva-1922-1")












import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('E:\chromedriver_win32\chromedriver')

browser.get('http://vma.muar.ru/ru/subjects/dvorec-truda-konkursnyy-proekt-perspektiva-1922-1')

import time
time.sleep(5)


data = BeautifulSoup(browser.page_source, "html.parser")
print(data)

head = data.contents[0].contents[0]

body = head.nextSibling





divTag = data.find_all("div", {"class": "leaflet-tile-container leaflet-zoom-animated"})
print(divTag[0])
for tag in divTag:
    tdTags = tag.find_all("img", {"class": "leaflet-tile leaflet-tile-loaded"})
    for tag in tdTags:
        print(tag)



# #All the Src
# for src in data.find_all('img'):
#     print(src['src'])
imgs = data.find_all('img')
some = data.find('img', class_="leaflet-tile leaflet-tile-loaded")
# some = data.find('div', class_="leaflet-tile-container leaflet-zoom-animated")

print(some)

for child in data.find('div', class_='leaflet-tile-container leaflet-zoom-animated').children:
    print(child)




#
# url = 'http://vma.muar.ru/ru/subjects/dvorec-truda-konkursnyy-proekt-perspektiva-1922-1'
# url = urllib.request.urlopen(url)
#
#
# page = BeautifulSoup(url, 'lxml')
# print(page.findAll('img'))
# #
#

# from bs4 import BeautifulSoup
# import urllib.request
#
#
# html = '<td valign="top">.....</td>\
#         <td width="580" valign="top">.......</td>\
#         <td>.....</td>'
#
# url = 'http://vma.muar.ru/ru/subjects/dvorec-truda-konkursnyy-proekt-perspektiva-1922-1'
# url = urllib.request.urlopen(url)
# #
# soup = BeautifulSoup(url, "lxml")

# ind_per = soup.find("div",{"div",{"class" : "sub_header_block"}})
# print(soup.find_all('img'))
#
# img = soup.find('img')
# # print(img)
#
# with urllib.request.urlopen('http://vma.muar.ru/ru/subjects/dvorec-truda-konkursnyy-proekt-perspektiva-1922-1') as f:
#   soup = BeautifulSoup(f.read(), 'lxml')
# for image in soup.select(".leaflet-layer"):
#   print(image.img["src"])
#
# # text = soup.findAll('div', class_='content_block')
# # print(text)
# # soup = BeautifulSoup(html, 'html.parser').find('div', class_='menu_navigate_block')
# # for i in soup.find_all('a', href=True):
# #     print(i['href'])
#
#
#
# # list1 = soup.find_all('div', class_ = 'leaflet-tile-container leaflet-zoom-animated')
# # print(list1)
# # list1 = soup.find_all('div', class_ = 'leaflet-tile-container leaflet-zoom-animated')
# # print(list1)
# # img = soup.find("div", {"id": "subject_view"}).find("img")
# #
# # heading = soup.find(id='subject_view')
# # image = heading.find("src")
#
# # results = soup.findAll("div", {"class" : "leaflet-tile leaflet-tile-loaded"})
#
# # for result in results :
# #     if len(result.attrs) == 1 :
# #         print(result)