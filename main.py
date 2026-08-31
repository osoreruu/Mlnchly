from colorama import init, Fore, Style
from modules.hashing.text2hash import run_hash
from modules.crypto.symmetric_cipher import run_cryptosym
from modules.crypto.asymmetric_cipher import run_cryptoasy
from modules.crypto.decrypt_sym import run_decryptsym
from modules.crypto.decrypt_asy import run_decryptasy
from modules.ui.ui import print_banner
from modules.generators.generate_pswrd import run_genpswrd
from modules.generators.generate_UA import run_genUA
from modules.network.robots_parser import run_robots_parser
from modules.network.portscanner import run_portscnnr
from modules.attack.bruteforce import run_brtfrce
from modules.other.pcinfo import run_HWIDGnrtr

init(autoreset=True)

def main():
	while True:
		print_banner()
		print(Fore.CYAN + Style.BRIGHT + """
			[1] Text2Hash
			[2] Symmetric Crypt
			[3] Asymmetric Crypt
			[4] Symmetric Decrypt
			[5] Asymmetric Decrypt
			[6] Generate Password
			[7] Brute Forcer
			[8] Generate UserAgent
			[9] Robots.txt and sitemap.xml parser
			[10] Port Scanner
			[11] HWID Generating
			[12] About
			[13] Credits
			""")

		while True:
			try:
				choice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))
				if choice not in range(1, 14):
					print(Fore.RED + Style.BRIGHT + "Choose function 1-13!")
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
			11: run_HWIDGnrtr,
			12: lambda: print(Fore.CYAN + Style.BRIGHT + """
				Mlnchly is a Python tool for working with hashes and cryptography; 
				it supports a wide range of algorithms and handles both encryption and decryption.
				"""),
			13: lambda: print(Fore.CYAN + Style.BRIGHT + """
				Sole creator: deferred. 
				DM: Telegram @ddeferred
			"""),
		}
	
		functions[choice]()

if __name__ == "__main__":
	main()