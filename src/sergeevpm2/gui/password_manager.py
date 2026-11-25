from nicegui import ui, app
from gui.header import nav
from gui.custom_table import custom_table
from gui.search_input import search_input


def password_manager():
    search_input()
    ui.separator()
    custom_table()