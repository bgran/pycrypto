## Käyttöohje

Ohjelman suoritus ja asennus tapahtuu:

### Asennus

pip3 install pycryptodome

### Ohjelman suoritus

Ajettavat ohjelmat ovat siis:

1. gen_rsa.py
2. encrypt.py
3. decrypt.py

### Sovelluksen testaus

    swift (~/pycrypto) 0 % ./gen_rsa.py 
    Enter key file name (default is /home/bgran/.pycrypto/key)> avain
    Prime found, seconds elapsed 10.77
    Prime found, seconds elapsed 10.635
    Generation of e and d elapsed 0.004 seconds
    Generation of a keypair took 21.414 seconds
    swift (~/pycrypto) 0 % ./encrypt.py -c avain.pub -i linux-source.tar.gz -o linux-source.tar.gz.enc 
    Encryption elapsed 2.095 seconds (95.582MiB/sec)
    swift (~/pycrypto) 1 % ./decrypt.py -c avain -i linux-source.tar.gz.enc -o puhdas
    Decryption elapsed 2.004 seconds (99.963MiB/sec)

