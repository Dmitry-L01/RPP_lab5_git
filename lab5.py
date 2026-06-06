# Версия 2.0. Для GIT.

import csv
import tkinter as tk # библиотека для окон
import os  # библиотека для работы с файлами и папками
from tkinter import ttk # для таблиц

# Создаем не зависимый класс
class Car:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.data = self.get_data(folder_path)  # сразу загружаем данные
    
    # Статический метод (работает сам по себе)
    # ==========Получить данные из data.csv==========
    @staticmethod
    def get_data(folder_path):
        data = []
        with open(f'{folder_path}/data.csv', "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    
    # ==========Подсчет кол-ва файлов==========
    @staticmethod
    def count_files(folder_path):
        # folder_path = "./lab4"  # текущая папка (где лежит программа)
        contents = os.listdir(folder_path) # Получаем список всего содержимого папки
        files = [f for f in contents if os.path.isfile(os.path.join(folder_path, f))] # Оставляем только файлы (отбрасываем папки)
        count = len(files)
        return count
    
    # ==========Вывод списка==========
    def out_List(self, operation):
        data2 = self.data[:] # Копируем массив
        
        for row in tree.get_children(): # Очистить все строки таблицы
            tree.delete(row)
        
        if( operation == 'date'):
            data2.sort(key=lambda row: row[1]) # сортируем массив по колонке 1(дата) key=lambda row: временная переменная
            for row in data2:
                tree.insert("", "end", values=row) # "" - корневой уровень, "end" - вставить в конец, что вставить
        elif (operation == 'numberSign'):
            data2.sort(key=lambda row: row[2])
            for row in data2:
                tree.insert("", "end", values=row)
        elif (operation == 'model'):
            data2.sort(key=lambda row: row[3])
            for row in data2:
                tree.insert("", "end", values=row)
        else:
            for items in self.data:
                tree.insert("", "end", values=items)
        
    # ==========Обработка кнопки добавления==========
    def button_add_click(self):
        # Получаем данные из полей
        val_date = entry_date.get()
        val_numberSign = entry_numberSign.get()
        val_model = entry_model.get()
        # Проверка на пустое поле
        if ((val_date == '') or (val_numberSign == '') or (val_model == '')):
            return
        
        id = len(self.data)+1
        self.data.append([str(id), val_date,val_numberSign,val_model]) # Так же добавляем в массив
        
        # Открываем в режиме добавления (append)
        with open(f'{self.folder_path}/data.csv', "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([str(id), val_date, val_numberSign, val_model])
        
        self.out_List('id') # Обновляем список по id
    
    
    # ==========Поиск ис списка==========
    def search_List(self):
        # Получаем данные из полей
        value = entry_search.get()
        column = combo_search.get()

        # Сортируем выбор
        if column == 'ID':
            column = 0
        elif column == 'Дата':
            column = 1
        elif column == 'Номерной знак':
            column = 2
        elif column == 'Марка':
            column = 3
        else:
            return
        
        # Очистить все строки таблицы
        for row in tree.get_children():
            tree.delete(row)
        # Вывести совпадения
        for items in self.data:
            if value.lower() in items[column].lower():
                tree.insert("", "end", values=items)



os.system('cls') # Просим очистить терминал

car = Car('./lab4') 

root = tk.Tk() # Создаём пустое окно
root.title("История проездов автомобилей")

# Центрируем
x = (root.winfo_screenwidth() - 600) // 2  # отступ слева     // - деление без остатка
y = (root.winfo_screenheight() - 900) // 2 # отступ сверху
root.geometry(f"600x800+{x}+{y}") # Устанавливаем ширину и высоту + отступы

# ==========Отображение блока Кол-во файлов==========
root.columnconfigure(0, weight=1) # Выравнивание по центру

frame1 = tk.Frame(root, bd=2, relief="solid") # Создаем блок    bd-толщина обводки  relief-способ заливки
frame1.grid(row=0, column=0, pady=(5, 0)) # Добавляем в сетку   pady-отступы(сверху, снизу)

label0_1 = tk.Label(
    frame1, 
    text="Количество файлов в директории:", 
    font=("Times New Roman", 12),
    )
label0_2 = tk.Label(
    frame1, 
    text=f"{car.count_files('./lab4')} шт.", 
    font=("Times New Roman", 12, "bold italic"),
    )

label0_1.grid(row=0, column=0)
label0_2.grid(row=0, column=1)


# ==========Отображение блока добавление записи==========
frame2 = tk.Frame(root, bd=1, relief='solid')
frame2.grid(row=1, column=0, padx=5, pady=(20, 0))

entry_date = tk.Entry(frame2, justify='center')
label_date = tk.Label(
    frame2, 
    text="Дата и время \n(ГГГГ-ММ-ДД ЧЧ:ММ)", 
    font=("Times New Roman", 8),
    )
entry_numberSign = tk.Entry(frame2, justify='center')
label_numberSign = tk.Label(
    frame2, 
    text="Номерной знак", 
    font=("Times New Roman", 8),
    anchor='center'
    )
entry_model = tk.Entry(frame2, justify='center')
label_model = tk.Label(
    frame2, 
    text="Модель", 
    font=("Times New Roman", 8),
    anchor='center'
    )
button_add = tk.Button(frame2, text="Добавить запись", font=("Times New Roman", 8), command= car.button_add_click)

# Вывод на экран
label_date.grid(row=0, column=0, padx=5)
entry_date.grid(row=1, column=0, padx=5)
label_numberSign.grid(row=0, column=1, padx=5)
entry_numberSign.grid(row=1, column=1, padx=5, pady=(0,5))
label_model.grid(row=0, column=2, padx=5)
entry_model.grid(row=1, column=2, padx=5, pady=(0,5))
button_add.grid(row=0, column=3, rowspan=2, padx=5)


# ==========Отображение блока сортировки==========
frame3 = tk.Frame(root)
frame3.grid(row=2, column=0, padx=5, pady=(20, 0))

label_sort = tk.Label(
    frame3, 
    text="Сортировка по:", 
    font=("Times New Roman", 12),
    )
# lambda Создаём анонимную функцию, которая вызовется при клике
button_id = tk.Button(frame3, text="ID", font=("Times New Roman", 8), command=lambda: car.out_List('id'))
button_date = tk.Button(frame3, text="Дата", font=("Times New Roman", 8), command=lambda: car.out_List('date'))
button_numberSign = tk.Button(frame3, text="Знак", font=("Times New Roman", 8), command=lambda: car.out_List('numberSign'))
button_model = tk.Button(frame3, text="Марка", font=("Times New Roman", 8), command=lambda: car.out_List('model'))

label_sort.grid(row=0, column=0, padx=5)
button_id.grid(row=0, column=1, padx=5)
button_date.grid(row=0, column=2, padx=5)
button_numberSign.grid(row=0, column=3, padx=5)
button_model.grid(row=0, column=4, padx=5)

# ==========Поиск по значению==========
frame4 = tk.Frame(root)
frame4.grid(row=3, column=0, padx=5, pady=(5, 0))

label_search = tk.Label(
    frame4, 
    text="Поиск:", 
    font=("Times New Roman", 12),
    )
entry_search = tk.Entry(frame4, justify='center')
label_search2 = tk.Label(
    frame4, 
    text="Из:", 
    font=("Times New Roman", 12),
    )
combo_search = ttk.Combobox(frame4, values=["ID", "Дата", "Номерной знак", "Марка"], state='readonly')
btn_search = tk.Button(frame4, text="Поиск", font=("Times New Roman", 8), command=lambda: car.search_List())

label_search.grid(row=0,column=0,padx=5)
entry_search.grid(row=0, column=1, padx=5)
label_search2.grid(row=0,column=2,padx=5)
combo_search.grid(row=0,column=3,padx=5)
btn_search.grid(row=0,column=4,)

# ==========Отображение блока с таблицей==========
frame5 = tk.Frame(root)
frame5.grid(row=4, column=0, padx=5, pady=(5, 0))
columns = ("номер", "дата", "знак", "марка")
tree = ttk.Treeview(frame5, columns=columns, show="headings")

# Настраиваем заголовки
tree.heading("номер", text="№")
tree.heading("дата", text="Дата и время")
tree.heading("знак", text="Номерной знак")
tree.heading("марка", text="Марка")

# Настраиваем ширину колонок
tree.column("номер", width=50, anchor="center")
tree.column("дата", width=150, anchor="center")
tree.column("знак", width=150, anchor="center")
tree.column("марка", width=150, anchor="center")

# Размещаем таблицу
tree.pack(fill=tk.BOTH, expand=True)

car.out_List('id') # Вызываем функцию вывода по id
print("Ветка bugfix")

print("Ветка feature")

root.mainloop() #Запускаем окно