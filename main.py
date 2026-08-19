import flet as ft
from flet import alignment

def main(page: ft.Page):
    page.title = "Calculadora Flet"
    
    # Ajustes de ventana fijos
    page.window.width = 360
    page.window.height = 560
    page.window.resizable = False
    page.window.maximizable = True

    page.bgcolor = "#153056"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    expresion = ""

    # Pantalla de la calculadora
    pantalla = ft.TextField(
        value="0",
        width=304,
        text_align=ft.TextAlign.RIGHT,
        text_size=20,
        read_only=True,
        border=ft.InputBorder.NONE,
        color="#FFFDFE",
        bgcolor="#282D2F",
        border_radius=0,
    )

    def boton_clic(e):
        nonlocal expresion
        # Obtenemos el texto del botón desde el contenido del contenedor
        valor = e.control.content.value

        if valor == "C":
            expresion = ""
            pantalla.value = "0"
        elif valor == "⌫": # <--- NUEVO
            expresion = expresion[:-1]
            pantalla.value = expresion if expresion != "" else "0"
        elif valor == "=":
            try:
                resultado_eval = str(eval(expresion.replace("x", "*").replace("÷", "/")))
                pantalla.value = resultado_eval
                expresion = resultado_eval
            except ZeroDivisionError:
                pantalla.value = "Error: Div / 0"
                expresion = ""
            except Exception:
                pantalla.value = "Error"
                expresion = ""
        else:
            if expresion == "0" or pantalla.value == "Error" or pantalla.value == "Error: Div / 0":
                expresion = ""
            expresion += valor
            pantalla.value = expresion
        
        page.update()

    def crear_boton(texto, color_fondo="#4B4E4F", color_texto=ft.Colors.WHITE):
        return ft.Container(
            content=ft.Text(
                texto, 
                size=20, 
                weight=ft.FontWeight.BOLD, 
                color=color_texto, 
                text_align=ft.TextAlign.CENTER
            ),
            width=70,
            height=70,
            bgcolor=color_fondo,
            on_click=boton_clic,
            border_radius=2
        )

    # Filas de botones
    fila_c = [crear_boton("C", "#FF5252"), crear_boton("(", "#282D2F"), crear_boton(")", "#282D2F"), crear_boton("⌫", "#141066")]
    fila_7 = [crear_boton("7"), crear_boton("8"), crear_boton("9"), crear_boton("÷", "#141066")]
    fila_4 = [crear_boton("4"), crear_boton("5"), crear_boton("6"), crear_boton("x", "#141066")]
    fila_1 = [crear_boton("1"), crear_boton("2"), crear_boton("3"), crear_boton("-", "#141066")]
    fila_0 = [crear_boton("0"), crear_boton("."), crear_boton("=", "#468EED"), crear_boton("+", "#141066")]

    # Contenedor principal de la calculadora
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row(controls=[pantalla], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(controls=fila_c, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                ft.Row(controls=fila_7, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                ft.Row(controls=fila_4, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                ft.Row(controls=fila_1, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                ft.Row(controls=fila_0, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
            ], spacing=8),
            padding=10,
            width=324,
            bgcolor="#000000",
            border_radius=5,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)