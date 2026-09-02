from modules.hashing.text2hash import run_hash
from modules.crypto.symmetric_cipher import run_cryptosym
from modules.crypto.asymmetric_cipher import run_cryptoasy
from modules.crypto.decrypt_sym import run_decryptsym
from modules.crypto.decrypt_asy import run_decryptasy
from modules.ui.ui import print_banner
from modules.generators.generate_pswrd import run_genpswrd
from modules.generators.generate_UA import run_genUA
from modules.generators.generate_UUID import run_uuid_gnrtr
from modules.network.parser import run_parser
from modules.network.portscanner import run_portscnnr
from modules.network.ipcalculator import run_ipclcltr
from modules.attack.bruteforce import run_brtfrce
from modules.other.pcinfo import run_HWIDGnrtr
from colorama import init, Fore, Style

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
			[12] IP Calculator
			[13] UUID Generator
			[14] About
			[15] Credits
			""")

		while True:
			try:
				choice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))
				if choice not in range(1, 15):
					print(Fore.RED + Style.BRIGHT + "Choose function 1-14!")
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
			9: run_parser,
			10: run_portscnnr,
			11: run_HWIDGnrtr,
			12: run_ipclcltr,
			13: run_uuid_gnrtr,
			14: lambda: print(Fore.CYAN + Style.BRIGHT + """
				Mlnchly - multitool with a lot of instruments for various purposes.
				"""),
			15: lambda: print(Fore.CYAN + Style.BRIGHT + """
				Sole creator: deferred. 
				DM: Telegram @ddeferred
			"""),
		}
	
		functions[choice]()

if __name__ == "__main__":
	main()
