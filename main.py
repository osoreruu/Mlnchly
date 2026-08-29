from colorama import init, Fore, Style
from modules.text2hash import run_hash
from modules.symmetric_cipher import run_cryptosym
from modules.asymmetric_cipher import run_cryptoasy
from modules.ui import print_banner
from modules.decrypt_sym import run_decryptsym
from modules.decrypt_asy import run_decryptasy
from modules.generate_pswrd import run_genpswrd
from modules.bruteforce import run_brtfrce
from modules.generate_UA import run_genUA
from modules.robots_parser import run_robots_parser
from modules.portscanner import run_portscnnr

init(autoreset=True)

def main():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔═══════════════════════╗
	  ║ 1. Text2Hash          ║
	  ║ 2. SymmetricCrypt     ║
	  ║ 3. AsymmetricCrypt    ║
	  ║ 4. SymmetricDecrypt   ║
	  ║ 5. AsymmetricDecrypt  ║
	  ║ 6. GeneratePassword   ║
	  ║ 7. BruteForcer        ║
	  ║ 8. Generate UserAgent ║
	  ║ 9. Robots.txt parser  ║
	  ║ 10. Port Scanner      ║
	  ║ 11. About	          ║
	  ║ 12. Credits           ║
	  ╚═══════════════════════╝
		""")

	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))
			if choice not in range(1, 13):
				print(Fore.RED + Style.BRIGHT + "Choose function 1-12!")
				continue
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	functions = {
		1: run_hash,
		2: run_cryptosym,
		3: run_cryptoasy,
		4: run_decryptsym,
		5: run_decryptasy,
		6: run_genpswrd,
		7: run_brtfrce,
		8: run_genUA,
		9: run_robots_parser,
		10: run_portscnnr,
		11: lambda: print(Fore.CYAN + Style.BRIGHT + """
			Mlnchly is a Python tool for working with hashes and cryptography; 
			it supports a wide range of algorithms and handles both encryption and decryption.
		"""),
		12: lambda: print(Fore.CYAN + Style.BRIGHT + """
			Sole creator: deferred. 
			DM: Telegram @ddeferred
		""")
	}

	functions[choice]()

if __name__ == "__main__":
	main()