from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes, serialization
from colorama import init, Fore, Style
from modules.ui import print_banner

init(autoreset=True)

def run_decryptasy():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
	  ╔══════════════════════════════╗
	  ║ 1. RSA2048 (Decrypt)         ║
	  ║ 2. ECC256 (Verify Signature) ║
	  ╚══════════════════════════════╝
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose asymmetric algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text.")

	if choice == 1:
		print(Fore.CYAN + Style.BRIGHT + "Paste your Private Key (PEM format, end with an empty line or press Ctrl+D / enter 'END'):")
		lines = []
		while True:
			line = input()
			if line.strip() == "END" or line == "":
				if lines:
					break
				continue
			lines.append(line)
		pem_data = "\n".join(lines).encode('utf-8')

		try:
			private_key = serialization.load_pem_private_key(
				pem_data,
				password=None
			)
			print(Fore.GREEN + Style.BRIGHT + "Good! Private key loaded.")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"Error loading private key: {e}")
			return

		while True:
			ciphertext_hex = input(Fore.CYAN + Style.BRIGHT + "Write your hex Ciphertext: ").strip()
			try:
				ciphertext_bytes = bytes.fromhex(ciphertext_hex)
				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Ciphertext!")

		try:
			decrypted_message = private_key.decrypt(
				ciphertext_bytes,
				padding.OAEP(
					mgf=padding.MGF1(algorithm=hashes.SHA256()),
					algorithm=hashes.SHA256(),
					label=None
				)
			)
			print(Fore.GREEN + Style.BRIGHT + f"\n[+] Decrypted text: {decrypted_message.decode('utf-8')}")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"\n[-] Decryption failed! Error: {e}")

	elif choice == 2:
		print(Fore.CYAN + Style.BRIGHT + "Paste your Public Key (PEM format, end with 'END' or empty line):")
		lines = []
		while True:
			line = input()
			if line.strip() == "END" or line == "":
				if lines:
					break
				continue
			lines.append(line)
		pem_data = "\n".join(lines).encode('utf-8')

		try:
			public_key = serialization.load_pem_public_key(pem_data)
			print(Fore.GREEN + Style.BRIGHT + "Good! Public key loaded.")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"Error loading public key: {e}")
			return

		message = input(Fore.CYAN + Style.BRIGHT + "Write original signed text: ").encode('UTF-8')

		while True:
			signature_hex = input(Fore.CYAN + Style.BRIGHT + "Write Signature (hex): ").strip()
			try:
				signature_bytes = bytes.fromhex(signature_hex)
				break
			except ValueError:
				print(Fore.RED + Style.BRIGHT + "Error: Invalid hex format for Signature!")

		try:
			public_key.verify(
				signature_bytes,
				message,
				ec.ECDSA(hashes.SHA256())
			)
			print(Fore.GREEN + Style.BRIGHT + "\n[+] Signature is VALID!")
		except Exception:
			print(Fore.RED + Style.BRIGHT + "\n[-] Signature is INVALID!")

	else:
		print(Fore.RED + Style.BRIGHT + "Choose number's 1-2.")