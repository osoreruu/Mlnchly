from fake_useragent import UserAgent
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_genUA():
	print_banner()
	ua = UserAgent()
	while True:
		try:
			count = int(input(Fore.CYAN + Style.BRIGHT + "Enter the number of User-Agents to generate: "))
			if count > 0:
				break
			print(Fore.RED + Style.BRIGHT + "Length must be greater than 0!")
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Write a number. Not text.")
	with open("useragents.txt", "w", encoding="utf-8") as f:
		for _ in range(1, count + 1):
			f.write(ua.random + "\n")
	print(Fore.GREEN + Style.BRIGHT + f"{count} UserAgent generated! UA writed in useragents.txt")