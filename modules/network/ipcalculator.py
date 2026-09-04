import ipaddress
from colorama import init, Fore, Style
from modules.ui.ui import print_banner
def run_ipclcltr():
	print_banner()
	try:
		usr_input = input(Fore.CYAN + Style.BRIGHT + "Write your IP address with subnet (e.g 192.168.0.0/24): ").strip()
		net = ipaddress.ip_network(usr_input, strict=False)

		hosts = list(net.hosts())
		First_usable_host = hosts[0] if hosts else "None (Single host / Point-to-Point)"

		print(Fore.GREEN + Style.BRIGHT + f"Quantity of addresses: {net.num_addresses}")
		print(Fore.GREEN + Style.BRIGHT + f"Mask: {net.netmask}")
		print(Fore.GREEN + Style.BRIGHT + f"Network Address: {net.network_address}")
		print(Fore.GREEN + Style.BRIGHT + f"Broadcast Address: {net.broadcast_address}")
		print(Fore.GREEN + Style.BRIGHT + f"First usable host: {First_usable_host}")

	except (ipaddress.AddressValueError, ipaddress.NetmaskValueError) as e:
		print(Fore.RED + Style.BRIGHT + f"Invalid IP or subnet format: {e}")
	except Exception as e:
		print(Fore.RED + Style.BRIGHT + f"Error: {e}")