import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from modules.ui.ui import print_banner
from colorama import init, Fore, Style

init(autoreset=True)

def run_numberphone():
	print_banner()
	while True:
		try:
			raw = input(Fore.CYAN + Style.BRIGHT + "Write number of phone (or type 'exit'): ")
			if raw == 'exit':
				break
			number = phonenumbers.parse(raw, None)
			isvalid = phonenumbers.is_valid_number(number)
			location = geocoder.description_for_number(number, "en")
			operatorname = carrier.name_for_number(number, "en")
			timezones = timezone.time_zones_for_number(number)
			print(Fore.GREEN + Style.BRIGHT + f"Valid: {isvalid}")
			print(Fore.GREEN + Style.BRIGHT + f"Location: {location}")
			print(Fore.GREEN + Style.BRIGHT + f"Operator Name: {operatorname}")
			print(Fore.GREEN + Style.BRIGHT + f"Timezone: {timezones}")
		except phonenumbers.NumberParseException:
			print(Fore.RED + Style.BRIGHT + "Invalid Format")
		except Exception as e:
			print(Fore.RED + Style.BRIGHT + f"Error: {e}")