from colorama import init, Fore, Style
from text2hash import run_hash
from symmetric_cipher import run_crypto
from ui import print_banner

init(autoreset=True)

def main():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		1. Text2Hash
		2. SymmetricCipher
		""")
	choice = int(input(Fore.CYAN + Style.BRIGHT + "Select func. 1 or 2: "))
	if choice == 1:
		run_hash()
	elif choice == 2:
		run_crypto()
	else:
		print(Fore.RED + Style.BRIGHT + "Wrong number!")

if __name__ == "__main__":
	main()