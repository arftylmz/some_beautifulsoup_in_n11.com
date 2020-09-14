import re
import urllib.request as urllib2
from bs4 import BeautifulSoup
# #---------- Kullanıcıdan istenilen değerler ------------
# aramaUrl_duzenlenicek = input("iphone se")
# aramaUrl= re.sub('(\s)','+',aramaUrl_duzenlenicek)
# minFiyat1 = 0
# maxFiyat1 = 200
# minFiyat = int(minFiyat1)
# maxFiyat = int(maxFiyat1)
#
#
# #-------------------- n11 bağlantısı ------------------
# url = "https://www.n11.com/arama?q=" + aramaUrl
# c = urllib2.urlopen(url)
# contents = c.read()
# soup = BeautifulSoup(contents,features="html.parser")
# count = 0
# Sozluk = {}
# for i in soup.find_all(class_ = re.compile("proDetail")):
#     link = i.find("a").get('href')
#     fiyat = i.find("ins").get_text()
#     x = fiyat.split()
#     asama1 = x[0]
#     asama2 = asama1.split(",")
#     asama2[0] = re.sub('[.]','',asama2[0])
#     asilFiyat = int(asama2[0])
#     baslik = i.find("a").get("title")
#     count += 1
#     if maxFiyat == 0 and minFiyat == 0:
#         Sozluk.setdefault(baslik,"boş")
#         Sozluk[baslik] = link
#     elif minFiyat == 0 and asilFiyat <= maxFiyat:
#         Sozluk.setdefault(baslik, "boş")
#         Sozluk[baslik] = link
#     elif minFiyat <= asilFiyat and maxFiyat == 0:
#         Sozluk.setdefault(baslik, "boş")
#         Sozluk[baslik] = link
#     elif minFiyat <= asilFiyat <= maxFiyat :
#         Sozluk.setdefault(baslik, "boş")
#         Sozluk[baslik] = link
#     print(baslik)
#     print(link)
#     print(asilFiyat)
#     if count == 10:
#         break
# print(Sozluk)




try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

from tkinterhtml import HtmlFrame

root = tk.Tk()

frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.grid(sticky=tk.NSEW)

frame.set_content("""
<html>
<body>
<h1>Hello world!</h1>
</body>
</html>
""")


# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# root.mainloop()
# url = "https://urun.n11.com/ikinci-el-telefonlar/apple-iphone-se-16gb-yenilenmis-P385929324"
# contents = urllib2.urlopen(url).read()
# soup = BeautifulSoup(contents,features="html.parser")
# print("""<html>\n<body>\n"""+str(soup.find_all(class_ = re.compile("tabPanelItem"))) +"""\n</body>\n</html>""")

