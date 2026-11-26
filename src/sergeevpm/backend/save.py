from aes_bridge import encrypt
from nicegui import ui, app
from pathlib import Path

def save():
    password = app.storage.client["current_password"]
    pre = str(app.storage.client["records"])
    encrypted = encrypt(pre, password)
    Path(app.storage.client["path"]).write_bytes(encrypted)
