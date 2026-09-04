import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

init(autoreset=True)

def run_cryptosym():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		[1] AES-256-GCM
		[2] ChaCha20-Poly1305
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose crypto algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

	if choice == 1:
		iv = os.urandom(12)
		text = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
		text_bytes = text.encode("UTF-8")

		key = AESGCM.generate_key(bit_length=256)

		aesgcm = AESGCM(key)
		ciphertext = aesgcm.encrypt(iv, text_bytes, None)

		with open("output/Key_AES.txt", 'w', encoding='UTF-8') as f:
			f.write(key.hex() + "\n")
		print(Fore.GREEN + Style.BRIGHT + f"IV (hex): {iv.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Ciphertext (hex): {ciphertext.hex()}")
		print(Fore.GREEN + Style.BRIGHT + "Key generated in Key_AES.txt")

	elif choice == 2:
		nonce = os.urandom(12)
		text = input(Fore.CYAN + Style.BRIGHT + "Write your text: ")
		text_bytes = text.encode("UTF-8")

		key = ChaCha20Poly1305.generate_key()

		cipher = ChaCha20Poly1305(key)
		encrypted_data = cipher.encrypt(nonce, text_bytes, None)

		with open("output/Key_ChaCha.txt", 'w', encoding='UTF-8') as f:
			f.write(key.hex() + "\n")
		print(Fore.GREEN + Style.BRIGHT + f"Nonce (hex): {nonce.hex()}")
		print(Fore.GREEN + Style.BRIGHT + f"Ciphertext (hex): {encrypted_data.hex()}")
		print(Fore.GREEN + Style.BRIGHT + "Key generated in Key_ChaCha.txt")