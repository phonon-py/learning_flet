import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()
    new_task = ft.TextField(hint_text="Whats need to be done?")
    # 以下が0行目の処理
    tasks_view = ft.Column()
    # おそらくカラムの設定
    view=ft.Column(
        width=600,
        controls=[
            # カラムの0行目
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                ],    
            ),
            # どこで配置するか？
            tasks_view
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(target=main)