import flet as ft

def main(page: ft.Page):
    t = ft.Text(value="Hello World")
    # page.controls.append(t)
    # page.update()
    # 上2行の処理を短縮
    page.add(t)
ft.app(target=main)