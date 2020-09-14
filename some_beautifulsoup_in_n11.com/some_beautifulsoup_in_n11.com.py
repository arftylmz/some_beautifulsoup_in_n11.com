import re
import urllib.request as urllib2
from bs4 import BeautifulSoup
from tkinter import *
from tkinterhtml import HtmlFrame

class Editor(Frame):

    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.root=parent
        self.initUI()

    def initUI(self):
        self.Sozluk = {}

        self.grid()
        frame = Frame(self, bg="Beige", width="1150", height="800", pady="25", padx="10")
        frame.grid()

        self.Urun_adi = Label(frame, text="Aramak İçin Ürün Adı Giriniz = ", fg="Blue", bg="Beige")
        self.Urun_adi.config(font=("Courier", 10, "bold italic"))
        self.Urun_adi.grid(row = 0,column = 0,columnspan = 2)

        self.aramaUrl_duzenlenicek = StringVar()
        self.degerGir = Entry(frame, textvariable=self.aramaUrl_duzenlenicek, fg="Blue", bg="Beige", width=40)
        self.degerGir.grid(row = 0, column = 2,columnspan = 2)

        self.button = Button(frame, text="Arama", fg="Blue", bg="Gold", command=self.Arama,width ="10")
        self.button.grid(row = 1, column = 0,sticky = E + S)

        self.bosLabel = Label(frame,fg="Blue", bg="Beige")
        self.bosLabel.grid(row = 2,column = 0)

        self.min = Label(frame, text="min = ", fg="Blue", bg="Beige")
        self.min.config(font=("Courier", 10, "bold italic"))
        self.min.grid(row = 3, column = 0,sticky = W)

        self.Minimum = IntVar()
        self.minGiris = Entry(frame, textvariable=self.Minimum, fg="Blue", bg="Beige", width=20)
        self.minGiris.grid(row = 3, column = 1)

        self.max = Label(frame, text = "max = ", fg="Blue", bg="Beige")
        self.max.config(font=("Courier", 10, "bold italic"))
        self.max.grid(row = 3, column = 2 )

        self.Maximum = IntVar()
        self.maxGiris = Entry(frame, textvariable=self.Maximum, fg="Blue", bg="Beige", width=20)
        self.maxGiris.grid(row = 3, column = 3)

        self.bosLabel2 = Label(frame,fg="Blue", bg="Beige")
        self.bosLabel2.grid(row = 4,column = 0)

        self.items = Label(frame, text="Ürünler:", fg="Blue", bg="Beige")
        self.items.grid(row = 5,column = 0, columnspan = 3,sticky = W)

        self.descriptions = Label(frame, text="İçerik:", fg="Blue", bg="Beige")
        self.descriptions.grid(row = 5, column = 3,sticky = W)

        self.listbox = Listbox(frame, selectmode="EXTENDED", fg="Blue", bg="Beige",height = 39)
        self.listbox.bind("<<ListboxSelect>>", self.onSelect)
        self.listbox.grid(row=6, column=0,columnspan = 3,rowspan = 2 ,sticky=W+E, pady="10")

        self.htmlFrame = HtmlFrame(frame,horizontal_scrollbar="auto")
        self.htmlFrame.grid(row = 6, column = 3,columnspan = 3, rowspan = 2, pady="10")



    def Arama(self):
        try:
            self.Sozluk.clear()
            self.listbox.delete(0,END)

            # ---------- Kullanıcıdan istenilen değerler ------------

            aramaUrl_duzenlenicek = str(self.aramaUrl_duzenlenicek.get())
            aramaUrl = re.sub('(\s)', '+', aramaUrl_duzenlenicek)
            minFiyat = self.Minimum.get()
            maxFiyat = self.Maximum.get()
            int(minFiyat)
            int(maxFiyat)

            # -------------------- n11 bağlantısı ------------------
            url = "https://www.n11.com/arama?q=" + aramaUrl
            c = urllib2.urlopen(url)
            contents = c.read()
            soup = BeautifulSoup(contents, features="html.parser")
            count = 0
            for i in soup.find_all(class_=re.compile("proDetail")):
                link = i.find("a").get('href')
                fiyat = i.find("ins").get_text()
                x = fiyat.split()
                asama1 = x[0]
                asama2 = asama1.split(",")
                kusurat = int(asama2[1])
                asama2[0] = re.sub('[.]', '', asama2[0])
                asilFiyat = int(asama2[0])
                if kusurat != 00:
                    asilFiyat = asilFiyat+1
                baslik = i.find("a").get("title")
                count += 1  # ürün sayımızı sınırlandırmak için bayrak değişkeni tutuyoruz

                urunler = asama1 + " TL " + baslik

            #------------- kullanıcının istediği minimum fiyat değerlerine göre kontrol --------------
                if maxFiyat == 0 and minFiyat == 0:
                    self.Sozluk.setdefault(urunler, "boş")
                    self.Sozluk[urunler] = link
                elif minFiyat == 0 and asilFiyat <= maxFiyat:
                    self.Sozluk.setdefault(urunler, "boş")
                    self.Sozluk[urunler] = link
                elif minFiyat <= asilFiyat and maxFiyat == 0:
                    self.Sozluk.setdefault(urunler, "boş")
                    self.Sozluk[urunler] = link
                elif minFiyat <= asilFiyat <= maxFiyat:
                    self.Sozluk.setdefault(urunler, "boş")
                    self.Sozluk[urunler] = link

                if count == 20: # ürün sayımızı 20 ile sınırlandırıyoruz.
                    break

            #------- ürünlerimizi listboxumuza ekliyoruz----------
            for j in self.Sozluk:
                self.listbox.insert(END,j)
        except:
            self.listbox.delete(0,END)
            self.listbox.insert(END,"İnternet bağlantısı kesik veya Eksik bir işlem yaptınız. lütfen işlemlerinizi tekrar deneyin.")

    def onSelect(self, val):
        try:
            widget = val.widget
            idx = widget.curselection()
            self.value = widget.get(idx)
            print(self.Sozluk[self.value])
            url = self.Sozluk[self.value]
            contents = urllib2.urlopen(url).read()
            soup = BeautifulSoup(contents, features="html.parser")
            self.htmlFrame.set_content("""<!DOCTYPE html>\n<html>\n<body>\n"""+str(soup.find_all(class_ = re.compile("tabPanelItem"))) +"""\n</body>\n</html>""")

        except:
            print("")






def main():
    root= Tk()
    root.title("n11-Searcher")
    root.geometry("1150x800+300+100")
    #konumu ayarlıyoruz ve ekran boyut ayarlamasını kapatıyoruz.
    root.resizable(FALSE,FALSE)
    App = Editor(root)
    root.mainloop()



if __name__ == '__main__':
    main()