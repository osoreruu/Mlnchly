import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

init(autoreset=True)

def run_cryptosym():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔═════════════════════╗
	  ║ 1. AES256-GCM       ║
	  ║ 2. ChaCha20Poly1305 ║
	  ╚═════════════════════╝
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose crypto algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	if choice == 1:
		iv = os.urandom(16)
		text = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
		text_bytes = text.encode("UTF-8")

		key = AESGCM.generate_key(bit_length=256)

		aesgcm = AESGCM(key)
		ciphertext = aesgcm.encrypt(iv, text_bytes, None)

		print(Fore.GREEN + Style.BRIGHT + f"IV (hex): {iv.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Ciphertext (hex): {ciphertext.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Key (hex): {key.hex()}")

	elif choice == 2:
		nonce = os.urandom(12)
		text = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
		text_bytes = text.encode("UTF-8")

		key = ChaCha20Poly1305.generate_key()

		cipher = ChaCha20Poly1305(key)
		encrypted_data = cipher.encrypt(nonce, text_bytes, None)

		print(Fore.GREEN + Style.BRIGHT + f"Nonce (hex): {nonce.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Ciphertext (hex): {encrypted_data.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Key (hex): {key.hex()}")