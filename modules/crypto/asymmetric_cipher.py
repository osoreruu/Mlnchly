from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes, serialization
from colorama import init, Fore, Style
from modules.ui.ui import print_banner

init(autoreset=True)

def run_cryptoasy():
	print_banner()
	print(Fore.CYAN + Style.BRIGHT + """
		[1] RSA2048 (Encrypt)
		[2] ECDSA P256 (Sign)
		""")
	while True:
		try:
			choice = int(input(Fore.CYAN + Style.BRIGHT + "Choose asymmetric algorithm: "))
			break
		except ValueError:
			print(Fore.RED + Style.BRIGHT + "Error! Write number, not text.")

	if choice == 1:
		private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
		public_key = private_key.public_key()
		
		pem_private = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
		pem_public = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

		message = input(Fore.CYAN + Style.BRIGHT + "Write your text to encrypt: ").encode('utf-8')
		if len(message) > 190:
			print(Fore.RED + Style.BRIGHT + "Your text isn't 190 bytes.")
			return
			
		ciphertext = public_key.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
		with open("output/pem_private_rsa.pem", 'w', encoding='UTF-8') as f:
			f.write(f"{pem_private.decode('UTF-8')}")
		print(Fore.GREEN + Style.BRIGHT + f"Public Key (PEM):\n {pem_public.decode('utf-8')}")
		print(Fore.GREEN + Style.BRIGHT + f"Ciphertext (hex):\n {ciphertext.hex()}")

	elif choice == 2:
		private_key = ec.generate_private_key(ec.SECP256R1())
		public_key = private_key.public_key()
		
		pem_private = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
		pem_public = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

		message = input(Fore.CYAN + Style.BRIGHT + "Write text to sign: ").encode('UTF-8')

		signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

		with open("output/pem_private_ecdsa.pem", 'w', encoding='UTF-8') as f:
			f.write(f"{pem_private.decode('UTF-8')}")
		print(Fore.GREEN + Style.BRIGHT + f"Public Key (PEM):\n {pem_public.decode('utf-8')}")
		print(Fore.GREEN + Style.BRIGHT + f"Signature (hex):\n {signature.hex()}")
	else:
		print(Fore.RED + Style.BRIGHT + "Choose number's 1-2.")