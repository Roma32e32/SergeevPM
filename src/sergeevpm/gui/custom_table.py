from nicegui import ui, app
from backend.search import search
from backend.save import save
from backend.record import Record, new_record


@ui.refreshable
def custom_table():
    records = app.storage.client["records"]

    found = search(
        records=records,
        site=app.storage.client["site_filter"],
        login=app.storage.client["login_filter"],
        tags=app.storage.client["tag_filter"]
    )
    with ui.grid(columns=4):
        ui.label("Сайт")
        ui.label("Логин")
        ui.label("Тэги")
        ui.label("Пароль")
        for index in found:
            record = records[index]
            ui.input().bind_value(record, "Site").on_value_change(save)
            ui.input().bind_value(record, "Login").on_value_change(save)
            ui.input_chips().bind_value(record, "Tags").on_value_change(save)
            ui.input().bind_value(record, "Password").on_value_change(save)

    ui.button("+").classes("w-full").on_click(lambda: records.append(new_record())).on_click(custom_table.refresh)
