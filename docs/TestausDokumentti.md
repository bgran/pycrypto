# Testausdokumentti

## Yksikkötestaus

Ohjelmistossa on kolme asiaa joita voi testata:

1. Lukujen generointi.
2. Lukujen testaus alkuluvuiksi.
3. RSA salaus.
4. RSA avaus.

### Ohjelmistologiikka

Testataan RSA -moduulin avaintenluontilogiikka. Testataan myös
kryptauksen toimivuuttaa ja nopeutta.

## Testikattavuus

Coverage testitulokset saadaan [tästä](docs/coverage_20211231.txt).

## Järjestelmätestaus

Sovellusta on testattu käsin eikä suurempia ongelmia ole esiitynyt.

## Suorityskykytestaus

Ohjelman suorituskyky on erittäin hyvä. Se laskee 200MiB -salatun tai
salattavan tiedon nykyaikaisella XEON-koneella noin 100MB/sec vauhdilla.
Tästä huomattavat määrä aikaa menee RSA-salauksen dekryptaamiseen /
enkryptaamiseen. Kun RSA -salaisuus on purettu niin kryptaus on erittäin
tehokas operaatio.

Tehokasta alkulukujen generointia siis tapahtuu melko hitaasti. Keskimääräisesti
21 sekunttia menee alkuluvun generointiin. Patolooginen 8192-bittinen alkulukupari
kesti kehittää `gen_rsa.py` -ohjelmalla kymmenen tuntia nopealla XEON -koneella.

Ohjelmisto siis tekee melko suoraviivaisen lukemisen ja kirjoituksen bufferi-muuttujaan 
joka varaa muistia sen tarpeisiin. Tässä on optimoimisen mahdollisuus ohjelmiston koon
suhteen muistijäljessä.

Testattiin myös 8192 -bittinen p ja q arvot joiden vaikutus enkryptaamiseen oli 10
sekunttia per selkokielinen tavu ja dekryptaaminen kului 13 sekunttia per 
kryptattu tavu.

Itse salattavan tiedoston koko kasvattaa suoritusaikaa lineäärisesti. O(n)

## Testien suorittaminen

Ohjelman testit voi suorittaa ajamalla

```
make tests
```
