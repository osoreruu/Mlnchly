from colorama import Fore, Style, init
from modules.ui.ui import print_banner
import socket

init(autoreset=True)

mx_hosts = {
	'gmail.com': 'gmail-smtp-in.l.google.com',
	'mail.ru': 'mxs.mail.ru',
	'yandex.ru': 'mx.yandex.ru',
	'ya.ru': 'mx.yandex.ru',
	'rambler.ru': 'mx.rambler.ru',
	'outlook.com': 'mail.hotmail.com',
	'yahoo.com': 'mta5.am0.yahoodns.net',
}


def run_SMTP():
	print_banner()
	email = input(Fore.CYAN + Style.BRIGHT + 'Write email to check: ').strip()

	try:
		username, domain = email.split('@')
	except ValueError:
		print(Fore.RED + Style.BRIGHT + 'Bad format of email!')
		return

	mx_host = mx_hosts.get(domain, f'smtp.{domain}')
	print(Fore.CYAN + Style.BRIGHT + f'Checking for {email}')

	try:
		smtp_ip = socket.gethostbyname(mx_host)
		print(Fore.CYAN + Style.BRIGHT + f'MX-server: {mx_host} ({smtp_ip})')
	except Exception:
		print(Fore.RED + Style.BRIGHT + 'Host not found')
		return

	for port in [25, 587, 465]:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(3.0)
			s.connect((smtp_ip, port))

			banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
			print(Fore.CYAN + Style.BRIGHT + f'Port {port}: OPEN | Banner: {banner}')

			s.send(b'EHLO checker.local\r\n')
			resp = s.recv(2048).decode('utf-8', errors='ignore')
			print(Fore.GREEN + Style.BRIGHT + f'Answer EHLO: {resp}')

			s.send(b'MAIL FROM: <test@checker.local>\r\n')
			mail_resp = s.recv(1024).decode('utf-8', errors='ignore')

			s.send(f'RCPT TO: <{email}>\r\n'.encode('utf-8'))
			rcpt_resp = s.recv(1024).decode('utf-8', errors='ignore')

			print(Fore.GREEN + Style.BRIGHT + f'MAIL FROM resp: {mail_resp.strip()}')
			print(Fore.GREEN + Style.BRIGHT + f'RCPT TO resp (Box): {rcpt_resp.strip()}')

			s.send(b'QUIT\r\n')
			s.close()
			break
		except Exception:
			print(Fore.RED + Style.BRIGHT + f'Port {port}: Closed / Timeout')