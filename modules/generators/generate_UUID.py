import uuid
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_uuid_generator():
	print_banner()
	while True:
		try:
			count = int(input(Fore.CYAN + Style.BRIGHT + "Type number of UUIDs: "))
			if count <= 0:
				print(Fore.RED + Style.BRIGHT + "Write number greater than 0.")
				continue
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Write number, not text.")
	with open("output/UUIDs.txt", "w", encoding="utf-8") as f:
		for _ in range(count + 1):
			f.write(str(uuid.uuid4()) + "\n")

	print(Fore.GREEN + Style.BRIGHT + f"{count} UUIDs Generated!")