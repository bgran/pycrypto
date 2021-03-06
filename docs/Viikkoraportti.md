# Viikkoraportit

## 6.11.2021

Aikaa käytetty projektiin: 12 tuntia.

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
- avainparin generointi
- salaus
- purkaminen
Nämä kolme annettuna on mahdollista laajentaa asioita huomattavasti.


## 13.11.2021

Aikaa käytetty projektiin: 7 tuntia.

### Edistys tällä viikolla

Toteutettiin unittestit Pythonin unittest -Python -standaardikirjaston parissa.
Toteutettiin kolme testi-tapausta RSA -moduuliin liittyen. Eli ensimmäinen tarkistaa
onko generoitu luku alkuluku. Toinen tarkistaa onko ketju:
1. p = rsa.Prime(...).gen_prime()
2. q = rsa.Prime(...).gen_prime()
3. Avainpari: ((e,n), (d,m)) = rsa.gen_keypair(p, q)
4. cleartext = "hello world"
5. ciphertext = rsa.encrypt((e,n), cleartext)
6. uusiclear = rsa.decrypt((d,m), ciphertext)
7. Onko: uusclear == cleartext
Eli jokaista ajoa varten kehitetään kaksi 1024 -bittisiä alkulukuja joita käytetään
testaamiseen. Avaimen koko on siis parametrisoitu koodissa, ja 2048 -bittinen
alkulukupari kestää 90 sekunttia laskea tehokkaalla XEON -koneella.

### Ohjelman edistus

Eli kirjoitettiin tällä viikolla myös AES -stubi.

### Opitut asiat

Testicaset tehdään pienillä alkuluvuilla koska isot sellaiset kestävät kauan
generoida. Havaittiin että ** -operaattorin tehokkuus on suurinpiirtein pow()
-metoodin tasoinen. Tultiin lopputulokseen että RSA -salaus tuottaa suuria
arvoja salattuja tavuja. Suuria tarkoittaa siis isoja lukuja.

### Epäselviä asioita ja vaikeuksia

On erittäin epäselvää mitä sovelluksen piirissä tehdään testikattavuus. Tarkoitaako
testikattavus siis että mahdollisimman paljon toteutusta saadaan testattua? Checkstyle
on myös epäselvä asia. Koodin laadun seuranta on epäselvää eikä selviä tarpeeksi
kurssien materiaaleista.

Miten tuntikirjanpito toimii projektissa?

### Mitä seuraavaksi?

Ohjelmiston pitää toteuttaa vakaita kryptauksia, eli komentorivi-käyttöliittymä
tulee toimia ilman ongelmia.


## 20.11.2021

Aikaa käytetty projektiin: 10 tuntia

### Edistys tällä viikolla

Toteutettiin vakaa salaus ja salauksen purkaminen tiedostojärjestelmästä haetuilla
avaintietueilla. Toteutettiin myös alkuosa AES -datan enkryptaamisesta.

### Opitut asiat

RSA toimii harvinaisen huonosti jos lukuarvoilla algoritmissä on jotain epämääräistä
kuten bitin heitto väärän suuntaan. Todettiin että paras tapa havaita hyökkäys
salausta vastaan jos softa kuolee OverflowError -poikkeukseen.

Epävaliidin avainparin käyttö siis ei tulkita missään vaiheessa, vaan softa kuolee nopeasti
jos sille yritetään antaa vääriä avaimia.

### Epäselviä asioita

Virhekäsittely on avoinna vielä. Eli pitääkö olla joku määritelty palautusarvo prosessin
exitoinnista eri operaatioille? Vai sopiiko että käyttää vain yhtä arvoa eli 1, joka on
erimpi kuin 0.

Tiedosto-järjestelmään kirjoitettava salattu viesti toimii aes.py:ssä määrittelyillä
delimitoreiden kanssa, eli RSA -salatut asia ovat ensin paketissa. Eli AES-enkryptaatio
voisi toimia jonkinlaisella PGP:stä tutulla armored ascii -toteutuksella. Myös analyyttinen
hyökkäys softaa vastaan on siis RSA:n ns. ECB, eli Electronic Code Book -tapainen
lähestymistapa koodaattuun AES -salaisuuteen on todellinen, koska mitään suojausta ei ole
toteutettu. Pitää katsoa mitä ja miten PGP tekee asiaan, eli miten estää datan
vuoto suoraan itse salatusta RSA-datasta, koska salaisuus on sama kaikille samoille merkeille.
Tämä on hankala asia. Myös suurempien avainten kanssa RSA -salauksen
koko on aika iso. En tiedä mitä asialle voi tehdä.

### Mitä seuraavaksi?

Pitää toteuttaa kattava Unit testit. Myös laitettava softa toimimaan siten että se
ei kirjoita yli tiedostoja ennenkuin se on saanut jotain laitettavaa niihiin. Eli
tiedostot kirjoitetaan vasta kun operaatiota ovat tehtyjä ja ne ovat toimivia. Myös
AES -kryptauksen dekryptausoperaatio pitää toimia hyvin tai ainakin oikein.

## 06.12.2012

Aikaa käytetty projektiin: 14 tuntia

### Edistys tällä viikolla

Muutettiin rsa.py koodi pylint -yhteensopivaksi. Tehtiin myös vertaisarviointi.

## Ohjelman edistyminen

Sairauden vuoksi ei koodia lisätty

## Mitä opin?

Opin että pylint valittaa tietyistä asioita jotka ovat ehkä vähän kaukaa haettuja.

## Mikä on epäselvää?

Ei juuri mikään.

## Mitä seuraavaksi?

Koodin käsittely eli toiminnallisuus on tehty riittävän pitkälle, vakausbugien
korjausta.

