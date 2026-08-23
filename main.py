from colorama import init, Fore, Style
from text2hash import run_hash
from symmetric_cipher import run_cryptosym
from asymmetric_cipher import run_cryptoasy
from ui import print_banner

init(autoreset=True)

def main():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		1. Text2Hash
		2. SymmetricCipher
		3. AsymmetricCipher
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Select func. 1, 2 or 3: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	if choice == 1:
		run_hash()
	elif choice == 2:
		run_cryptosym()
	elif choice == 3:
		run_cryptoasy()
	else:
		print(Fore.RED + Style.BRIGHT + "Wrong number!")

if __name__ == "__main__":
	main()