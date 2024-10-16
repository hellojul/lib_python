import subprocess

# Fonction pour exécuter une commande bash et obtenir sa sortie
def execute_command(command):
    """
    Exécute une commande bash et retourne sa sortie sous forme de chaîne.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

# Fonction pour exécuter une commande bash et obtenir à la fois stdout et stderr
def execute_command_full(command):
    """
    Exécute une commande bash et retourne à la fois stdout et stderr.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip(), result.stderr.strip()

# Fonction pour vérifier si une commande existe sur le système
def command_exists(command):
    """
    Vérifie si une commande bash donnée existe sur le système.
    """
    result = subprocess.run(f'which {command}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

# Fonction pour exécuter une commande bash sans attendre qu'elle se termine (asynchrone)
def execute_command_async(command):
    """
    Exécute une commande bash de manière asynchrone sans attendre sa fin.
    """
    subprocess.Popen(command, shell=True)

# Fonction pour capturer la sortie d'une commande en temps réel
def execute_command_realtime(command):
    """
    Exécute une commande bash et diffuse sa sortie ligne par ligne en temps réel.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end='')

# Fonction pour obtenir le code de sortie d'une commande bash
def get_command_exit_code(command):
    """
    Exécute une commande bash et retourne son code de sortie.
    """
    result = subprocess.run(command, shell=True)
    return result.returncode

# Fonction pour exécuter une commande avec des variables d'environnement personnalisées
def execute_command_with_env(command, env_vars):
    """
    Exécute une commande bash avec des variables d'environnement personnalisées.
    `env_vars` doit être un dictionnaire de variables d'environnement.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env_vars)
    return result.stdout.strip()

def execute_command_to_file(command, output_file):
    """
    Exécute une commande bash et redirige sa sortie vers un fichier.
    """
    with open(output_file, 'w') as file:
        result = subprocess.run(command, shell=True, stdout=file, stderr=subprocess.PIPE, text=True)
    return result.returncode

def execute_commands_in_sequence(commands):
    """
    Exécute une liste de commandes bash en séquence.
    """
    results = {}
    for command in commands:
        exit_code = execute_command(command)
        results[command] = exit_code
    return results

def get_command_path(command):
    """
    Récupère le chemin d'installation d'une commande bash.
    """
    result = subprocess.run(f'which {command}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None



