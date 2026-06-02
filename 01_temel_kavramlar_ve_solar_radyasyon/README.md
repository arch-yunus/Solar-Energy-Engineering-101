# Modul 1: Temel Kavramlar ve Solar Radyasyon

Bu modul, gunes enerjisinin fiziksel temelini ve sahada en cok kullanilan
radyasyon birimlerini tanitir.

## Ogrenme hedefleri

- Gunes sabiti, irradiance ve irradiation kavramlarini ayirt etmek.
- W, Wh, kWh, W/m2 ve kWh/m2/gun birimlerini dogru kullanmak.
- Guneslenme suresi ile enerji uretimi arasindaki farki aciklamak.
- Konum, mevsim, egim ve atmosfer kosullarinin potansiyele etkisini yorumlamak.

## Temel kavramlar

| Kavram | Kisa aciklama |
| --- | --- |
| Irradiance | Anlik gunes gucu yogunlugu, genelde W/m2 ile verilir. |
| Irradiation | Belirli surede birim alana gelen enerji, genelde kWh/m2 ile verilir. |
| Peak sun hour | Bir gunluk enerjinin 1000 W/m2 esdegeri saat cinsinden ifadesi. |
| Albedo | Yuzeyden yansiyan gunes isinimi orani. |

## Basit hesap

Bir bolgede ortalama 5 kWh/m2/gun gunes enerjisi varsa ve 2 m2 panel alani
kullaniyorsak, teorik gelen enerji:

```text
5 kWh/m2/gun x 2 m2 = 10 kWh/gun
```

Panel verimi yuzde 20 ise elektrik enerjisi yaklasik:

```text
10 kWh/gun x 0.20 = 2 kWh/gun
```

Gercek sistemde sicaklik, kablo, invertor, kirlenme ve golgeleme kayiplari
eklenir. Bu nedenle tasarimlarda performans orani kullanilir.

## Mini uygulama

`data/turkiye_gunes_potansiyeli.csv` dosyasindan bir il sec. Ortalama guneslenme
degerini kullanarak 1 kW kurulu gucun gunluk uretimini tahmin et.

