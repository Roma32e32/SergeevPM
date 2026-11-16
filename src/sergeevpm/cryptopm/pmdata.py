from nicegui import binding


@binding.bindable_dataclass
class Record:
    """Строка менеджера паролей. Поля биндятся к элементам NiceGUI напрямую."""

    site: str = ''
    login: str = ''
    tags: str = ''
    password: str = ''
