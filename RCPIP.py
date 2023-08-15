import requests
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Obtener la IP pública
def get_public_ip():
    try:
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        return data['ip']
    except Exception as e:
        return str(e)

# Copiar la IP al portapapeles
def copy_to_clipboard(ip):
    root.clipboard_clear()
    root.clipboard_append(ip)
    root.update()

# Crear la interfaz gráfica
root = tk.Tk()
root.title('RCPIP')

bg_image = Image.open('background.png')
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

ip_frame = tk.Frame(root, bg='#ffffff', bd=5)
ip_frame.place(relx=0.5, rely=0.5, anchor='center')

font_title = ('Montserrat', 24, 'bold')
title_label = tk.Label(ip_frame, text='RCPIP', bg='#ffffff', font=font_title)
title_label.pack()

font_style = ('Lato', 14)

ip_value = tk.Label(ip_frame, text=get_public_ip(), bg='#ffffff', font=font_style)
ip_value.pack()

copy_button = tk.Button(ip_frame, text='Copiar al Portapapeles', bg='#66ccff', fg='white', font=('Helvetica', 10), command=lambda: copy_to_clipboard(ip_value.cget('text')))
copy_button.pack(pady=10)

exit_button = tk.Button(ip_frame, text='Salir', bg='#66ccff', fg='white', font=('Helvetica', 10), command=root.quit)
exit_button.pack()

root.mainloop()
