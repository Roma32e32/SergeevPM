from nicegui import ui
from .header import nav

#@ui.page("/home")
def home():
    #nav()
    ui.label("Сие замечательное приложение сделано студентом")
    ui.label("группы ИСП-225п")
    ui.label("Сергеевым Романом")
    ui.label("В рамках учебной практики 04")