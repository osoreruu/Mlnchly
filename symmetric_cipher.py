import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from colorama import init, Fore, Style
from ui import print_banner

init(autoreset=True)

def run_cryptosym():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		1. AES256 (PKCS7)
		2. ChaCha20
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose crypto algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	if choice == 1:
		while True:	
			IV = input(Fore.CYAN + Style.BRIGHT + "Write your IV (16 symbols): ")
			iv_bytes = IV.encode('utf-8')

			if len(iv_bytes) == 16:
				print(Fore.GREEN + Style.BRIGHT + "Good!")
				break
			else:
				print(Fore.RED + Style.BRIGHT + "Error: IV length must be 16!")

		ciphertext = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
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
		while True:
			nonce = input(Fore.CYAN + Style.BRIGHT + "Write your nonce (16 symbols): ")
			nonce_bytes = nonce.encode('UTF-8')
    
			if len(nonce_bytes) == 16:
				print(Fore.GREEN + Style.BRIGHT + "Good!")
				break
			else:
				print(Fore.RED + Style.BRIGHT + "Error: nonce length must be 16!")

		text = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
		text_bytes = text.encode('UTF-8')
		key = os.urandom(32)

		cipher = Cipher(algorithms.ChaCha20(key, nonce_bytes), mode=None)
		encryptor = cipher.encryptor()
		encrypted_data = encryptor.update(text_bytes) + encryptor.finalize()

		print(Fore.GREEN + Style.BRIGHT + f"\n[+] Ciphertext (hex): {encrypted_data.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"[+] Key (hex): {key.hex()}")