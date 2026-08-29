import socket
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_portscnnr():
	print_banner()
	ip = input(Fore.CYAN + Style.BRIGHT + "Write ipv4 Address you want scan: ").strip()
	while True:
		raw_ports = input(Fore.CYAN + Style.BRIGHT + "Enter the ports separated by spaces (e.g. 80 443): ")
		ports = [int(p) for p in raw_ports.replace(',', ' ').split() if p.isdigit() and 1 <= int(p) <= 65535]
		if ports:
			break
		print(Fore.RED + Style.BRIGHT + "Error: enter at least one valid port number.")
	print(Fore.CYAN + Style.BRIGHT + f"Scanning {ip} for {ports}")
	for port in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.0)
		result = s.connect_ex((ip, port))
		s.close()

		if result == 0:
			print(Fore.GREEN + Style.BRIGHT + f"Port {port}: OPEN")
		else:
			print(Fore.RED + Style.BRIGHT + f"Port {port}: CLOSED")