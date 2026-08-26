from colorama import init, Fore, Style
from modules.ui import print_banner
import string
import secrets

init(autoreset=True)

def run_genpswrd():
	print_banner()
	Alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+-="
	try:
		length = int(input(Fore.CYAN + Style.BRIGHT + "Write a length of password: "))
	except ValueError:
		print(Fore.RED + Style.BRIGHT + "Write a number!")
		return

	password = "".join(secrets.choice(Alphabet) for _ in range(length))
	print(Fore.GREEN + Style.BRIGHT + f"Your password is: {password}")