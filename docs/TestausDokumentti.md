# Testausdokumentti

## Yksikkötestaus

Ohjelmistossa on kolme asiaa joita voi testata:

1. Lukujen generointi.
2. Lukujen testaus alkuluvuiksi.
3. RSA salaus.
4. RSA avaus.

### Ohjelmistologiikka

Testataan RSA -moduulin avaintenluontilogiikka.

## Testikattavuus

Coverage testitulokset saadaan [tästä](coverage_20211206.txt).

## Järjestelmätestaus

Sovellusta on testattu käsin eikä suurempia ongelmia ole esiitynyt.

## Suorityskykytestaus

Ohjelman suorituskyky on erittäin hyvä. Se laskee 200MiB -salatun tai
salattavan tiedon nykyaikaisella XEON-koneella noin 100MB/sec vauhdilla.
Tästä huomattavat määrä aikaa menee RSA-salauksen dekryptaamiseen /
enkryptaamiseen. Kun RSA -salaisuus on purettu niin kryptaus on erittäin
tehokas operaatio.

Tehokasta alkulukujen generointia siis tapahtuu melko hitaasti. Keskimääräisesti
21 sekunttia menee alkuluvun generointiin.

Itse salattavan tiedoston koko kasvattaa suoritusaikaa lineäärisesti. O(n)

## Testien suorittaminen

Ohjelman testit voi suorittaa ajamalla

```
make tests
```
