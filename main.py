from colorama import Fore, Style, init
from modules.ui.ui import print_banner

init(autoreset=True)

def main():
    while True:
        print_banner()
        print(Fore.CYAN + Style.BRIGHT + """
            [1] Text2Hash
            [2] Symmetric Crypt
            [3] Asymmetric Crypt
            [4] Symmetric Decrypt
            [5] Asymmetric Decrypt
            [6] Generate Password
            [7] Brute Forcer
            [8] Generate UserAgent
            [9] Robots.txt and sitemap.xml parser
            [10] Port Scanner
            [11] HWID Generating
            [12] IP Calculator
            [13] UUID Generator
            [14] Number checker
            [15] DNS Checker
            [16] About
            [17] Credits
            """)

        while True:
            try:
                choice = int(input(Fore.CYAN + Style.BRIGHT + "Select function: "))
                if choice not in range(1, 18):
                    print(Fore.RED + Style.BRIGHT + "Choose function 1-17!")
                    continue
                break
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Error! Write number, not text")

        functions = {
            1: lambda: __import__("modules.hashing.text2hash", fromlist=["run_hash"]).run_hash(),
            2: lambda: __import__("modules.crypto.symmetric_cipher", fromlist=["run_cryptosym"]).run_cryptosym(),
            3: lambda: __import__("modules.crypto.asymmetric_cipher", fromlist=["run_cryptoasy"]).run_cryptoasy(),
            4: lambda: __import__("modules.crypto.decrypt_sym", fromlist=["run_decryptsym"]).run_decryptsym(),
            5: lambda: __import__("modules.crypto.decrypt_asy", fromlist=["run_decryptasy"]).run_decryptasy(),
            6: lambda: __import__("modules.generators.generate_pswrd", fromlist=["run_genpswrd"]).run_genpswrd(),
            7: lambda: __import__("modules.attack.bruteforce", fromlist=["run_brtfrce"]).run_brtfrce(),
            8: lambda: __import__("modules.generators.generate_UA", fromlist=["run_genUA"]).run_genUA(),
            9: lambda: __import__("modules.network.parser", fromlist=["run_parser"]).run_parser(),
            10: lambda: __import__("modules.network.portscanner", fromlist=["run_portscnnr"]).run_portscnnr(),
            11: lambda: __import__("modules.other.pcinfo", fromlist=["run_HWIDGnrtr"]).run_HWIDGnrtr(),
            12: lambda: __import__("modules.network.ipcalculator", fromlist=["run_ipclcltr"]).run_ipclcltr(),
            13: lambda: __import__("modules.generators.generate_UUID", fromlist=["run_uuid_gnrtr"]).run_uuid_gnrtr(),
            14: lambda: __import__("modules.attack.phonenumber", fromlist=["run_numberphone"]).run_numberphone(),
            15: lambda: __import__("modules.network.dnschecker", fromlist=["run_dnschecker"]).run_dnschecker(),
            16: lambda: print(Fore.CYAN + Style.BRIGHT + """
                Mlnchly - multitool with a lot of instruments for various purposes.
                """),
            17: lambda: print(Fore.CYAN + Style.BRIGHT + """
                Sole creator: deferred. 
                DM: Telegram @ddeferred
            """),
        }
    
        functions[choice]()

if __name__ == "__main__":
    main()