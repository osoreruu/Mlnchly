import uuid
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_uuid_gnrtr():
	print_banner()
	while True:
		try:
			count = int(input(Fore.CYAN + Style.BRIGHT + "Type number of UUIDs: "))
			if count <= 0:
				print(Fore.RED + Style.BRIGHT + "Write number greater than 0.")
				continue
			for _ in range(count):
				print(Fore.GREEN + Style.BRIGHT + str(uuid.uuid4()))
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Write number, not text.")	