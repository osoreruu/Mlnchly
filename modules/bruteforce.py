from colorama import init, Fore, Style
from modules.ui import print_banner
import hashlib
import itertools
import string

init(autoreset=True)

def run_brtfrce():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔═══════════════════════════════════╗
	  ║ 1. Dictionary Brute (RockYou.txt) ║
	  ║ 2. Base Brute-Force               ║
	  ╚═══════════════════════════════════╝
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
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))
			if choice not in (1, 2):
				print(Fore.RED + Style.BRIGHT + "Choose 1 or 2!")
				continue
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Select number, not text.")

	if choice == 1:
		path = input(Fore.CYAN + Style.BRIGHT + "Write a path to rockyou.txt [default: rockyou/rockyou.txt]: ").strip()

		if not path:
			path = "rockyou/rockyou.txt"

		basehash = input(Fore.CYAN + Style.BRIGHT + "Write your hash to Dictionary Brute: ").strip().lower()

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
				algochoice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))

				if algochoice not in range(1, 7):
					print(Fore.RED + Style.BRIGHT + "Choose from 1 to 6!")
					continue

				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Select number, not text.")

		founded_pass = False

		try:
			with open(path, 'r', encoding='latin-1') as f:
				print(Fore.GREEN + Style.BRIGHT + "Cracking...")

				for line in f:
					password = line.strip()
					text = password.encode('UTF-8')
					h = hash_functions[algochoice](text).hexdigest()

					if h == basehash:
						print(Fore.GREEN + Style.BRIGHT + f"Success! Password: {password}")
						founded_pass = True
						break

			if not founded_pass:
				print(Fore.RED + Style.BRIGHT + "Password wasn't found.")

		except FileNotFoundError:
			print(Fore.RED + Style.BRIGHT + f"Error: File '{path}' not found.")

	elif choice == 2:
		basehash = input(Fore.CYAN + Style.BRIGHT + "Write your hash to Base Brute-Force: ").strip().lower()

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
				algochoice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))

				if algochoice not in range(1, 7):
					print(Fore.RED + Style.BRIGHT + "Choose from 1 to 6!")
					continue

				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Select number, not text.")

		while True:
			try:
				min_len = int(input(Fore.CYAN + Style.BRIGHT + "Enter minimum password length: "))

				if min_len < 1:
					print(Fore.RED + Style.BRIGHT + "Length must be greater than 0!")
					continue

				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Select number, not text.")

		while True:
			try:
				max_len = int(input(Fore.CYAN + Style.BRIGHT + "Enter maximum password length: "))

				if max_len < min_len:
					print(Fore.RED + Style.BRIGHT + "Max length can't be less than min length!")
					continue

				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Select number, not text.")

		chars = string.ascii_lowercase + string.digits

		print(Fore.GREEN + Style.BRIGHT + f"Starting brute-force for lengths from {min_len} to {max_len}...")

		founded_pass = False

		for length in range(min_len, max_len + 1):
			if founded_pass:
				break

			print(Fore.YELLOW + Style.BRIGHT + f"Checking length {length}...")

			pool = itertools.product(chars, repeat=length)

			for guess_tuple in pool:
				password = "".join(guess_tuple)
				text = password.encode('UTF-8')
				h = hash_functions[algochoice](text).hexdigest()

				if h == basehash:
					print(Fore.GREEN + Style.BRIGHT + f"Success! Password: {password}")
					founded_pass = True
					break

		if not founded_pass:
			print(Fore.RED + Style.BRIGHT + "Password wasn't found.")