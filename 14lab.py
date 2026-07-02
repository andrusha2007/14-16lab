# # #14.1
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, rating=0):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.rating = rating
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#     def show_flavors(self):
#         for flavor in self.flavors:
#             print(flavor)
# stand = IceCreamStand("Мороженое", "кафе", ["ванильное", "шоколадное", "клубничное"])
# print("Название:", stand.restaurant_name)
# print("Тип:", stand.cuisine_type)
# stand.show_flavors()


# 14.2
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type, rating=0):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.rating = rating
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavors, location, open_time, close_time):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors
#         self.location = location
#         self.open_time = open_time
#         self.close_time = close_time
#     def show_flavors(self):
#         for flavor in self.flavors:
#             print(flavor)
#
#     def add_flavor(self, flavor):
#         self.flavors.append(flavor)
#         print(f"Добавлен сорт: {flavor}")
#
#     def remove_flavor(self, flavor):
#         if flavor in self.flavors:
#             self.flavors.remove(flavor)
#             print(f"Удален сорт: {flavor}")
#         else:
#             print(f"Сорт {flavor} не найден")
#
#     def has_flavor(self, flavor):
#         return flavor in self.flavors
#
#     def add_popsicle(self, flavor):
#         print(f"Мороженое на палочке: {flavor}")
#         self.add_flavor(flavor + " на палочке")
#
#     def add_soft_icecream(self, flavor):
#         print(f"Мягкое мороженое: {flavor}")
#         self.add_flavor(flavor + " мягкое")
# stand = IceCreamStand(
#     "Мороженое",
#     "кафе",
#     ["ванильное", "шоколадное", "клубничное"],
#     "ул. Пушкина 10",
#     "10:00",
#     "22:00"
# )
#
# print("Текущие сорта:")
# stand.show_flavors()
# print()
# stand.add_flavor("мятное")
# print()
# print("Есть ванильное?", stand.has_flavor("ванильное"))
# print("Есть карамельное?", stand.has_flavor("карамельное"))
# print()
# stand.remove_flavor("мятное")
# print()
# stand.add_popsicle("шоколадное")
# stand.add_soft_icecream("ванильное")
# print()
# print("Итоговые сорта:")
# stand.show_flavors()

# #3
import tkinter as tk
from tkinter import messagebox

class IceCreamStandGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Кафе-мороженое")
        self.root.geometry("400x300")

        self.flavors = ["Ванильное", "Шоколадное", "Клубничное", "Фисташковое"]

        tk.Label(root, text="Кафе - мороженое", font=("Arial", 16)).pack(pady=10)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_listbox()

        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=5)

        tk.Label(entry_frame, text="Новый сорт:").pack(side=tk.LEFT)
        self.entry = tk.Entry(entry_frame)
        self.entry.pack(side=tk.LEFT, padx=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Добавить", command=self.add_flavor).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Удалить", command=self.remove_flavor).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Проверить", command=self.check_flavor).pack(side=tk.LEFT, padx=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for flavor in self.flavors:
            self.listbox.insert(tk.END, flavor)

    def add_flavor(self):
        new_flavor = self.entry.get().strip()
        if new_flavor:
            if new_flavor not in self.flavors:
                self.flavors.append(new_flavor)
                self.update_listbox()
                self.entry.delete(0, tk.END)
                messagebox.showinfo("Успешно", f"Сорт '{new_flavor}' добавлен")
            else:
                messagebox.showwarning("Внимание", "Такой сорт уже есть")
        else:
            messagebox.showwarning("Ошибка", "Введите название сорта")

    def remove_flavor(self):
        selected = self.listbox.curselection()
        if selected:
            flavor = self.listbox.get(selected[0])
            self.flavors.remove(flavor)
            self.update_listbox()
            messagebox.showinfo("Успешно", f"Сорт '{flavor}' удален")
        else:
            messagebox.showwarning("Ошибка", "Выберите сорт для удаления")

    def check_flavor(self):
        flavor = self.entry.get().strip()
        if flavor:
            if flavor in self.flavors:
                messagebox.showinfo("Результат", f"Сорт '{flavor}' есть в наличии")
            else:
                messagebox.showinfo("Результат", f"Сорта '{flavor}' нет в наличии")
        else:
            messagebox.showwarning("Ошибка", "Введите название сорта для проверки")

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamStandGUI(root)
    root.mainloop()
