from nicegui import ui
import global_data
from cryptopm.pm import PM
import cryptography

def nav():
    with ui.header():
        ui.button('Главная', on_click=lambda: ui.navigate.to('/'))
        ui.button('Открыть файл', on_click=lambda: ui.navigate.to('/open'))
        ui.button('Манеджер Паролей', on_click=lambda: ui.navigate.to('/pm'))
        ui.button('Генератор Паролей', on_click=lambda: ui.navigate.to('gen'))

@ui.page('/')
def home():
    nav()
    ui.label('Сие замечательное приложение сделано студентом')
    ui.label('ИСП-225п')
    ui.label('Сергеевым Романом')
    ui.label('В рамках учебной практики 04')

def new_pm():
    try:
        global_data.PWM = PM(global_data.PATH, global_data.PASS)
    except cryptography.exceptions.InvalidTag:
        ui.notify('Неверный пароль')
    except FileNotFoundError:
        ui.notify('Такого файла нет')
    else:
        ui.notify('Файл успешно открыт и расшифрован')

@ui.page('/open')
def open_pwm():
    nav()
    ui.input('Введите путь').style('width: 400px').bind_value(global_data, 'PATH')
    ui.input('Пароль', password=True).style('width: 400px').bind_value(global_data, 'PASS')
    ui.button('Открыть', on_click=new_pm).style('width: 400px')

@ui.page('/pm')
def pass_manager():
    nav()

    with ui.row():
        ui.input('Поиск по сайту')
        ui.input('Поиск по логину')
        ui.input('Поиск по тэгам')

@ui.page('/gen')
def pass_gen():
    nav()

ui.run(native=True)