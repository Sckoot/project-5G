from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox as mb

tel=['samsung','xaomi', 'ётафон', 'орех']

def click():
    prov=combo.get()
    if prov in tel:
        print('На вашем телефоне всё будет работать!')
        mb.showinfo('proverka', 'Ваш теелфон поддерживает 5G!')
    else:
        mb.showinfo('proverka', 'К сожалению, но ваш телефон НЕ поддерживает 5G')
        print('К сожалению, на ваш телефон не поддерживает 5G(((')

root=Tk()
root.title("5G.ru")
root.geometry('800x600')
root.resizable(True, True)
root['bg']='white'

label=Label(text='Для проверки поддержания 5G на вашем телефоне, введите модель устройства' , font=('Times New Roman', 15))
label1=Label(text='или выберите из списка.', font=('Times New Roman', 15))
combo=Combobox(root, width=30, font=('Times New Roman', 20))
combo['values']=(tel+['нокия'])
button=Button(text='Проверить',  font=('Times New Roman', 18), command=click)

label.pack()
label1.pack()
combo.pack()
button.pack()

root.mainloop()
