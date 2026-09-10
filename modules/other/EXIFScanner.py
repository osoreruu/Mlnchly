from PIL import Image
import os
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

init(autoreset=True)

def run_EXIF_scan():
	print_banner()
	path = input(Fore.CYAN + Style.BRIGHT + "Enter the path to the image: ").strip()
	
	if not os.path.exists(path):
		print(Fore.RED + Style.BRIGHT + f"File not found: {path}")
		return

	try:
		image = Image.open(path)
		exif = image.getexif()

		if not exif:
			print(Fore.RED + Style.BRIGHT + "Exif not found")
			return

		for tag_id, value in exif.items():
			print(Fore.CYAN + Style.BRIGHT + f"Tag [{tag_id}]: {value}")

	except Exception as e:
		print(Fore.RED + Style.BRIGHT + f"Error: {e}")