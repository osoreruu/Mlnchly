import httpx
from modules.ui.ui import print_banner
from colorama import init, Fore, Style
from fake_useragent import UserAgent

init(autoreset=True)
ua = UserAgent()


def run_robots_parser():
	print("""
		[1] Parse robots.txt
		[2] Parse sitemap.xml
	""")
	try:
		choice = int(input(Fore.CYAN + Style.BRIGHT + "Select what to parse: "))
		if choice == 1:
			site = input(Fore.CYAN + Style.BRIGHT + "Type yout URL: ").strip().replace("https://", "").replace("http://", "").rstrip("/")
			url = f"https://{site}/robots.txt"
			try:
				response = httpx.get(url, timeout=5.0, follow_redirects=True, headers={"User-Agent": ua.random})
				if response.status_code == 200:
					print(Fore.GREEN + Style.BRIGHT + "robots.txt is found!")
					with open(f"output_{site}_robots.txt", "w", encoding="utf-8") as f:
						f.write(response.text)
				else:
					print(f"robots.txt not found! Error: {response.status_code}")
			except httpx.RequestError as e:
				print(Fore.RED + Style.BRIGHT + f"Connection Error: {e})")
		elif choice == 2:
			site = input(Fore.CYAN + Style.BRIGHT + "Type yout URL: ").strip().replace("https://", "").replace("http://", "").rstrip("/")
			url = f"https://{site}/sitemap.xml"
			try:
				response = httpx.get(url, timeout=5.0, follow_redirects=True, headers={"User-Agent": ua.random})
				if response.status_code == 200:
					print(Fore.GREEN + Style.BRIGHT + "sitemap.xml is found!")
					with open(f"output_{site}_sitemap.txt", "w", encoding="utf-8") as f:
						f.write(response.text)
				else:
					print(f"sitemap.xml not found! Error: {response.status_code}")
			except httpx.RequestError as e:
				print(Fore.RED + Style.BRIGHT + f"Connection Error: {e})")
		else:
			print(Fore.RED + Style.BRIGHT + "Write a number 1 or 2!")
	except ValueError:
		print(Fore.RED + Style.BRIGHT + "Write number, not text!")