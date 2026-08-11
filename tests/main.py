"""
Dự án này được tạo ra để chúc mừng sinh nhật một cô gái hết sức tuyệt vời
Đó là Chị Huong Le
Được tạo bởi Man Ly
"""
import flet as ft

def main(page: ft.Page):
    page.title = "Main Screen"
    page.window.height = 600
    page.window.width = 600
    message = "Happy Birthday, Chị Hương"

    first_display = ft.Text( message, size =18)
    page.add(first_display)

if __name__ == "__main__":
    ft.run(main)
