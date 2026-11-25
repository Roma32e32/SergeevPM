from nicegui import ui
from gui.home import home
from gui.open_pwm import open_pwm
from gui.password_manager import password_manager
from gui.header import nav

@ui.page('/')
def layout():
    nav()
    ui.sub_pages({
        '/' : home,
        '/open': open_pwm,
        '/pm': password_manager,
    })

ui.run(native=True)
