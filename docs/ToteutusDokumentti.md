# Toteutusdokumentti

Ohjenuora tehokkaan ja turvallisen datan enkoodamiseen ja dekoodaamiseen.

## Ohjelman yleisrakenne

1. `gen_rsa.py`
	- Luokka RSA -avainparin luomiseen
	- Funktiot:
		- `main`
			- Luo uuden RSA-avainparin ja tallentaa sen tiedostojärjestelmään.
		- `crypto_test`
			- Testejä varten tehty stubi joka luo avainparin ja salaa ja avaa datoja.

2. `rsa.py`
	- `Prime` 
		- Luokka tekee alkulukuja.
		- Tärkeät metoodit:
			- `__init__`
			- `gen_prime`
	- `gen_keypair`
	- `encrypt`
	- `decrypt`
	- `RSA_Container`
		- Enkapsuloi datan palottelemisen eteenpäin.

3. `encrypt.py`
	- Kryptaa julkisella avaimella datat.

4. `decrypt.py`
	- Purkaa salauksen salaisella avaimella.

3. `aes.py`
    - Luokka AES -salauksen enkapsuloinniksi.

## Ohjelman puutteet ja parannusehdotukset

RSA -salaisuus tallennetaan ECB -moodissa suoraan kryptattavaan tiedostoon
joka saattaa vuotaa siis tietoja käytetystä AES-salaisuudesta koska
salattu arvo cipher tavulle cleartext on sama aina kun cleartext tulee vastaan
salatussa datassa, eli pystyy tekemään johtopäätöksiä salatusta datasta.

## Lähteet

- Applied Cryptography, Second Edition, Bruce Schneier
- AES -esimerkit https://pycryptodome.readthedocs.io/en/latest/src/examples.html

