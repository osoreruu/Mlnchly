from colorama import init, Fore, Style
from modules.text2hash import run_hash
from modules.symmetric_cipher import run_cryptosym
from modules.asymmetric_cipher import run_cryptoasy
from modules.ui import print_banner
from modules.decrypt_sym import run_decryptsym
from modules.decrypt_asy import run_decryptasy

init(autoreset=True)

def main():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔══════════════════════╗
	  ║ 1. Text2Hash         ║
	  ║ 2. SymmetricCrypt    ║
	  ║ 3. AsymmetricCrypt   ║
	  ║ 4. SymmetricDecrypt  ║
	  ║ 5. AsymmetricDecrypt ║
	  ╚══════════════════════╝
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Select func. 1, 2, 3, 4 or 5: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	if choice == 1:
		run_hash()
	elif choice == 2:
		run_cryptosym()
	elif choice == 3:
		run_cryptoasy()
	elif choice == 4:
		run_decryptsym()
	elif choice == 5:
		run_decryptasy()
	else:
		print(Fore.RED + Style.BRIGHT + "Wrong number!")

if __name__ == "__main__":
	main()