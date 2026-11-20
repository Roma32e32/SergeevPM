from nicegui import ui
from crypto_file import CryptoFile
import ast
import global_data
import cryptography


def nav():
    with ui.header():
        ui.button('Главная', on_click=lambda: ui.navigate.to('/'))
        ui.button('Открыть файл', on_click=lambda: ui.navigate.to('/open'))
        ui.button('Манеджер Паролей', on_click=lambda: ui.navigate.to('/pm'))
        #ui.button('Генератор Паролей', on_click=lambda: ui.navigate.to('gen'))

@ui.page('/')
def home():
    nav()
    ui.label('Сие замечательное приложение сделано студентом')
    ui.label('группы ИСП-225п')
    ui.label('Сергеевым Романом')
    ui.label('В рамках учебной практики 04')

def new_cf():
    try:
        global_data.CF = CryptoFile(global_data.PATH, global_data.PASS)
        global_data.ROWS = ast.literal_eval(global_data.CF.read())
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
    ui.button('Открыть', on_click=new_cf).style('width: 400px')

@ui.page('/pm')
def pass_manager():
    nav()
    table = ui.aggrid({
        'columnDefs': [{'headerName': 'Name', 'field': 'name', 'editable': True},
                       {'headerName': 'Age', 'field': 'age', 'editable': True}],
        'rowData': global_data.ROWS
    })

    def sync(e):
        global_data.ROWS[int(e.args['rowId'])][e.args['colId']] = e.args['newValue']
        global_data.CF.write(str(global_data.ROWS))
    table.on('cellValueChanged', sync)

ui.run(native=True)