from colorama import Fore, Style, init
import dns.resolver
from modules.ui.ui import print_banner

init(autoreset=True)

def run_dnschecker():
	print_banner()
	types = ["A", "AAAA", "MX", "TXT", "NS", "CNAME"]
	while True:
		try:
			domain = input(Fore.CYAN + Style.BRIGHT + "Write your DNS (Format: xbox-dns.ru): ").strip()
			if domain == "exit":
				break
			if not domain:
				continue
			
			for r_type in types:
				try:
					answers = dns.resolver.resolve(domain, r_type)
					print(Fore.CYAN + Style.BRIGHT + f"[{r_type} Types]:")
					for rdata in answers:
						print(Fore.CYAN + Style.BRIGHT + f"{rdata.to_text()}")
				except dns.resolver.NoAnswer:
					pass
				except dns.resolver.NXDOMAIN:
					print(Fore.RED + Style.BRIGHT + f"Domain {domain} does not exist.")
					break
				except Exception:
					pass
					
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"Error: {e}")