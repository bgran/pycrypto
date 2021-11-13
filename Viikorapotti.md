# Viikkoraportit

## 6.11.2021

### Suunnitelu

Pycrypto -softan suunnittelu aloitettiin minun henkilökohtaisesta kiinnostukessta
salaus-menetelmiä kohtaan. Eli RSA todettiin siis sopivaksi aiheeksi. Aiheessa on
monta kiinnostavaa asiaa yhdessä. Esim. isojen alkulukujen generointi on kiinostava
aihe. Myös teoria RSA:n taustalla kiinnostaa todisteluun siitä että RSA:n turvallisuus
on kiinni isojen lukujen faktorisoinnin kanssa. Eli lukujen faktorointtin ei ole 
olemassa tehokkasta algoritmiä.

### Toteutus

Toteutus aloitettiin Python (3) -kielen toteutuksen parissa. Identifioitiin siis ongelma-
kohtia toteutuksessa. Vastaan tuli aiheita kuten lukujen primarility, eli numeroiden
alkuluvullisuus. Nopea toteutus teki siis isoja alkulukuja melko nopeaan tahtiin. Eli
käytettävien alkulukujen suuruus siis parametria, kuten on myös Rabin-Miller testin
iteraatoiden määrä. Ison alkuluvun generointi on aikaavievää. Tästä päästään itse asiaa
eli miten tehdä softasta käyttökelpoinen.

Käyttökelpoisuus siis toimii $PYCRYPTO_DIR -ympäristömuuttujen varassa, eli se tekee
hakemistoja ja asettaa niiihin $PYCRYPTO_DIR/secret.key ja $PYCRYPTO_DIR/public.key
-tiedostot. Näin saamme tehtyä tehokkaasti testaustympäristön.

Salattava data ei siis ole RSA:lla salattua, koska Bruce Schneier kirjoitti Applied
Cryptographics -kirjassaan että RSA on suunnilleen sata kertaa hitaampaa kuin DES-
salauksen nopeus. Eli softa tekee tiedostoni, jossa on ensin otsikkotietueena AES
-avain ja sen jälkeen AES-kryptattu salattu tiedosto. AES on symmetrinen salaus
-menetelmä, joka toimii 128, 192 tai 256 -bittisten avainten kanssa. Eli koska
RSA:n hitaus on huomattava niin vain AES -avain kryptataan ja AES -salattu data tulee
RSA-salatun AES -salasanan perään.

### Lessons learned

Tällä viikolla opin että Pythonin ** operaattori on tuskallisen hidas verrattuna 
sisäänrakennetun pow() -funktioon verrattuna.

### Edistysaskeleet

Softa osaa tehdä avainparit, ja salata dataa, ja purkaa sitä annettulla avaimella.

### Epäselvyyksiä

Ei mitään raportoitavia epäselvyyksiä. Kävimme läpi Hannu Kärnan kanssa ohjelmistoa
ja päädyimme sopivaan laajuuteen ja ns. scopeen joka softalla on.

### Mitä teen seuraavaksi
Tarkoituksena on tehdä loppuun asti asiat jotka liityvät salaus-ympäristön kokoamiseen.
Tarvitaan toimivat softat jotka tekevät mitä on tarkoitus tehdä:
        o avainparin generointi
        o salaus
        o purkaminen
Nämä kolme annettuna on mahdollista laajentaa asioita huomattavasti.


## 13..11.2021

### Edistys tällä viikolla

Toteutettiin unittestit Pythonin unittest -Python -standaardikirjaston parissa.
Toteutettiin kolme testi-tapausta RSA -moduuliin liittyen. Eli ensimmäinen tarkistaa
onko generoitu luku alkuluku. Toinen tarkistaa onko ketju:
	* p = rsa.Prime(...).gen_prime()
	* q = rsa.Prime(...).gen_prime()
	* Avainpari: ((e,n), (d,m)) = rsa.gen_keypair(p, q)
	* cleartext = "hello world"
	* ciphertext = rsa.encrypt((e,n), cleartext)
	* uusiclear = rsa.decrypt((d,m), ciphertext)
	* Onko: uusclear == cleartext
Eli jokaista ajoa varten kehitetään kaksi 1024 -bittisiä alkulukuja joita käytetään
testaamiseen. Avaimen koko on siis parametrisoitu koodissa, ja 2048 -bittinen
alkulukupari kestää 90 sekunttia laskea tehokkaalla XEON -koneella.

### Ohjelman edistus

Eli kirjoitettiin tällä viikolla myös AES -stubi.

### Opitut asiat

Testicaset tehdään pienillä alkuluvuilla koska isot sellaiset kestävät kauan
generoida. Havaittiin että ** -operaattorin tehokkuus on suurinpiirtein pow()
-metoodin tasoinen. Tultiin lopputulokseen että RSA -salaus tuottaa suuria
arvoja salattuja tavuja. Suuria tarkoittaa siis