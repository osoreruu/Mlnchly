[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge&logo=pytest)](https://github.com/osoreruu/Mlnchly)   ![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)   ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)   ![Repo Size](https://img.shields.io/github/repo-size/osoreruu/Mlnchly)   ![OS Support](https://img.shields.io/badge/os-linux%20%7C%20macos%20%7C%20windows-lightgrey)

***Mlnchly*** is a crypto tool for calculating **SHA-1**, **SHA-256**, **Blake2b**, and **SHA-3** hashes (including **384**-bit and **512**-bit versions). ***Mlnchly*** also supports data encryption using **AES-256** and **ChaCha20**; while the key is generated randomly, you can also provide your own **IV**, and the key remains visible after encryption.

***Installation***:

git clone https://github.com/osoreruu/Mlnchly.git

cd Mlnchly

pip install -r requirements.txt

***Usage***:

python main.py

Then **select** desire tool by **number's**

***Advantages of my tool***: modularity, lightweight design, and speed.

***Functions***:

**Hashing**: **SHA1**, **SHA256**, **SHA3_384**, **SHA3_512**, **Blake2b**
**Symmetric** Encrypt: **AES256**, **ChaCha20**
**Asymmetric** Encrypt: **RSA2048**, **ECC256**
**Decrypting** of **Symmetric and Asymmetric Encryption's**
**Generating password** of every length, used safe **import secrets**.
**Brute-Forcing** password with **RockYou.txt** and dump method.
