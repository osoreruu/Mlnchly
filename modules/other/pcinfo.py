import os
import sys
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_infoaboutpc():
    print_banner()
    output_file = "pc_info.txt"
    pc_info = {
        "BIOS Date": "/sys/class/dmi/id/bios_date",
        "BIOS Release": "/sys/class/dmi/id/bios_release",
        "BIOS Vendor": "/sys/class/dmi/id/bios_vendor",
        "BIOS Version": "/sys/class/dmi/id/bios_version",
        "Board Asset Tag": "/sys/class/dmi/id/board_asset_tag",
        "Board Name": "/sys/class/dmi/id/board_name",
        "Board Serial": "/sys/class/dmi/id/board_serial",
        "Board Vendor": "/sys/class/dmi/id/board_vendor",
        "Board Version": "/sys/class/dmi/id/board_version",
        "Chassis Serial": "/sys/class/dmi/id/chassis_serial",
        "Product Serial": "/sys/class/dmi/id/product_serial",
        "Product UUID": "/sys/class/dmi/id/product_uuid"
    }

    collected_data = {}
    
    for name, path in pc_info.items():
        try:
            with open(path, "r", encoding="utf-8") as f:
                collected_data[name] = f.read().strip()
        except PermissionError:
            collected_data[name] = Fore.RED + Style.BRIGHT + "Access Denied (Needs sudo)"
        except FileNotFoundError:
            collected_data[name] = Fore.RED + Style.BRIGHT + "Not Found"
            
    for key, value in collected_data.items():
        print(Fore.CYAN + Style.BRIGHT + f"{key}: {value}")

    with open(output_file, "w", encoding="utf-8") as f:
        for key, value in collected_data.items():
            f.write(f"{key}: {value}\n")

    print(Fore.GREEN + Style.BRIGHT + f"Data successfully saved to file: {output_file}")