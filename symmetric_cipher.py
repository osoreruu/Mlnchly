import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from colorama import init, Fore, Style

init(autoreset=True)

def run_crypto():
	print(Fore.MAGENTA + Style.BRIGHT + """
	 ███▄ ▄███▓ ██▓     ███▄    █  ▄████▄   ██░ ██  ██▓   ▓██   ██▓
	▓██▒▀█▀ ██▒▓██▒     ██ ▀█   █ ▒██▀ ▀█  ▓██░ ██▒▓██▒    ▒██  ██▒
	▓██    ▓██░▒██░    ▓██  ▀█ ██▒▒▓█    ▄ ▒██▀▀██░▒██░     ▒██ ██░
	▒██    ▒██ ▒██░    ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒░▓█ ░██ ▒██░     ░ ▐██▓░
	▒██▒   ░██▒░██████▒▒██░   ▓██░▒ ▓███▀ ░░▓█▒░██▓░██████▒ ░ ██▒▓░
	░ ▒░   ░  ░░ ▒░▓  ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▓  ░  ██▒▒▒ 
	░  ░      ░░ ░ ▒  ░░ ░░   ░ ▒░  ░  ▒    ▒ ░▒░ ░░ ░ ▒  ░▓██ ░▒░ 
	░      ░     ░ ░      ░   ░ ░ ░         ░  ░░ ░  ░ ░   ▒ ▒ ░░  
	       ░       ░  ░         ░ ░ ░       ░  ░  ░    ░  ░░ ░     
 	                             ░                        ░ ░
		""")
	print(Fore.CYAN + Style.BRIGHT + """
		1. AES256 (PKCS7)
		2. ChaCha20
		""")
	choice = int(input(Fore.BLUE + Style.BRIGHT + "Choose crypto algorithm: "))

	if choice == 1:

		IV = input(Fore.BLUE + Style.BRIGHT + "Write you'r IV (16 symbols): ")
		iv_bytes = IV.encode('utf-8')

		if len(iv_bytes) != 16:
			print(Fore.RED + Style.BRIGHT + "Error: IV length must be 16!")
			exit()
		else:
			print(Fore.GREEN + Style.BRIGHT + "Good!")

		ciphertext = input(Fore.BLUE + Style.BRIGHT + "Write you'r text: ")
		text_bytes = ciphertext.encode('UTF-8')

		key = os.urandom(32)

		padder = padding.PKCS7(128).padder()
		padded_data = padder.update(text_bytes) + padder.finalize()

		cipher = Cipher(algorithms.AES(key), modes.CBC(iv_bytes))
		encryptor = cipher.encryptor()
		ciphertext = encryptor.update(padded_data) + encryptor.finalize()

		print(Fore.GREEN + Style.BRIGHT + f"\n[+] Ciphertext (hex): {ciphertext.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"[+] Key (hex): {key.hex()}")

	elif choice == 2:
		nonce = input(Fore.BLUE + Style.BRIGHT + "Write you'r nonce (16 symbols): ")
		nonce_bytes = nonce.encode('UTF-8')
    
		if len(nonce_bytes) != 16:
			print(Fore.RED + Style.BRIGHT + "Error: nonce length must be 16!")
			exit()
		else:
			print(Fore.GREEN + Style.BRIGHT + "Good!")

		text = input(Fore.BLUE + Style.BRIGHT + "Write you'r text: ")
		text_bytes = text.encode('UTF-8')
		key = os.urandom(32)

		cipher = Cipher(algorithms.ChaCha20(key, nonce_bytes), mode=None)
		encryptor = cipher.encryptor()
		encrypted_data = encryptor.update(text_bytes) + encryptor.finalize()

		print(Fore.GREEN + Style.BRIGHT + f"\n[+] Ciphertext (hex): {encrypted_data.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"[+] Key (hex): {key.hex()}")