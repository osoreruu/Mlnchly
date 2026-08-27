import httpx
from modules.ui import print_banner
from colorama import init, Fore, Style
from fake_useragent import UserAgent

init(autoreset=True)
ua = UserAgent()

def run_robots_parser():
	site = input(Fore.CYAN + Style.BRIGHT + "Type yout URL: ").strip().replace("https://", "").replace("http://", "").rstrip("/")
	url = f"https://{site}/robots.txt"
	try:
		response = httpx.get(url, timeout=5.0, follow_redirects=True, headers={"UserAgent": ua.random})
		if response.status_code == 200:
			print(Fore.GREEN + Style.BRIGHT + "robots.txt is found!")
			with open(f"output_{site}.txt", "w", encoding="utf-8") as f:
				f.write(response.text)
		else:
			print(f"robots.txt not found! Error: {response.status_code}")
	except httpx.RequestError as e:
		print(Fore.RED + Style.BRIGHT + f"[-] Connection error: {e}")