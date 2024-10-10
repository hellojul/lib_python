# system_info_utils.py

import platform
import os
import psutil
import socket
import shutil
import time
import uuid

# 1. Function to get the operating system details
# Fonction pour obtenir les détails du système d'exploitation
def get_os_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor()
    }

# 2. Function to get CPU information
# Fonction pour obtenir des informations sur le processeur (CPU)
def get_cpu_info():
    return {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "CPU Frequency": psutil.cpu_freq()._asdict(),
        "CPU Usage Per Core": psutil.cpu_percent(percpu=True),
        "Total CPU Usage": psutil.cpu_percent()
    }

# 3. Function to get memory (RAM) information
# Fonction pour obtenir des informations sur la mémoire (RAM)
def get_memory_info():
    svmem = psutil.virtual_memory()
    return {
        "Total": svmem.total,
        "Available": svmem.available,
        "Used": svmem.used,
        "Percentage": svmem.percent
    }

# 4. Function to get disk usage information
# Fonction pour obtenir des informations sur l'utilisation des disques
def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System Type": partition.fstype,
            "Total Size": usage.total,
            "Used": usage.used,
            "Free": usage.free,
            "Percentage": usage.percent
        })
    return disk_info

# 5. Function to get network information
# Fonction pour obtenir des informations réseau
def get_network_info():
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
                addr_info['Netmask'] = address.netmask
                addr_info['Broadcast MAC'] = address.broadcast
            addresses.append(addr_info)
        
        network_info[interface_name] = {
            "Addresses": addresses,
            "Is Up": if_stats[interface_name].isup,
            "Speed (Mbps)": if_stats[interface_name].speed
        }
    return network_info

# 6. Function to get current user information
# Fonction pour obtenir des informations sur l'utilisateur actuel
def get_user_info():
    return {
        "Username": os.getlogin(),
        "User ID": os.getuid(),
        "Group ID": os.getgid(),
        "Home Directory": os.path.expanduser("~")
    }

# 7. Function to get uptime of the system
# Fonction pour obtenir le temps d'activité (uptime) du système
def get_uptime():
    boot_time_timestamp = psutil.boot_time()
    bt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(boot_time_timestamp))
    return {
        "Boot Time": bt,
        "Uptime (seconds)": time.time() - boot_time_timestamp
    }

# 8. Function to get disk IO statistics
# Fonction pour obtenir des statistiques sur les entrées/sorties du disque
def get_disk_io_info():
    disk_io = psutil.disk_io_counters()
    return {
        "Read Count": disk_io.read_count,
        "Write Count": disk_io.write_count,
        "Read Bytes": disk_io.read_bytes,
        "Write Bytes": disk_io.write_bytes
    }

# 9. Function to get network IO statistics
# Fonction pour obtenir des statistiques sur les entrées/sorties réseau
def get_network_io_info():
    net_io = psutil.net_io_counters()
    return {
        "Bytes Sent": net_io.bytes_sent,
        "Bytes Received": net_io.bytes_recv,
        "Packets Sent": net_io.packets_sent,
        "Packets Received": net_io.packets_recv
    }

# 10. Function to get battery status (if available)
# Fonction pour obtenir le statut de la batterie (si disponible)
def get_battery_info():
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        if battery is not None:
            return {
                "Percentage": battery.percent,
                "Seconds Left": battery.secsleft,
                "Power Plugged In": battery.power_plugged
            }
        else:
            return "Battery information not available"
    return "Battery monitoring not supported"

# 11. Function to get the system's hostname and IP address
# Fonction pour obtenir le nom d'hôte et l'adresse IP du système
def get_host_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "Hostname": hostname,
        "IP Address": ip_address
    }

# 12. Function to get system's MAC address
# Fonction pour obtenir l'adresse MAC du système
def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                    for elements in range(0, 2 * 6, 8)][::-1])
    return mac

# 13. Function to get current running processes
# Fonction pour obtenir la liste des processus en cours d'exécution
def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'status']):
        processes.append(proc.info)
    return processes

# Example usage of the functions
if __name__ == "__main__":
    print("OS Information:", get_os_info())
    print("CPU Information:", get_cpu_info())
    print("Memory Information:", get_memory_info())
    print("Disk Information:", get_disk_info())
    print("Network Information:", get_network_info())
    print("User Information:", get_user_info())
    print("System Uptime:", get_uptime())
    print("Disk IO Information:", get_disk_io_info())
    print("Network IO Information:", get_network_io_info())
    print("Battery Information:", get_battery_info())
    print("Host Information:", get_host_info())
    print("MAC Address:", get_mac_address())
    print("Running Processes:", get_running_processes())

