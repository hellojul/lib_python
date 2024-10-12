import os
import shutil
from datetime import datetime

class FileManager:
    # === Fonctions pour la manipulation de répertoires ===

    def get_current_directory(self) -> str:
        """
        Retourne le chemin du répertoire de travail actuel.
        """
        return os.getcwd()

    def change_directory(self, path: str) -> None:
        """
        Change le répertoire de travail actuel vers 'path'.
        """
        os.chdir(path)

    def list_directory_contents(self, path: str = ".") -> list:
        """
        Liste le contenu du répertoire spécifié. Si aucun chemin n'est fourni, 
        le répertoire de travail actuel est utilisé.
        """
        return os.listdir(path)

    def create_directory(self, path: str) -> None:
        """
        Crée un nouveau répertoire à l'emplacement spécifié.
        """
        os.mkdir(path)

    def remove_directory(self, path: str) -> None:
        """
        Supprime un répertoire vide.
        """
        os.rmdir(path)

    def create_nested_directories(self, path: str) -> None:
        """
        Crée un ensemble de répertoires imbriqués (ex: 'parent/enfant').
        """
        os.makedirs(path)

    def remove_nested_directories(self, path: str) -> None:
        """
        Supprime un répertoire et tout son contenu de manière récursive.
        """
        shutil.rmtree(path)

    # === Fonctions pour la manipulation de fichiers ===

    def create_empty_file(self, path: str) -> None:
        """
        Crée un fichier vide à l'emplacement spécifié.
        """
        with open(path, 'w') as file:
            pass

    def remove_file(self, path: str) -> None:
        """
        Supprime un fichier à l'emplacement spécifié.
        """
        os.remove(path)

    def rename_file_or_directory(self, old_path: str, new_path: str) -> None:
        """
        Renomme un fichier ou un répertoire.
        """
        os.rename(old_path, new_path)

    def copy_file(self, source: str, destination: str) -> None:
        """
        Copie un fichier de la source vers la destination.
        """
        shutil.copy2(source, destination)

    def move_file(self, source: str, destination: str) -> None:
        """
        Déplace un fichier de la source vers la destination.
        """
        shutil.move(source, destination)

    # === Fonctions d'information sur les fichiers et répertoires ===

    def get_file_size(self, path: str) -> int:
        """
        Retourne la taille du fichier en octets.
        """
        return os.path.getsize(path)

    def get_file_extension(self, path: str) -> str:
        """
        Retourne l'extension du fichier (ex: '.txt', '.jpg').
        """
        return os.path.splitext(path)[1]

    def get_last_modified_time(self, path: str) -> datetime:
        """
        Retourne la date et l'heure de la dernière modification du fichier ou répertoire.
        """
        timestamp = os.path.getmtime(path)
        return datetime.fromtimestamp(timestamp)

    def is_file(self, path: str) -> bool:
        """
        Vérifie si le chemin correspond à un fichier.
        """
        return os.path.isfile(path)

    def is_directory(self, path: str) -> bool:
        """
        Vérifie si le chemin correspond à un répertoire.
        """
        return os.path.isdir(path)

    def file_exists(self, path: str) -> bool:
        """
        Vérifie si un fichier ou un répertoire existe à l'emplacement spécifié.
        """
        return os.path.exists(path)

    def directory_exists(self, path: str) -> bool:
        """
        Vérifie si un répertoire existe à l'emplacement spécifié.
        """
        return os.path.isdir(path)

    # === Fonctions sur les chemins de fichiers ===

    def get_absolute_path(self, path: str) -> str:
        """
        Retourne le chemin absolu pour un chemin donné.
        """
        return os.path.abspath(path)

    def join_paths(self, *paths: str) -> str:
        """
        Concatène plusieurs chemins de manière sécurisée (selon le système d'exploitation).
        """
        return os.path.join(*paths)

    def split_path(self, path: str) -> tuple:
        """
        Sépare un chemin en (répertoire, nom de fichier).
        """
        return os.path.split(path)

    def get_basename(self, path: str) -> str:
        """
        Retourne le nom du fichier ou du répertoire à partir d'un chemin complet.
        """
        return os.path.basename(path)

    def get_dirname(self, path: str) -> str:
        """
        Retourne le nom du répertoire parent à partir d'un chemin complet.
        """
        return os.path.dirname(path)

    # === Informations sur l'environnement système ===

    def get_environment_variable(self, var: str) -> str:
        """
        Retourne la valeur d'une variable d'environnement.
        """
        return os.getenv(var)

    def set_environment_variable(self, var: str, value: str) -> None:
        """
        Définit une variable d'environnement avec la valeur spécifiée.
        """
        os.environ[var] = value

    def get_user_home_directory(self) -> str:
        """
        Retourne le répertoire personnel de l'utilisateur actuel.
        """
        return os.path.expanduser("~")

    def get_temp_directory(self) -> str:
        """
        Retourne le chemin du répertoire temporaire du système.
        """
        return os.path.gettempdir()

    def get_platform_name(self) -> str:
        """
        Retourne le nom du système d'exploitation (ex: 'posix', 'nt').
        """
        return os.name

    # === Fonctions supplémentaires utiles ===

    def copy_directory(self, source: str, destination: str) -> None:
        """
        Copie un répertoire et tout son contenu de la source vers la destination.
        """
        shutil.copytree(source, destination)

    def archive_directory(self, source: str, archive_name: str) -> str:
        """
        Crée une archive ZIP du répertoire spécifié et la nomme comme défini.
        """
        return shutil.make_archive(archive_name, 'zip', source)

    def extract_archive(self, archive_path: str, destination: str) -> None:
        """
        Extrait le contenu d'une archive vers le répertoire de destination.
        """
        shutil.unpack_archive(archive_path, destination)

    def get_directory_size(self, path: str) -> int:
        """
        Calcule la taille totale du répertoire en parcourant récursivement son contenu.
        """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def search_files_by_extension(self, directory: str, extension: str) -> list:
        """
        Recherche tous les fichiers d'un répertoire ayant une extension spécifique.
        """
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if f.endswith(extension)]

