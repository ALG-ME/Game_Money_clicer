import tkinter as tk
import time
import image
from PIL import Image, ImageTk


# Глобальные переменные
ruble_count = 0
start_time = None

# Функция для обновления счета рублей
def update_ruble_count(label):
    label.config(text=f"Рублей: {ruble_count}")

# Функция для обработки нажатия на картинку
def click_image(event):
    global ruble_count
    ruble_count += 1
    update_ruble_count(ruble_label)

# Функция для обработки нажатия на кнопку "Сброс"
def reset_button():
    global ruble_count, start_time
    ruble_count = 0
    start_time = time.time()
    update_ruble_count(ruble_label)
    time_label.config(text="Время: 0 сек")

# Функция для обновления таймера
def update_timer():
    global start_time
    if start_time is not None:
        elapsed_time = int(time.time() - start_time)
        time_label.config(text=f"Время: {elapsed_time} сек")
    window.after(1000, update_timer)  # Обновляем таймер каждую секунду

# Создание главного окна
window = tk.Tk()
window.title("Кликер")
window.geometry("400x400")
window.configure(bg="#ECECEC")  # Изменение цвета окна

# Создание метки для счета рублей
ruble_label = tk.Label(window, text=f"Рублей: {ruble_count}", font=("Helvetica", 18), bg="#ECECEC")
ruble_label.pack(pady=10)

# Создание метки для времени
time_label = tk.Label(window, text="Время: 0 сек", font=("Helvetica", 14), bg="#ECECEC")
time_label.pack(side="left", padx=10, pady=10)

# Загрузка картинки для нажатия
image = Image.open("maxresdefault.jpg")  #путь к изображению
image = image.resize((600, 100))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(window, image=photo, bg="#ECECEC")
image_label.image = photo  # Сохранение ссылки на изображение
image_label.bind("<Button-1>", click_image)
image_label.pack()

# Создание кнопки "Сброс" внизу экрана
reset_button = tk.Button(window, text="Сброс", command=reset_button, font=("Helvetica", 14))
reset_button.pack(side="bottom", pady=20)

# Запуск таймера
update_timer()

# Запуск главного цикла
window.mainloop()
