import os
import platform
import psutil
import getpass
import wmi
import winreg
from datetime import datetime

def get_processor():
    return platform.processor()

def get_device_name():
    return platform.node()

def get_installed_ram():
    ram_bytes = psutil.virtual_memory().total
    ram_gb = round(ram_bytes / (1024 ** 3), 2)
    return f"{ram_gb} GB"

def get_storage():
    partitions = psutil.disk_partitions()
    storage_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total_gb = round(usage.total / (1024 ** 3), 2)
            storage_info.append(f"{partition.device}: {total_gb} GB")
        except PermissionError:
            continue
    return storage_info

def get_graphics_card():
    c = wmi.WMI()
    gpus = c.Win32_VideoController()
    return [gpu.Name for gpu in gpus]

def get_current_user():
    return getpass.getuser()

def get_windows_specifications():
    specs = {
        "Edition": "N/A",
        "Version": "N/A",
        "Installed on": "N/A",
        "OS build": "N/A"
    }

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
            specs["Edition"] = winreg.QueryValueEx(key, "ProductName")[0]
            specs["Version"] = winreg.QueryValueEx(key, "DisplayVersion")[0]
            build = winreg.QueryValueEx(key, "CurrentBuildNumber")[0]
            ubr = winreg.QueryValueEx(key, "UBR")[0]  
            specs["OS build"] = f"{build}.{ubr}"

            install_date_raw = winreg.QueryValueEx(key, "InstallDate")[0]
            install_date = datetime.fromtimestamp(install_date_raw).strftime("%d-%m-%Y")
            specs["Installed on"] = install_date
    except Exception as e:
        specs["Error"] = str(e)

    return specs

def get_installed_software_registry():
    software_list = []
    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    ]

    hives = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]

    for hive in hives:
        for path in reg_paths:
            try:
                reg_key = winreg.OpenKey(hive, path)
                for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
                    try:
                        sub_key_name = winreg.EnumKey(reg_key, i)
                        sub_key = winreg.OpenKey(reg_key, sub_key_name)
                        name, version = None, None
                        try:
                            name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
                        except FileNotFoundError:
                            continue
                        try:
                            version = winreg.QueryValueEx(sub_key, "DisplayVersion")[0]
                        except FileNotFoundError:
                            version = "N/A"
                        if name:
                            software_list.append((name, version))
                    except Exception:
                        continue
            except Exception:
                continue
    return software_list

def save_to_txt():
    lines = []
    lines.append("--- System Information ---\n")
    lines.append(f"Processor         {get_processor()}")
    lines.append(f"Full Device Name  {get_device_name()}")
    lines.append(f"Installed RAM     {get_installed_ram()}")

    lines.append("\nStorage:")
    for s in get_storage():
        lines.append(f"  {s}")

    lines.append("\nGraphics Card:")
    for gpu in get_graphics_card():
        lines.append(f"  {gpu}")

    lines.append(f"\nCurrent User      {get_current_user()}")

    lines.append("\n--- Windows Specifications ---")
    specs = get_windows_specifications()
    for k in ["Edition", "Version", "Installed on", "OS build"]:
        lines.append(f"{k:<15} {specs.get(k, 'N/A')}")

    lines.append("\n--- Installed Software ---\n")
    software_list = get_installed_software_registry()
    for name, version in sorted(software_list):
        lines.append(f"{name} - {version}")

    output_file = "system_info.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"\n System report saved to: {output_file}")

if __name__ == "__main__":
    save_to_txt()
