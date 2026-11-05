import customtkinter as ctk
from tkinter import filedialog
from frames import OpenFrame, DecryptFrame, ManagerFrame




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Переключение фреймов")
        self.geometry("900x600")

        # Контейнер для фреймов (чтобы не пересоздавать окно)
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.current_frame = None  # Ссылка на текущий фрейм

        self.show_OF()

    def clear_container(self):
        """Удаляет текущий фрейм"""
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def show_OF(self):
        self.clear_container()
        self.current_frame = OpenFrame(self.container, self.show_DF)
        self.current_frame.pack(fill="both", expand=True)

    def show_DF(self, filepath):
        self.clear_container()
        self.current_frame = DecryptFrame(self.container, filepath, self.show_OF, self.show_MF)
        self.current_frame.pack(fill="both", expand=True)

    def show_MF(self):
        self.clear_container()
        self.current_frame = ManagerFrame(self.container, self.show_OF)
        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()