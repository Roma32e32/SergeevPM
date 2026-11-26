from nicegui import ui, app
from .header import nav
from cryptography.exceptions import InvalidTag
from ast import literal_eval
from aes_bridge import decrypt
from pathlib import Path


#@ui.page("/open")
def open_pwm():
    def new_cf():
        try:
            raw = Path(app.storage.client['path']).read_text(encoding="utf-8")
            decrypted = decrypt(raw, app.storage.client['password'])
            records = literal_eval(decrypted.decode("utf-8"))
            app.storage.client["records"] = records
            app.storage.client['current_password'] = app.storage.client['password']
        except InvalidTag:
            ui.notify("Неверный пароль")
        except FileNotFoundError:
            ui.notify("Такого файла нет")
        else:
            ui.notify("Файл успешно открыт и расшифрован")

    #nav()
    ui.input("Введите путь").style("width: 400px").bind_value(app.storage.client, "path")
    ui.input("Пароль", password=True).style("width: 400px").bind_value(app.storage.client, "password")
    ui.button("Открыть", on_click=new_cf).style("width: 400px")