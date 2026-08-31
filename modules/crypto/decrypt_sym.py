from cryptography.hazmat.primitives.ciphers.aead import AESGCM, ChaCha20Poly1305
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

init(autoreset=True)


def run_decryptsym():
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
		try:
			iv = bytes.fromhex(input("iv (hex): "))
			ciphertext = bytes.fromhex(input("Ciphertext (hex): "))
			key = bytes.fromhex(input("Key (hex): "))

			aesgcm = AESGCM(key)
			plaintext = aesgcm.decrypt(iv, ciphertext, None)

			print(Fore.GREEN + Style.BRIGHT + f"Text: {plaintext.decode('UTF-8')}")

		except Exception:
			print(Fore.RED + Style.BRIGHT + "Decryption failed!")

	elif choice == 2:
		try:
			nonce = bytes.fromhex(input("Nonce (hex): "))
			ciphertext = bytes.fromhex(input("Ciphertext (hex): "))
			key = bytes.fromhex(input("Key (hex): "))

			cipher = ChaCha20Poly1305(key)
			plaintext = cipher.decrypt(nonce, ciphertext, None)

			print(Fore.GREEN + Style.BRIGHT + f"Text: {plaintext.decode('UTF-8')}")

		except Exception:
			print(Fore.RED + Style.BRIGHT + "Decryption failed!")