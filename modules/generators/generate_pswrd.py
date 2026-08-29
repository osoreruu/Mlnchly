from colorama import init, Fore, Style
from modules.ui.ui import print_banner
import string
import secrets

init(autoreset=True)

def run_genpswrd():
	print_banner()
	alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-="

	while True:
		try:
			length = int(input(Fore.CYAN + Style.BRIGHT + "Write a length of password: "))
			if length > 0:
				break
			print(Fore.RED + Style.BRIGHT + "Length must be greater than 0!")
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Write a number!")

	password = "".join(secrets.choice(alphabet) for _ in range(length))
	print(Fore.GREEN + Style.BRIGHT + f"Your password is: {password}")