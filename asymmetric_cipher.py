from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes
from colorama import init, Fore, Style
from ui import print_banner

init(autoreset=True)

def run_cryptoasy():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		1. RSA2048 (Encrypt)
		2. ECC256 (Sign)
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose asymmetric algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text.")

	if choice == 1:
		private_key = rsa.generate_private_key(
			public_exponent=65537,
			key_size=2048
		)
		public_key = private_key.public_key()
		message = input(Fore.CYAN + Style.BRIGHT + "Write your text to encrypt: ").encode('utf-8')
		ciphertext = public_key.encrypt(
					message,
					padding.OAEP(
						mgf=padding.MGF1(algorithm=hashes.SHA256()),
						algorithm=hashes.SHA256(),
						label=None
					)
				)
		print(Fore.GREEN + Style.BRIGHT + f"\n[+] Ciphertext (hex): {ciphertext.hex()}")
	elif choice == 2:
		private_key = ec.generate_private_key(ec.SECP256R1())
		public_key = private_key.public_key()
		message = input(Fore.CYAN + Style.BRIGHT + "Write text to sign: ").encode('UTF-8')
		signature = private_key.sign(
			message,
			ec.ECDSA(hashes.SHA256())
		)
		try:
			public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
			is_valid = True
		except Exception:
			is_valid = False
		print(Fore.GREEN + Style.BRIGHT + f"\n[+] Signature (hex): {signature.hex()}")
	else:
		print(Fore.RED + Style.BRIGHT + "Choose number's 1-2.")