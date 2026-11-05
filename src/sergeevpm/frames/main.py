import customtkinter as ctk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=(("CSV", "*.csv"), ("Все файлы", "*.*"))
    )
    return filepath


class OpenFrame(ctk.CTkFrame):
    def __init__(self, master, DF_callback):
        super().__init__(master)
        self.DF_callback = DF_callback

        ctk.CTkLabel(self, text="Это Первый фрейм", font=("Arial", 20)).pack(pady=40)
        ctk.CTkButton(self, text="Открыть файл", command=self.callback_open_file).pack(pady=10)

    def callback_open_file(self):
        filepath = open_file()
        if filepath:  # Если пользователь не отменил выбор
            self.DF_callback(filepath)


class DecryptFrame(ctk.CTkFrame):
    def __init__(self, master, file_path, OF_callback, MF_callback):
        super().__init__(master)
        self.file_path = file_path  # Сохраняем путь

        ctk.CTkLabel(self, text="Введите пароль", font=("Arial", 20)).pack(pady=40)
        ctk.CTkLabel(self, text=f"Выбран файл: {file_path}", font=("Arial", 12)).pack(pady=10)
        ctk.CTkEntry(self, placeholder_text="сюда", show="*").pack(pady=10)

        ctk.CTkButton(self, text="Выбрать другой файл", command=OF_callback).pack(pady=10)
        ctk.CTkButton(self, text="К менеджеру", command=MF_callback).pack(pady=10)


class ManagerFrame(ctk.CTkFrame):
    def __init__(self, master, OF_callback):
        super().__init__(master)

        ctk.CTkLabel(self, text="Менеджер паролей", font=("Arial", 20)).pack(pady=40)
        ctk.CTkButton(self, text="Вернуться к первому", command=OF_callback).pack(pady=10)