# pip install pyautogui
import pyautogui
import time

# -----------------------
# Mouse Positioning
# -----------------------

def move_mouse(x, y):
    """Déplace la souris aux coordonnées (x, y) de l'écran."""
    pyautogui.moveTo(x, y)

def move_mouse_relative(dx, dy):
    """Déplace la souris de manière relative à sa position actuelle."""
    pyautogui.move(dx, dy)

def get_mouse_position():
    """Retourne la position actuelle de la souris (x, y)."""
    position = pyautogui.position()
    print(f"Position actuelle de la souris : {position}")
    return position

# -----------------------
# Mouse Clicks
# -----------------------

def left_click(x=None, y=None):
    """Effectue un clic gauche. Si x et y sont fournis, clique à cette position."""
    if x is not None and y is not None:
        pyautogui.click(x, y)
    else:
        pyautogui.click()

def right_click(x=None, y=None):
    """Effectue un clic droit. Si x et y sont fournis, clique à cette position."""
    if x is not None and y is not None:
        pyautogui.click(x, y, button='right')
    else:
        pyautogui.click(button='right')

def double_click(x=None, y=None):
    """Effectue un double clic gauche. Si x et y sont fournis, clique à cette position."""
    if x is not None and y is not None:
        pyautogui.doubleClick(x, y)
    else:
        pyautogui.doubleClick()

def middle_click(x=None, y=None):
    """Effectue un clic du bouton central. Si x et y sont fournis, clique à cette position."""
    if x is not None and y is not None:
        pyautogui.click(x, y, button='middle')
    else:
        pyautogui.click(button='middle')

# -----------------------
# Mouse Dragging
# -----------------------

def drag_mouse(x, y, duration=0.5):
    """Déplace la souris en cliquant depuis la position actuelle jusqu'à (x, y)."""
    pyautogui.dragTo(x, y, duration=duration, button='left')

def drag_mouse_relative(dx, dy, duration=0.5):
    """Déplace la souris en maintenant le clic depuis la position actuelle de manière relative."""
    pyautogui.dragRel(dx, dy, duration=duration, button='left')

# -----------------------
# Mouse Scrolling
# -----------------------

def scroll_up(amount):
    """Fait défiler la molette vers le haut."""
    pyautogui.scroll(amount)

def scroll_down(amount):
    """Fait défiler la molette vers le bas."""
    pyautogui.scroll(-amount)

