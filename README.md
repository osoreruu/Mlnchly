***Mlnchly*** is a crypto tool for calculating **SHA-1**, **SHA-256**, **Blake2b**, and **SHA-3** hashes (including **384**-bit and **512**-bit versions). ***Mlnchly*** also supports data encryption using **AES-256** and **ChaCha20**; while the key is generated randomly, you can also provide your own **IV**, and the key remains visible after encryption.

***Installation***:

git clone https://github.com/osoreruu/Mlnchly.git

cd Mlnchly

pip install -r requirements.txt

***Usage***:

python main.py

Then **select** desire tool by **number's**

***Advantages of my tool***: modularity, lightweight design, and speed.

***Function's***:
Hashing: **SHA1**, **SHA256**, **SHA3_384**, **SHA3_512**, **Blake2b**
Symmetric Encrypt: **AES256**, **ChaCha20**
Asymmetric Encrypt: **RSA2048**, **ECC256**
Decrypting of **Symmetric and Asymmetric Encryption's**
Generating passsword of every length, used safe **import secrets**.
