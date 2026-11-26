from nicegui import ui

def page_a():
    ui.label('Это страница A')
    # Ссылка на страницу B
    ui.link('Перейти на страницу B', '/page-b')

def page_b():
    ui.label('Это страница B')
    # Ссылка обратно на страницу A
    ui.link('Вернуться на страницу A', '/page-a')

@ui.page('/')
def main():
    ui.sub_pages({
        '/page-a': page_a,
        '/page-b': page_b,
        '/': lambda: ui.label('Главная. Выберите страницу.'),
    })

ui.run()