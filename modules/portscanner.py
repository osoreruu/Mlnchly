import socket
from modules.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_portscnnr():
	print_banner()
	IP = input(Fore.CYAN + Style.BRIGHT + "Write ipv4 Address you want scan: ").strip()
	while True:
		raw_ports = input(Fore.CYAN + Style.BRIGHT + "Enter the ports separated by spaces (e.g. 80 443): ")
		ports = [int(p) for p in raw_ports.replace(',', ' ').split() if p.isdigit()]
		if ports:
			break
		print(Fore.RED + Style.BRIGHT + "Error: enter at least one valid port number.")
	print(Fore.CYAN + Style.BRIGHT + f"Scanning {IP} for {ports}")
	for port in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.0)
		result = s.connect_ex((IP, port))
		s.close()

		if result == 0:
			print(Fore.GREEN + Style.BRIGHT + f"Port {port}: OPEN")
		else:
			print(Fore.RED + Style.BRIGHT + f"Port {port}: CLOSED")