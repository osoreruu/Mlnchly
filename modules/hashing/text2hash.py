import hashlib
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

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

	hash_functions = {
		1: hashlib.md5,
		2: hashlib.sha1,
		3: hashlib.sha256,
		4: hashlib.sha3_384,
		5: hashlib.sha3_512,
		6: hashlib.blake2b
	}

	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Write a hash func. number: "))
			if choice not in hash_functions:
				print(Fore.RED + Style.BRIGHT + "Choose a number from 1 to 6!")
				continue
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text!")

	text = input(Fore.CYAN + Style.BRIGHT + "Write your phrase: ").encode('utf-8')

	hash_function = hash_functions[choice]
	result = hash_function(text).hexdigest()

	print(Fore.GREEN + Style.BRIGHT + f"Result: {result}")