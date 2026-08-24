from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from colorama import init, Fore, Style
from modules.ui import print_banner

init(autoreset=True)

def run_decryptsym():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔═══════════════════╗
	  ║ 1. AES256 (PKCS7) ║
	  ║ 2. ChaCha20       ║
	  ╚═══════════════════╝
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose crypto algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")
	if choice == 1:
		while True:	
			IV = input(Fore.CYAN + Style.BRIGHT + "Write your IV (16 symbols): ").strip()
			iv_bytes = IV.encode('utf-8')

			if len(iv_bytes) == 16:
				print(Fore.GREEN + Style.BRIGHT + "Good!")
				break
			else:
				print(Fore.RED + Style.BRIGHT + "Error: IV length must be 16!")
		while True:
			key_hex = input(Fore.CYAN + Style.BRIGHT + "Write your Key: ").strip()
			try:
				key = bytes.fromhex(key_hex)
				if len(key) == 32:
					print(Fore.GREEN + Style.BRIGHT + "Good!")
					break
				else:
					print(Fore.RED + Style.BRIGHT + "Error: Key length must be 64 hex symbols!")
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Key!")
		while True:
			ciphertext_hex = input(Fore.CYAN + Style.BRIGHT + "Write your hex Ciphertext: ").strip()
			try:
				ciphertext_bytes = bytes.fromhex(ciphertext_hex)
				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Ciphertext!")
		try:
			cipher = Cipher(algorithms.AES(key), modes.CBC(iv_bytes))
			decryptor = cipher.decryptor()
			padded_data = decryptor.update(ciphertext_bytes) + decryptor.finalize()
			unpadder = padding.PKCS7(128).unpadder()
			text_bytes = unpadder.update(padded_data) + unpadder.finalize()

			print(Fore.GREEN + Style.BRIGHT + f"\n[+] Decrypted text: {text_bytes.decode('utf-8')}")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"\n[-] Decryption failed! Check your key, IV or ciphertext. Error: {e}")
	elif choice == 2:
		while True:
			nonce = input(Fore.CYAN + Style.BRIGHT + "Write your nonce (16 symbols): ")
			nonce_bytes = nonce.encode('UTF-8')
	
			if len(nonce_bytes) == 16:
				print(Fore.GREEN + Style.BRIGHT + "Good!")
				break
			else:
				print(Fore.RED + Style.BRIGHT + "Error: nonce length must be 16!")
		while True:
			key_hex = input(Fore.CYAN + Style.BRIGHT + "Write your Key (hex): ").strip()
			try:
				key = bytes.fromhex(key_hex)
				if len(key) == 32:
					print(Fore.GREEN + Style.BRIGHT + "Good!")
					break
				else:
					print(Fore.RED + Style.BRIGHT + "Error: Key length must be 32 bytes (64 hex characters)!")
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Key!")
		while True:
			ciphertext_hex = input(Fore.CYAN + Style.BRIGHT + "Write your Ciphertext (hex): ").strip()
			try:
				ciphertext_bytes = bytes.fromhex(ciphertext_hex)
				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Ciphertext!")
		try:
			cipher = Cipher(algorithms.ChaCha20(key, nonce_bytes), mode=None)
			decryptor = cipher.decryptor()
			decrypted_data = decryptor.update(ciphertext_bytes) + decryptor.finalize()

			print(Fore.GREEN + Style.BRIGHT + f"\n[+] Decrypted text: {decrypted_data.decode('utf-8')}")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"\n[-] Decryption failed! Check your key, nonce or ciphertext. Error: {e}")
	else:
		print(Fore.RED + Style.BRIGHT + "Choose number's 1-2.")