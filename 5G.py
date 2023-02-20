from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

tel=['Apple iPhone 12 Pro Max', 'Apple iPhone 12 Pro', 'Apple iPhone 12 Mini', 'Apple iPhone 12', 'Huawei P40','Huawei P40 Pro','Huawei P40 Lite', 'Huawei Mate 30E Pro', 'Huawei Enjoy 20 Plus', 'Huawei Enjoy 20 Pro', 'Huawei Nova 8 SE','Huawei Nova 7 Pro', 'Huawei Nova 7 SE', 'Huawei Nova 7','Huawei Nova 6','Huawei Mate Xs','Huawei Mate X','Huawei Mate 30 Pro','Huawei Mate 30','Honor V30','Honor View 30 Pro','Honor 30 S', 'Samsung Galaxy A51','Samsung W21', 'Samsung W20', 'Samsung Galaxy S20+', 'Samsung Galaxy S20', 'Samsung Galaxy A71', 'Sharp Aquos Sense', 'Sharp Aquos', 'Oppo Realme 7', 'Oppo A92s', 'Oppo Realme X50 Pro', 'Oppo Find X2 Pro','Oppo Find X2 Lite', 'Oppo Find X2', 'Oppo Reno 3 Pro', 'Oppo Reno 3', 'ZTE Axon 10S Pro', 'ZTE a1', 'ZTE Axon 11', 'ZTE Rakuten BIG','ZTE Nubia', 'ZTE Nubia Play', 'Xiaomi Mi 10 Youth', 'Xiaomi Mi 10 Lite', 'Xiaomi Redmi K30 Pro', 'Xiaomi Redmi K30', 'Realme X50m','Xiaomi Black Shark 3 Pro','Xiaomi Black Shark 3','Vivo S6', 'Vivo Z6', 'Vivo Nex 3S', 'Vivo iQOO Pro', 'Vivo iQOO 5 Pro', 'Vivo iQOO 5', 'Vivo iQOO Z1x', 'Vivo iQOO 3', 'Vivo G1', 'BBK Vivo iQOO Z1', 'Vivo X30', 'Vivo Nex 3', 'Pocophone Poco F2 Pro','Fujitsu Arrows NX 9','Meizu 17 Aircraft','Meizu 17 Pro', 'Meizu 17', 'LG Velvet', 'Planet Computers','OnePlus 8 Pro', 'OnePlus 8', 'Oppo Ace2','Motorola Edge', 'Motorola Edge+', 'TCL 10', 'Nokia 8.3', 'Sony Xperia 1', 'LG V50S ThinQ']


def click():
    prov=combo.get()
    if prov in tel:
        print('На вашем телефоне всё будет работать!')
        mb.showinfo('proverka', 'Ваш теелфон поддерживает 5G!')
    else:
        mb.showinfo('proverka', 'К сожалению, но ваш телефон НЕ поддерживает 5G')
        print('К сожалению, ваш телефон не поддерживает 5G')

root=Tk()
root.title("5G.ru")
root.geometry('800x600')
root.resizable(True, True)
root['bg']='white'

label=Label(text='Для проверки поддержания 5G на вашем телефоне, введите модель устройства' , font=('Times New Roman', 15))
label1=Label(text='или выберите из списка.', font=('Times New Roman', 15))
combo=Combobox(root, width=30, font=('Times New Roman', 20))
combo['values']=(['если вашего телефона в списке не окажется, то введите его вручную'] + tel+['Apple iPhone XS Max', 'Aplee iPhone XS', 'Apple iPhone Pro 11'])
button=Button(text='Проверить',  font=('Times New Roman', 18), command=click)

label.pack()
label1.pack()
combo.pack()
button.pack()

root.mainloop()
