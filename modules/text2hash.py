import hashlib
from colorama import init, Fore, Style
from modules.ui import print_banner

init(autoreset=True)

def run_hash():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		╔═════════════╗
		║ 1. MD5      ║
		║ 2. SHA1     ║
		║ 3. SHA256   ║
		║ 4. SHA3_384 ║
		║ 5. SHA3_512 ║
		║ 6. Blake2b  ║
		╚═════════════╝
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Write a hash func. number: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text!")

	text = input(Fore.CYAN + Style.BRIGHT + "Write your phrase: ").encode('utf-8')

	if choice == 1:
		print(Fore.GREEN + Style.BRIGHT + f"Result: {hashlib.md5(text).hexdigest()}")
	elif choice == 2:
		print(Fore.GREEN + Style.BRIGHT+ f"Result: {hashlib.sha1(text).hexdigest()}")
	elif choice == 3:
		print(Fore.GREEN + Style.BRIGHT + f"Result: {hashlib.sha256(text).hexdigest()}")
	elif choice == 4:
		print(Fore.GREEN + Style.BRIGHT + f"Result: {hashlib.sha3_384(text).hexdigest()}")
	elif choice == 5:
		print(Fore.GREEN + Style.BRIGHT + f"Result: {hashlib.sha3_512(text).hexdigest()}")
	elif choice == 6:
		print(Fore.GREEN + Style.BRIGHT + f"Result: {hashlib.blake2b(text).hexdigest()}")
	else:
		print(Fore.RED + Style.BRIGHT + "Choose number's 1-6.")