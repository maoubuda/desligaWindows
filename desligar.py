import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()

texto = tk.StringVar()

# store value
value = tk.StringVar(value="0")

tempo = int(value.get())

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Desligar PC')


def quitting():
    # stoping shutdown
    os.system(f"shutdown -a")
    # closing app
    root.destroy()


def create_interface_2(tempo):
    global texto
    texto.set(f"Tempo até desligar : {tempo} segundos")
    cd = ttk.Label(textvariable=texto)
    cd.pack(padx=5, pady=5)
    stop_button.pack(fill=tk.X, expand=True, pady=10)
    cd.after(1000, lambda: counting_down())


# Here goes the shutdown
def shutdown_act(e):
    global value
    global tempo
    tempo = int(value.get())
    if e == "Segundos":
        tempo = tempo
        all_forget()
        os.system(f"shutdown -s -t {tempo}")
        create_interface_2(tempo)
    elif e == "Minutos":
        tempo = tempo*60
        all_forget()
        os.system(f"shutdown -s -t {tempo}")
        create_interface_2(tempo)
    elif e == "Horas":
        tempo = tempo*3600
        all_forget()
        os.system(f"shutdown -s -t {tempo}")
        create_interface_2(tempo)

# unpack old screen


def all_forget():
    label.pack_forget()
    type_cb.pack_forget()
    value_label.pack_forget()
    value_entry.pack_forget()
    action_button.pack_forget()

# contador


def counting_down():
    global texto
    global tempo
    texto.set(f"Tempo até desligar : {tempo} segundos")
    tempo = tempo - 1
    cd.after(1000, lambda: counting_down())


# label
label = ttk.Label(text="Por Favor Escolha o Tipo:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_type = tk.StringVar()
type_cb = ttk.Combobox(root, textvariable=selected_type)

# values on combobox
type_cb['values'] = ["Segundos", "Minutos", "Horas"]

# prevent typing a value
type_cb['state'] = 'readonly'

# place the widget
type_cb.pack(fill=tk.X, padx=5, pady=5)

# value
value_label = ttk.Label(root, text="Valor :")
value_label.pack(fill=tk.X, expand=True)

value_entry = ttk.Entry(root, textvariable=value)
value_entry.pack(fill=tk.X, expand=True)
value_entry.focus()

# action button
action_button = ttk.Button(root, text="Confirmar",
                           command=lambda: shutdown_act(selected_type.get()))
action_button.pack(fill=tk.X, expand=True, pady=10)

# label contadora
texto.set("")
cd = ttk.Label(textvariable=texto)

# stop button
stop_button = ttk.Button(root, text="Parar",
                         command=lambda: quitting())

root.mainloop()
