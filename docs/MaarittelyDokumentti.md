# Määrittely

## Aihe

Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (perioodi II) Laboratorio-työskentely
Toeutuskieli: Python (3)
Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma.
Kieli: Suomi

Toteutetaaan RSA-salausalgoritmi (Rivest-Shamir-Adleman, 1978). RSA on assymetrinen kryptoalgoritmi
jolla on mahdollista salata, purkaa ja allekirjoittaa tietoa. RSA on turvallinen koska isojen
lukujen tekijöihin jako on hyvin hankala operaatio.

## Käyttötapauksia

Ohjelmisto siis toteuttaa RSA -salauksen puhtaasti ainoastaan Pythonissa, mitään
laajennuksia Python C-API:a vastaan ei tehdä. Ohjelmiston käyttötapaukset ovat muotoa:

* Käyttäjä tarvitsee komennon joka luo RSA-avainparin.
* Avainparin julkinen osa on jaettavissa.
* Avainparin salainen osa on piillotettava.
* Komento "encrypt" koodaa selkokielisen datan ja koodaa RSA:lla AES -avaimen.
* Komento "decrypt" purkaa AES -avaimen RSA -salauksesta ja avaa sillä ns. cipher-tekstin.
* Komentokehotteessa annettu ympäristömuuttuja eli. $PYCRYPTO_DIR on annettu hakemisto josta käsin saa julkisen ja salaisen avaimen.
* On mahdollista tehdä useita avainpareja yhdelle käyttäjälle.
* Ohjelmisto ei tue salasanojen asettaimsta avainparilla.

## Ohjelmiston toiminta

### Matematiikkaa RSA:n osalta

Ohjelmisto toimii siis diskreettisen Python-koodien kanssa. Mitään erillisiä laajennuksia
ei siis tehdä. Ohjelmisto toimii siis Pythonin integer -tyypin muuttujien kanssa, joiden
koko on mielivaltainen. Tämä tarkoittaa ettei erillistä BigInt -tyyppistä muuttujaa tarvita.
RSA -salausken oleellinen osa eli kryptaus tekee muotoa:

>	c = m ** e mod n

Jossa c on cipher teksti, m on tieto jota puretaan, e on (p-1)(q-1), joka on huomattavan
suuri arvo, ja n on p ja q kerrottuna. Tämä toimii hankalasti Pythonin ** operaattorin kanssa
joka tulee toteutta pow -sisäänrakennettua funktiota. Havaittiin toimivaksi testauksen
ohessa. Pythonin ** operaattori ei toimi ajassa joka on hyväksyttävä.

### RSA toteutus

Luodessa uusia alkulukuja RSA:n p ja q -arvoille käytetään ensin ykinkertaista generoitua
taulua esim. kaikista alkuluvuista jotka ovat esim. kahdesta kymmeneentuhanteen, niiden
generoiminen on suhteellisen pieni operaatio verrattuna olematta käyttämättä aikaa niiden
antamaa osviittaa siitä että annettu luku on alkuluku. Ohjelmisto generoi siis RSA-
avainparin generoinnin yhteydessä aina uudestaan jonkin pienen luvun verran alkulukuja
joita vastaan voidaan verrata onko luku jaettavissa alkulukujen kanssa. Itse todennäköisyys
siitä että annettu luku on alkuluku saadaan Rabin-Miller -alkuluku -testin kanssa, joka
laskee todennäkisyyksiä alkuluvullisuudesta, eli iteroitaessa Rabin-Miller testiä saadaan
todennäköisesti alkuluku generoitua. On vielä hieman tutkittava miten monta iteraatiota
Rabin-Milleriä on parasta ajaa. Eli on perusteltua tuhlata hieman avainmahdollisuuksia
tekemällä ensimmäisen p ja q -arvojen MSB, eli eniten merkitsevä bitti yhdeksi. Tämä estää
tapaukset joissa avainpari ei ole ikinä pienempi kuin 1024 -bittiä.

## Aikavaativuus

Koska softa on tehty järkevästi ei nopeudella oli suurta merkitystä sen suhteen, että miten
nopeasti salataan dataa. Eli RSA:n osalta tulee aikavaativuuksia:
    - Rabin-Miller alkulukutesti
        - Aikavaativuus: O(k log^3 n), missä k on iteraatoiden määrä ja n on testattava luku.
    - Alkulukujnen p ja q kehittäminen
        - Aikavaativuus O(log n)
    - n = p * q
        - Aikavaativuus (n^2)
    - Enkryptio ja dekryptio
        - Modulus-operaation laskenta on pahimassa tapauksessa O(M(n)2^k).

