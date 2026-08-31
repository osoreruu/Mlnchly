import os
import sys
import hashlib
from pathlib import Path
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_HWIDGnrtr():
	print_banner()
	output_file = "pc_info.txt"
	pc_info = {
		"Board Serial": "/sys/class/dmi/id/board_serial",
		"Product Serial": "/sys/class/dmi/id/product_serial",
		"Product UUID": "/sys/class/dmi/id/product_uuid"
	}

	collected_data = {}
	hwid_components = []
	
	for name, path in pc_info.items():
		try:
			with open(path, "r", encoding="utf-8") as f:
				val = f.read().strip()
				collected_data[name] = val
				if val and not val.lower().startswith("to be filled"):
					hwid_components.append(val)
		except PermissionError:
			collected_data[name] = Fore.RED + Style.BRIGHT + "Access Denied (Needs sudo)"
		except FileNotFoundError:
			collected_data[name] = Fore.RED + Style.BRIGHT + "Not Found"
			
	if hwid_components:
		raw_hwid = "|".join(hwid_components)
		generated_hwid = hashlib.sha256(raw_hwid.encode("utf-8")).hexdigest()
	else:
		generated_hwid = "Unable to generate (No valid data / No permissions)"

	for key, value in collected_data.items():
		print(Fore.CYAN + Style.BRIGHT + f"{key}: {value}")
	
	print(Fore.GREEN + Style.BRIGHT + f"Generated HWID: {generated_hwid}")

	with open(output_file, "w", encoding="utf-8") as f:
		for key, value in collected_data.items():
			clean_value = value
			for color in [Fore.RED, Style.BRIGHT]:
				clean_value = clean_value.replace(color, "")
			f.write(f"{key}: {clean_value} | ")
		f.write(f"Generated HWID: {generated_hwid}")

	print(Fore.GREEN + Style.BRIGHT + f"Data successfully saved to file: {output_file}")