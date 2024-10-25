# apt install xdotool
import os
import subprocess

# -----------------------
# Gestion des fenêtres
# -----------------------

def switch_window():
    """Bascule entre les fenêtres ouvertes (Alt+Tab)."""
    os.system("xdotool key alt+Tab")

def minimize_window():
    """Minimise la fenêtre actuelle (Ctrl+Super+D)."""
    os.system("xdotool key ctrl+super+d")

def maximize_window():
    """Maximise ou restaure la fenêtre actuelle (Super+Up)."""
    os.system("xdotool key super+Up")

def close_window():
    """Ferme la fenêtre actuelle (Alt+F4)."""
    os.system("xdotool key alt+F4")

def show_desktop():
    """Réduit toutes les fenêtres pour afficher le bureau (Super+D)."""
    os.system("xdotool key super+d")

def restore_all_windows():
    """Restaure toutes les fenêtres réduites (Super+D)."""
    os.system("xdotool key super+d")

def toggle_fullscreen():
    """Passe la fenêtre actuelle en plein écran ou annule (F11)."""
    os.system("xdotool key F11")

def align_window_left():
    """Aligne la fenêtre active à gauche de l’écran (Super+Left)."""
    os.system("xdotool key super+Left")

def align_window_right():
    """Aligne la fenêtre active à droite de l’écran (Super+Right)."""
    os.system("xdotool key super+Right")

# -----------------------
# Contrôle de Firefox
# -----------------------

def open_new_tab():
    """Ouvre un nouvel onglet dans Firefox (Ctrl+T)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+t")

def close_tab():
    """Ferme l'onglet actuel dans Firefox (Ctrl+W)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+w")

def refresh_page():
    """Actualise la page dans Firefox (Ctrl+R)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+r")

def search_text():
    """Ouvre la barre de recherche dans Firefox (Ctrl+F)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+f")

def next_tab():
    """Bascule vers l'onglet suivant dans Firefox (Ctrl+Tab)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+Tab")

def previous_tab():
    """Bascule vers l'onglet précédent dans Firefox (Ctrl+Shift+Tab)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+shift+Tab")

def open_private_window():
    """Ouvre une nouvelle fenêtre privée dans Firefox (Ctrl+Shift+P)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+shift+p")

def open_downloads():
    """Ouvre la page de téléchargements dans Firefox (Ctrl+J)."""
    os.system("xdotool search --onlyvisible --class Firefox windowactivate key ctrl+j")

# -----------------------
# Commandes système
# -----------------------

def open_terminal():
    """Ouvre un nouveau terminal (Ctrl+Alt+T)."""
    os.system("xdotool key ctrl+alt+t")

def lock_screen():
    """Verrouille l'écran (Super+L)."""
    os.system("xdotool key super+l")

def take_screenshot():
    """Effectue une capture d'écran (PrintScreen)."""
    os.system("xdotool key Print")

def open_file_manager():
    """Ouvre le gestionnaire de fichiers (Super+E)."""
    os.system("xdotool key super+e")

def show_notification_center():
    """Affiche le centre de notifications (Super+N)."""
    os.system("xdotool key super+n")

def open_settings():
    """Ouvre les paramètres système (Super+S)."""
    os.system("xdotool key super+s")

def vopen_calculator():
    """Ouvre la calculatrice (Ctrl+Alt+C)."""
    os.system("xdotool key ctrl+alt+c")

def open_task_manager():
    """Ouvre le gestionnaire des tâches (Ctrl+Shift+Esc)."""
    os.system("xdotool key ctrl+shift+Escape")

# -----------------------
# Contrôle multimédia
# -----------------------

def volume_up():
    """Augmente le volume (Volume Up)."""
    os.system("xdotool key XF86AudioRaiseVolume")

def volume_down():
    """Diminue le volume (Volume Down)."""
    os.system("xdotool key XF86AudioLowerVolume")

def mute():
    """Coupe le son (Mute)."""
    os.system("xdotool key XF86AudioMute")

def play_pause():
    """Met en lecture/pause le média en cours (Play/Pause)."""
    os.system("xdotool key XF86AudioPlay")

def next_track():
    """Passe au morceau suivant (Next)."""
    os.system("xdotool key XF86AudioNext")

def previous_track():
    """Revient au morceau précédent (Previous)."""
    os.system("xdotool key XF86AudioPrev")

def stop_media():
    """Arrête la lecture du média en cours (Stop)."""
    os.system("xdotool key XF86AudioStop")

# -----------------------
# Lancement d'applications
# -----------------------

def launch_application(app_name):
    """Lance une application en utilisant son nom de commande."""
    try:
        subprocess.Popen(app_name)
        print(f"Lancement de {app_name}")
    except FileNotFoundError:
        print(f"L'application '{app_name}' est introuvable.")

