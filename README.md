# encryptions
Assignment of foundations of privacy course:

- RSA encryption/decryption
- Elgamal encryption/decryption
- Diffie-Hellman key exchange
- Elgamal re-encryption
- Elgamal Universal re-encryption


run locally:
```
  pip3 install -r requirements.txt
  python3 app.py
```

run with docker:
```
  docker build . -t encryption
  docker run --rm -it -p 5000:5000 encryption
```
