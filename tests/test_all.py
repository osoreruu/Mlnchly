import hashlib
import os
import sys
import traceback
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# COLORS
# ============================================================

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


# ============================================================
# TEST SYSTEM
# ============================================================

total_tests = 0
passed_tests = 0
failed_tests = 0


def run_test(name, function):
    global total_tests
    global passed_tests
    global failed_tests

    total_tests += 1

    try:
        function()

        passed_tests += 1

        print(
            f"{GREEN}[PASS]{RESET} "
            f"{name}"
        )

        return True

    except Exception as error:
        failed_tests += 1

        print(
            f"{RED}[FAIL]{RESET} "
            f"{name}"
        )

        print(
            f"       {RED}{type(error).__name__}: "
            f"{error}{RESET}"
        )

        return False


def section(name):
    print()
    print(
        f"{CYAN}========== {name} =========={RESET}"
    )


# ============================================================
# HASHING TESTS
# ============================================================

def hashing_tests():

    section("HASHING")

    def md5():
        result = hashlib.md5(
            b"hello"
        ).hexdigest()

        assert result == (
            "5d41402abc4b2a76b9719d911017c592"
        )

    def sha256():
        result = hashlib.sha256(
            b"hello"
        ).hexdigest()

        assert len(result) == 64

    def sha512():
        result = hashlib.sha512(
            b"hello"
        ).hexdigest()

        assert len(result) == 128

    def deterministic():
        a = hashlib.sha256(
            b"hello"
        ).hexdigest()

        b = hashlib.sha256(
            b"hello"
        ).hexdigest()

        assert a == b

    def different_input():
        a = hashlib.sha256(
            b"hello"
        ).hexdigest()

        b = hashlib.sha256(
            b"hello!"
        ).hexdigest()

        assert a != b

    run_test("MD5", md5)
    run_test("SHA256", sha256)
    run_test("SHA512", sha512)
    run_test("Deterministic hash", deterministic)
    run_test("Different input", different_input)


# ============================================================
# CRYPTO TESTS
# ============================================================

def crypto_tests():

    section("CRYPTOGRAPHY")

    def aes():
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM

        key = AESGCM.generate_key(
            bit_length=256
        )

        nonce = os.urandom(12)

        message = b"hello world"

        cipher = AESGCM(key)

        encrypted = cipher.encrypt(
            nonce,
            message,
            None
        )

        decrypted = cipher.decrypt(
            nonce,
            encrypted,
            None
        )

        assert decrypted == message

    def chacha():
        from cryptography.hazmat.primitives.ciphers.aead import (
            ChaCha20Poly1305
        )

        key = ChaCha20Poly1305.generate_key()

        nonce = os.urandom(12)

        message = b"hello world"

        cipher = ChaCha20Poly1305(key)

        encrypted = cipher.encrypt(
            nonce,
            message,
            None
        )

        decrypted = cipher.decrypt(
            nonce,
            encrypted,
            None
        )

        assert decrypted == message

    def rsa():
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes

        private = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public = private.public_key()

        message = b"hello RSA"

        encrypted = public.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        decrypted = private.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()
                ),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        assert decrypted == message

    def ecdsa():
        from cryptography.hazmat.primitives.asymmetric import ec
        from cryptography.hazmat.primitives import hashes

        private = ec.generate_private_key(
            ec.SECP256R1()
        )

        public = private.public_key()

        message = b"hello"

        signature = private.sign(
            message,
            ec.ECDSA(
                hashes.SHA256()
            )
        )

        public.verify(
            signature,
            message,
            ec.ECDSA(
                hashes.SHA256()
            )
        )

    run_test("AES-256-GCM", aes)
    run_test("ChaCha20-Poly1305", chacha)
    run_test("RSA-2048", rsa)
    run_test("ECDSA P-256", ecdsa)


# ============================================================
# IP TESTS
# ============================================================

def ip_tests():

    section("IP CALCULATOR")

    import ipaddress

    def network():
        network = ipaddress.ip_network(
            "192.168.1.10/24",
            strict=False
        )

        assert str(
            network.network_address
        ) == "192.168.1.0"

    def broadcast():
        network = ipaddress.ip_network(
            "192.168.1.10/24",
            strict=False
        )

        assert str(
            network.broadcast_address
        ) == "192.168.1.255"

    def netmask():
        network = ipaddress.ip_network(
            "192.168.1.10/24",
            strict=False
        )

        assert str(
            network.netmask
        ) == "255.255.255.0"

    def hosts():
        network = ipaddress.ip_network(
            "192.168.1.0/24"
        )

        hosts = list(
            network.hosts()
        )

        assert str(hosts[0]) == "192.168.1.1"
        assert str(hosts[-1]) == "192.168.1.254"

    def invalid_ip():
        try:
            ipaddress.ip_address(
                "999.999.999.999"
            )

            raise AssertionError(
                "Invalid IP was accepted"
            )

        except ValueError:
            pass

    run_test("Network address", network)
    run_test("Broadcast address", broadcast)
    run_test("Netmask", netmask)
    run_test("Usable hosts", hosts)
    run_test("Invalid IP detection", invalid_ip)


# ============================================================
# PASSWORD TESTS
# ============================================================

def password_tests():

    section("PASSWORD GENERATOR")

    import secrets
    import string

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    def length():
        password = "".join(
            secrets.choice(alphabet)
            for _ in range(32)
        )

        assert len(password) == 32

    def characters():
        password = "".join(
            secrets.choice(alphabet)
            for _ in range(100)
        )

        assert all(
            char in alphabet
            for char in password
        )

    def random():
        password1 = "".join(
            secrets.choice(alphabet)
            for _ in range(32)
        )

        password2 = "".join(
            secrets.choice(alphabet)
            for _ in range(32)
        )

        assert password1 != password2

    run_test("Correct length", length)
    run_test("Allowed characters", characters)
    run_test("Random generation", random)


# ============================================================
# IMPORT TESTS
# ============================================================

def import_run_tests():

    section("MODULE IMPORTS")

    modules = [
        "modules.hashing.text2hash",
        "modules.crypto.symmetric_cipher",
        "modules.crypto.asymmetric_cipher",
        "modules.crypto.decrypt_sym",
        "modules.crypto.decrypt_asy",
        "modules.generators.generate_pswrd",
        "modules.generators.generate_UA",
        "modules.network.ipcalculator",
        "modules.network.portscanner",
        "modules.network.robots_parser",
        "modules.attack.bruteforce",
        "modules.other.pcinfo",
        "modules.ui.ui",
    ]

    for module_name in modules:

        def check(module=module_name):
            __import__(module)

        run_test(
            f"Import {module_name}",
            check
        )


# ============================================================
# FINAL REPORT
# ============================================================

def report():

    print()
    print(
        f"{CYAN}"
        "========================================"
    )

    print(
        "          MLNCHLY TEST REPORT"
    )

    print(
        "========================================"
        f"{RESET}"
    )

    print()

    print(
        f"Total tests : {total_tests}"
    )

    print(
        f"{GREEN}Passed      : "
        f"{passed_tests}{RESET}"
    )

    print(
        f"{RED}Failed      : "
        f"{failed_tests}{RESET}"
    )

    if total_tests > 0:

        score = (
            passed_tests / total_tests
        ) * 10

        print()

        if score >= 9:
            color = GREEN
        elif score >= 7:
            color = YELLOW
        else:
            color = RED

        print(
            f"{color}"
            f"SCORE       : "
            f"{score:.1f}/10"
            f"{RESET}"
        )

    print()
    print(
        f"{CYAN}"
        "========================================"
        f"{RESET}"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print(
        f"{CYAN}"
        "\nMLNCHLY AUTOMATED TESTS"
        f"{RESET}"
    )

    hashing_tests()
    crypto_tests()
    ip_tests()
    password_tests()
    import_run_tests()

    report()

    if failed_tests > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
