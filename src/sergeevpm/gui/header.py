from nicegui import ui

def nav():
    with ui.header():
        ui.button("Главная", on_click=lambda: ui.navigate.to("/"))
        ui.button("Открыть файл", on_click=lambda: ui.navigate.to("/open"))
        ui.button("Манеджер Паролей", on_click=lambda: ui.navigate.to("/pm"))
        # ui.button('Генератор Паролей', on_click=lambda: ui.navigate.to('gen'))