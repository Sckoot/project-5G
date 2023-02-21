from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

tel=['Apple iPhone 14', 'Apple iPhone 13', 'Apple iPhone 12', 'Samsung Galaxy Z Flod4', 'Samsung Galaxy Z Flip4 ', 'Samsung Galaxy Z Flod3', 'Samsung Galaxy Z Flip3 ', 'Samsung Galaxy S23', 'Samsung Galaxy S22','Samsung Galaxy S21','Samsung Galaxy A73','Samsung Galaxy A53','Samsung Galaxy A52','Samsung Galaxy A03','Samsung Galaxy A33','Samsung Galaxy A32','Samsung Galaxy A23','Samsung Galaxy A22','Samsung Galaxy A13','Samsung Galaxy A12','Samsung Galaxy M53','Samsung Galaxy M33','Samsung Galaxy M32','Samsung Galaxy M23','Samsung Galaxy M22','Samsung Galaxy M12', 'Huawei Mate P40', 'Huawei Honor 30Pro Plus', 'Meizu 18', 'Nokia G50 DS', 'Nokia XR20', 'Nokia X20', 'Nokia X10', 'LG WING ™ 5G | AT & T', 'LG K92™ 5G | AT&T', 'LG VELVET™ 5G | AT&T', 'LG V60 ThinQ ™ 5G | AT & T', 'LG V60 ThinQ ™ 5G | Cricket', 'Двойной экран LG V60 ThinQ ™ 5G | Sprint', 'LG V60 ThinQ™ 5G | Sprint', 'LG WING ™ 5G | T-Mobile', 'LG VELVET™ 5G | T-Mobile', 'Двойной экран LG V60 ThinQ ™ 5G | T-Mobile', 'LG V60 ThinQ™ 5G | T-Mobile', 'LG K92™ 5G | U.S. Cellular', 'LG V60 ThinQ™ 5G | U.S. Cellular', 'LG WING™ 5G | Verizon', 'LG VELVET™ 5G UW | Verizon', 'LG V60 ThinQ™ 5G UW | Verizon', 'LG V50 ThinQ ™ 5G | Verizon', 'Lenovo Legion Y90', 'Xiaomi 11', 'Xiaomi 12', 'Xiaomi Black Shark 4', 'Xiaomi Black Shark 5', 'Xiaomi Poco x4', ' Xiaomi Poco x5', ' Xiaomi Poco M3', 'Xiaomi Poco M4', 'Xiaomi Redmi Note 12', 'Xiaomi Redmi Note 11', 'Xiaomi Redmi Note 10', 'Xiaomi Redmi k30', 'Xiaomi Redmi k40', 'Xiaomi Redmi k50', 'Xiaomi Mi 10', 'Xiaomi Mi 11', 'Realme x50', 'Realme  GT Neo 3', 'Realme  GT2', 'Realme  V25', 'Realme  GT Neo Flash Edition', 'Realme  GT Neo 2', 'Realme  Q3s', 'Realme  9', 'Realme  GT', 'Oppo Reno6', 'Oppo Reno7', 'Oppo Reno5', 'Oppo Reno4', 'Oppo Find x3', 'Oppo Find x5', 'ZTE Nubia Red Magic 8 Pro', 'ZTE Nubia Red Magic 7 Pro', 'ZTE Nubia Red Magic 5s']
def click():
    prov=combo.get()
    if prov in tel:
        print('На вашем телефоне всё будет работать!')
        mb.showinfo('proverka', 'Ваш телефон поддерживает 5G!')
    else:
        mb.showinfo('proverka', 'К сожалению, ваш телефон НЕ поддерживает 5G')
        print('К сожалению, ваш телефон не поддерживает 5G')

root=Tk()
root.title("5G.ru")
root.geometry('800x600')
root.resizable(True, True)
root['bg']='white'

label=Label(text='Для проверки поддержания 5G на вашем телефоне, введите модель устройства' , font=('Times New Roman', 15))
label1=Label(text='или выберите из списка.', font=('Times New Roman', 15))
combo=Combobox(root, width=30, font=('Times New Roman', 20))
combo['values']=(tel)
button=Button(text='Проверить',  font=('Times New Roman', 18), command=click)

label.pack()
label1.pack()
combo.pack()
button.pack()

root.mainloop()
