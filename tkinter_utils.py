import tkinter as tk
from tkinter import messagebox, colorchooser

# --- 1. Fonctions pour configurer la fenêtre principale ---
def create_main_window(title="Application Tkinter", width=800, height=600):
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(bg="lightgray")
    return window

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# --- 2. Fonctions pour gérer les couleurs ---
def choose_color():
    color = colorchooser.askcolor(title="Choisissez une couleur")
    return color[1] if color else None

# --- 3. Fonctions pour créer des menus ---
def create_menu(window, menu_structure):
    menubar = tk.Menu(window)
    for menu_name, commands in menu_structure.items():
        menu = tk.Menu(menubar, tearoff=0)
        for label, command in commands:
            menu.add_command(label=label, command=command)
        menubar.add_cascade(label=menu_name, menu=menu)
    window.config(menu=menubar)

# --- 4. Fonctions pour créer des widgets avancés ---
def create_spinbox(parent, from_=0, to=10, font=("Arial", 12)):
    spinbox = tk.Spinbox(parent, from_=from_, to=to, font=font)
    spinbox.pack(pady=5)
    return spinbox

def create_slider(parent, from_=0, to=100, orient=tk.HORIZONTAL, length=200):
    slider = tk.Scale(parent, from_=from_, to=to, orient=orient, length=length)
    slider.pack(pady=5)
    return slider

def create_canvas(parent, width=200, height=200, bg="white"):
    canvas = tk.Canvas(parent, width=width, height=height, bg=bg)
    canvas.pack(pady=10)
    return canvas

# --- 5. Fonctions de mise en page ---
def pack_widgets(widgets, side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5):
    for widget in widgets:
        widget.pack(side=side, fill=fill, expand=expand, padx=padx, pady=pady)

def grid_widgets(widgets, start_row=0, start_column=0):
    for i, widget in enumerate(widgets):
        row = start_row + i // 3
        col = start_column + i % 3
        widget.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# --- 6. Fonctions pour le Canvas ---
def draw_rectangle(canvas, x1, y1, x2, y2, fill="blue", outline="black"):
    return canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)

def draw_circle(canvas, x, y, radius, fill="green", outline="black"):
    return canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=fill, outline=outline)

# --- 7. Fonctions pour les animations ---
def animate_color(widget, colors, delay=500):
    def change_color(index):
        widget.config(bg=colors[index % len(colors)])
        widget.after(delay, change_color, index + 1)
    change_color(0)

def move_widget(widget, x_change, y_change, steps=50, delay=20):
    def move_step(step):
        if step < steps:
            widget.place(x=widget.winfo_x() + x_change, y=widget.winfo_y() + y_change)
            widget.after(delay, move_step, step + 1)
    move_step(0)

# --- 8. Fonctions supplémentaires ---
def clear_canvas(canvas):
    canvas.delete("all")

def show_message_box(title="Message", message="Contenu du message", msg_type="info"):
    if msg_type == "info":
        messagebox.showinfo(title, message)
    elif msg_type == "warning":
        messagebox.showwarning(title, message)
    elif msg_type == "error":
        messagebox.showerror(title, message)

def create_sample_app():
    window = create_main_window("Application Tkinter Avancée", 500, 400)
    center_window(window)

    menu_structure = {
        "Fichier": [("Ouvrir", lambda: show_message_box("Info", "Ouvrir fichier")),
                    ("Quitter", window.quit)],
        "Aide": [("À propos", lambda: show_message_box("À propos", "Application Tkinter"))]
    }
    create_menu(window, menu_structure)

    # Création de widgets
    label = tk.Label(window, text="Animations et Widgets", font=("Arial", 16), bg="lightblue")
    button = tk.Button(window, text="Change Color", command=lambda: animate_color(label, ["lightblue", "lightgreen", "lightcoral"]))
    canvas = create_canvas(window, 200, 100)
    spinbox = create_spinbox(window, 0, 10)
    slider = create_slider(window, 0, 100)

    # Mise en page
    widgets = [label, button, spinbox, slider, canvas]
    pack_widgets(widgets)

    # Dessiner sur le canevas
    draw_rectangle(canvas, 10, 10, 100, 60, fill="red")
    draw_circle(canvas, 150, 50, 30, fill="blue")

    # Animation du bouton
    move_widget(button, 5, 5)

    window.mainloop()

