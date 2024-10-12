import platform
import os
import psutil
import socket
import shutil
import time
import uuid
import json
import math

class SystemInfo:
    """
    Classe pour gérer et afficher les informations du système, du CPU, de la mémoire, du disque,
    du réseau et d'autres statistiques liées au système.
    """

    @staticmethod
    def get_os_info():
        """
        Retourne les détails du système d'exploitation.
        """
        return {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "OS Release": platform.release(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }

    @staticmethod
    def get_cpu_info():
        """
        Retourne les informations sur le processeur (CPU).
        """
        return {
            "Physical Cores": psutil.cpu_count(logical=False),
            "Total Cores": psutil.cpu_count(logical=True),
            "CPU Frequency": psutil.cpu_freq()._asdict(),
            "CPU Usage Per Core": psutil.cpu_percent(percpu=True),
            "Total CPU Usage": psutil.cpu_percent(interval=1)
        }

    @staticmethod
    def get_memory_info():
        """
        Retourne les informations sur la mémoire RAM.
        """
        svmem = psutil.virtual_memory()
        return {
            "Total": SystemInfo.convert_size(svmem.total),
            "Available": SystemInfo.convert_size(svmem.available),
            "Used": SystemInfo.convert_size(svmem.used),
            "Percentage": f"{svmem.percent}%"
        }

    @staticmethod
    def get_disk_info():
        """
        Retourne les informations sur l'utilisation des disques.
        """
        partitions = psutil.disk_partitions()
        disk_info = []
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "Device": partition.device,
                "Mountpoint": partition.mountpoint,
                "File System Type": partition.fstype,
                "Total Size": SystemInfo.convert_size(usage.total),
                "Used": SystemInfo.convert_size(usage.used),
                "Free": SystemInfo.convert_size(usage.free),
                "Percentage": f"{usage.percent}%"
            })
        return disk_info

    @staticmethod
    def get_network_info():
        """
        Retourne les informations réseau (interfaces et statistiques).
        """
        if_addrs = psutil.net_if_addrs()
        if_stats = psutil.net_if_stats()
        network_info = {}
        for interface_name, interface_addresses in if_addrs.items():
            addresses = []
            for address in interface_addresses:
                addr_info = {}
                if str(address.family) == 'AddressFamily.AF_INET':
                    addr_info['IP Address'] = address.address
                    addr_info['Netmask'] = address.netmask
                    addr_info['Broadcast IP'] = address.broadcast
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    addr_info['MAC Address'] = address.address
                addresses.append(addr_info)
            network_info[interface_name] = {
                "Addresses": addresses,
                "Is Up": if_stats[interface_name].isup,
                "Speed (Mbps)": if_stats[interface_name].speed
            }
        return network_info

    @staticmethod
    def get_user_info():
        """
        Retourne les informations sur l'utilisateur actuel.
        """
        return {
            "Username": os.getlogin(),
            "User ID": os.getuid(),
            "Group ID": os.getgid(),
            "Home Directory": os.path.expanduser("~")
        }

    @staticmethod
    def get_uptime():
        """
        Retourne le temps d'activité du système (uptime).
        """
        boot_time_timestamp = psutil.boot_time()
        bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time_timestamp))
        uptime_seconds = time.time() - boot_time_timestamp
        uptime_formatted = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
        return {
            "Boot Time": bt,
            "Uptime (formatted)": uptime_formatted,
            "Uptime (seconds)": uptime_seconds
        }

    @staticmethod
    def get_disk_io_info():
        """
        Retourne les statistiques d'entrées/sorties des disques.
        """
        disk_io = psutil.disk_io_counters()
        return {
            "Read Count": disk_io.read_count,
            "Write Count": disk_io.write_count,
            "Read Bytes": SystemInfo.convert_size(disk_io.read_bytes),
            "Write Bytes": SystemInfo.convert_size(disk_io.write_bytes)
        }

    @staticmethod
    def get_network_io_info():
        """
        Retourne les statistiques d'entrées/sorties réseau.
        """
        net_io = psutil.net_io_counters()
        return {
            "Bytes Sent": SystemInfo.convert_size(net_io.bytes_sent),
            "Bytes Received": SystemInfo.convert_size(net_io.bytes_recv),
            "Packets Sent": net_io.packets_sent,
            "Packets Received": net_io.packets_recv
        }

    @staticmethod
    def get_battery_info():
        """
        Retourne les informations sur la batterie (si disponible).
        """
        if hasattr(psutil, "sensors_battery"):
            battery = psutil.sensors_battery()
            if battery is not None:
                return {
                    "Percentage": f"{battery.percent}%",
                    "Seconds Left": battery.secsleft,
                    "Power Plugged In": battery.power_plugged
                }
            else:
                return "Battery information not available"
        return "Battery monitoring not supported"

    @staticmethod
    def get_host_info():
        """
        Retourne le nom d'hôte et l'adresse IP du système.
        """
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return {
            "Hostname": hostname,
            "IP Address": ip_address
        }

    @staticmethod
    def get_mac_address():
        """
        Retourne l'adresse MAC du système.
        """
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                        for elements in range(0, 2 * 6, 8)][::-1])
        return mac

    @staticmethod
    def get_running_processes():
        """
        Retourne la liste des processus en cours d'exécution.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status']):
            processes.append(proc.info)
        return processes

    # === Fonctions utilitaires ===

    @staticmethod
    def convert_size(size_bytes):
        """
        Convertit une taille en octets en une chaîne lisible (Ko, Mo, Go, etc.).
        """
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_name[i]}"

    @staticmethod
    def display_json(data):
        """
        Affiche les données dans un format JSON lisible pour la console.
        """
        print(json.dumps(data, indent=4, ensure_ascii=False))


# Exemple d'utilisation de la classe SystemInfo
if __name__ == "__main__":
    print("\nOS Information:")
    SystemInfo.display_json(SystemInfo.get_os_info())

    print("\nCPU Information:")
    SystemInfo.display_json(SystemInfo.get_cpu_info())

    print("\nMemory Information:")
    SystemInfo.display_json(SystemInfo.get_memory_info())

    print("\nDisk Information:")
    SystemInfo.display_json(SystemInfo.get_disk_info())

    print("\nNetwork Information:")
    SystemInfo.display_json(SystemInfo.get_network_info())

    print("\nUser Information:")
    SystemInfo.display_json(SystemInfo.get_user_info())

    print("\nSystem Uptime:")
    SystemInfo.display_json(SystemInfo.get_uptime())

    print("\nDisk IO Information:")
    SystemInfo.display_json(SystemInfo.get_disk_io_info())

    print("\nNetwork IO Information:")
    SystemInfo.display_json(SystemInfo.get_network_io_info())

    print("\nBattery Information:")
    SystemInfo.display_json(SystemInfo.get_battery_info())

    print("\nHost Information:")
    SystemInfo.display_json(SystemInfo.get_host_info())

    print("\nMAC Address:")
    print(SystemInfo.get_mac_address())

    print("\nRunning Processes:")
    SystemInfo.display_json(SystemInfo.get_running_processes())

