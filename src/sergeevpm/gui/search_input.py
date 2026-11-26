from nicegui import ui, app
from gui.custom_table import custom_table

def search_input():
    with ui.grid(columns=4):
        ui.input('Поиск по сайту').bind_value(app.storage.client, 'site_filter')
        ui.input('Поиск по логину').bind_value(app.storage.client, 'login_filter')
        ui.input_chips('Поиск по тэгам').bind_value(app.storage.client, 'tag_filter')
        ui.button('Найти').on_click(custom_table.refresh)