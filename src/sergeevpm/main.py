import random
import string

import cryptography
import global_data
from cryptopm.pm import PM
from nicegui import binding, ui


@binding.bindable_dataclass
class Filters:
    site: str = ""
    login: str = ""
    tags: str = ""


PASSWORD_CHARSETS = {
    "Строчные": string.ascii_lowercase,
    "Прописные": string.ascii_uppercase,
    "Цифры": string.digits,
    "Символы": "!@#$%^&*()-_=+[]{}:;,.?/",
}


def nav():
    with ui.header():
        ui.button("Главная", on_click=lambda: ui.navigate.to("/"))
        ui.button("Открыть файл", on_click=lambda: ui.navigate.to("/open"))
        ui.button("Манеджер Паролей", on_click=lambda: ui.navigate.to("/pm"))
        ui.button("Генератор Паролей", on_click=lambda: ui.navigate.to("gen"))


@ui.page("/")
def home():
    nav()
    ui.label("Сие замечательное приложение сделано студентом")
    ui.label("ИСП-225п")
    ui.label("Сергеевым Романом")
    ui.label("В рамках учебной практики 04")


def new_pm():
    try:
        global_data.PWM = PM(global_data.PATH, global_data.PASS)
    except cryptography.exceptions.InvalidTag:
        ui.notify("Неверный пароль")
    except FileNotFoundError:
        ui.notify("Такого файла нет")
    else:
        ui.notify("Файл успешно открыт и расшифрован")


@ui.page("/open")
def open_pwm():
    nav()
    ui.input("Введите путь").style("width: 400px").bind_value(global_data, "PATH")
    ui.input("Пароль", password=True).style("width: 400px").bind_value(
        global_data, "PASS"
    )
    ui.button("Открыть", on_click=new_pm).style("width: 400px")


@ui.page("/pm")
def pass_manager():
    nav()

    pm = global_data.PWM
    if pm is None:
        ui.label("Файл не открыт")
        ui.button("Открыть файл", on_click=lambda: ui.navigate.to("/open"))
        return

    filters = Filters()

    def delete(index):
        del pm.records[index]
        pm.save()
        table.refresh()

    def add():
        pm.add_record()
        filters.site = filters.login = filters.tags = ""
        table.refresh()

    @ui.refreshable
    def table():
        found = pm.find(
            site=filters.site or None,
            login=filters.login or None,
            tags=[tag.strip() for tag in filters.tags.split(",") if tag.strip()]
            or None,
        )
        if not found:
            ui.label("Ничего не найдено")
        for index in found:
            record = pm.records[index]
            with ui.row().classes("items-center"):
                ui.input("Сайт").bind_value(record, "site").on_value_change(pm.save)
                ui.input("Логин").bind_value(record, "login").on_value_change(pm.save)
                ui.input("Тэги").bind_value(record, "tags").on_value_change(pm.save)
                ui.input("Пароль", password=True).bind_value(
                    record, "password"
                ).on_value_change(pm.save)
                ui.button(icon="delete", on_click=lambda i=index: delete(i)).props(
                    "flat round dense color=negative"
                )

    with ui.row():
        ui.input("Поиск по сайту").bind_value(filters, "site").on(
            "keydown.enter", table.refresh
        )
        ui.input("Поиск по логину").bind_value(filters, "login").on(
            "keydown.enter", table.refresh
        )
        ui.input("Поиск по тэгам").bind_value(filters, "tags").on(
            "keydown.enter", table.refresh
        )
        ui.button("Найти", icon="search", on_click=table.refresh)
        ui.button("Добавить", icon="add", on_click=add)

    ui.separator().classes("bg-black")
    table()


@ui.page("/gen")
def pass_gen():
    nav()

    mouse = bytearray()
    counter = 0

    def collect(event):
        data = event.args.values() if isinstance(event.args, dict) else event.args
        for value in data:
            mouse.append(int(value or 0) & 0xFF)
        del mouse[:-512]
        status.set_text(f"Набрано энтропии: {len(mouse)} байт")

    def generate():
        nonlocal counter
        groups = [charset for box, charset in checkboxes if box.value]
        if not groups:
            ui.notify("Выберите хотя бы один набор символов", type="warning")
            return
        if len(mouse) < 64:
            ui.notify("Подвигайте мышкой по полю выше", type="warning")
            return
        rng = random.Random(bytes(mouse) + counter.to_bytes(8, "big"))
        counter += 1
        length = int(length_slider.value)
        chars = [rng.choice(group) for group in groups]
        chars += rng.choices("".join(groups), k=length - len(chars))
        rng.shuffle(chars)
        password_field.value = "".join(chars)

    def copy():
        if not password_field.value:
            ui.notify("Сначала сгенерируйте пароль", type="warning")
            return
        ui.clipboard.write(password_field.value)
        ui.notify("Пароль скопирован")

    with ui.column().classes("w-full max-w-xl gap-4"):
        ui.label("Проведите мышкой по полю — движения станут энтропией для пароля")
        area = ui.column().classes(
            "w-full h-40 border-2 border-dashed border-gray-400 rounded items-center justify-center cursor-crosshair"
        )
        with area:
            status = ui.label("Набрано энтропии: 0 байт")
        area.on(
            "mousemove",
            collect,
            js_handler="(e) => emit(e.movementX, e.movementY, e.offsetX, e.offsetY, e.timeStamp)",
            throttle=0.05,
        )

        with ui.row():
            checkboxes = [
                (ui.checkbox(name, value=True), charset)
                for name, charset in PASSWORD_CHARSETS.items()
            ]

        with ui.row().classes("items-center"):
            ui.label("Длина")
            length_slider = (
                ui.slider(min=8, max=64, value=16).props("label-always").classes("w-64")
            )

        password_field = (
            ui.input("Пароль").props("readonly outlined").classes("w-full font-mono")
        )

        with ui.row():
            ui.button("Сгенерировать", icon="casino", on_click=generate)
            ui.button("Скопировать", icon="content_copy", on_click=copy)


ui.run(native=True)
