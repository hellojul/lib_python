import os
import shutil
from datetime import datetime

class FileManager:
    # === Fonctions pour la manipulation de répertoires ===

    def get_current_directory(self) -> str:
        return os.getcwd()

    def change_directory(self, path: str) -> None:
        os.chdir(path)

    def list_directory_contents(self, path: str = ".") -> list:
        return os.listdir(path)

    def create_directory(self, path: str) -> None:
        os.mkdir(path)

    def remove_directory(self, path: str) -> None:
        os.rmdir(path)

    def create_nested_directories(self, path: str) -> None:
        os.makedirs(path)

    def remove_nested_directories(self, path: str) -> None:
        shutil.rmtree(path)

    # === Fonctions pour la manipulation de fichiers ===

    def create_empty_file(self, path: str) -> None:
        with open(path, 'w') as file:
            pass

    def remove_file(self, path: str) -> None:
        os.remove(path)

    def rename_file_or_directory(self, old_path: str, new_path: str) -> None:
        os.rename(old_path, new_path)

    def copy_file(self, source: str, destination: str) -> None:
        shutil.copy2(source, destination)

    def move_file(self, source: str, destination: str) -> None:
        shutil.move(source, destination)

    # === Fonctions d'information sur les fichiers et répertoires ===

    def get_file_size(self, path: str) -> int:
        return os.path.getsize(path)

    def get_file_extension(self, path: str) -> str:
        return os.path.splitext(path)[1]

    def get_last_modified_time(self, path: str) -> datetime:
        timestamp = os.path.getmtime(path)
        return datetime.fromtimestamp(timestamp)

    def is_file(self, path: str) -> bool:
        return os.path.isfile(path)

    def is_directory(self, path: str) -> bool:
        return os.path.isdir(path)

    def file_exists(self, path: str) -> bool:
        return os.path.exists(path)

    def directory_exists(self, path: str) -> bool:
        return os.path.isdir(path)

    # === Fonctions sur les chemins de fichiers ===

    def get_absolute_path(self, path: str) -> str:
        return os.path.abspath(path)

    def join_paths(self, *paths: str) -> str:
        return os.path.join(*paths)

    def split_path(self, path: str) -> tuple:
        return os.path.split(path)

    def get_basename(self, path: str) -> str:
        return os.path.basename(path)

    def get_dirname(self, path: str) -> str:
        return os.path.dirname(path)

    # === Informations sur l'environnement système ===

    def get_environment_variable(self, var: str) -> str:
        return os.getenv(var)

    def set_environment_variable(self, var: str, value: str) -> None:
        os.environ[var] = value

    def get_user_home_directory(self) -> str:
        return os.path.expanduser("~")

    def get_temp_directory(self) -> str:
        return os.path.gettempdir()

    def get_platform_name(self) -> str:
        return os.name

    # === Fonctions supplémentaires utiles ===

    def copy_directory(self, source: str, destination: str) -> None:
        shutil.copytree(source, destination)

    def archive_directory(self, source: str, archive_name: str) -> str:
        return shutil.make_archive(archive_name, 'zip', source)

    def extract_archive(self, archive_path: str, destination: str) -> None:
        shutil.unpack_archive(archive_path, destination)

    def get_directory_size(self, path: str) -> int:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def search_files_by_extension(self, directory: str, extension: str) -> list:
        return [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if f.endswith(extension)]

