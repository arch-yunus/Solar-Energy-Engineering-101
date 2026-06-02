# Modul 2: Fotovoltaik (PV) Sistemler

Bu modul, gunes isigini dogrudan elektrige ceviren PV sistemlerin temel
bilesenlerini ve performansini inceler.

## Ogrenme hedefleri

- Fotovoltaik etkinin temel mantigini aciklamak.
- Panel, string, MPPT, invertor ve combiner box rollerini ayirt etmek.
- Sicaklik, golgeleme, kirlenme ve yonelim kayiplarini hesaba katmak.
- STC ve NOCT gibi panel veri sayfasi kosullarini okumak.

## PV sistem bilesenleri

| Bilesen | Gorev |
| --- | --- |
| PV panel | Isigi DC elektrige cevirir. |
| Invertor | DC elektrigi AC elektrige cevirir ve sebeke ile senkronlar. |
| MPPT | Panel dizisinin maksimum guc noktasinda calismasini saglar. |
| Kablo ve koruma | Enerjiyi guvenli tasir, kisa devre ve asiri akima karsi korur. |
| Izleme sistemi | Uretim, ariza ve performans takibini saglar. |

## Uretim tahmini

Yaklasik gunluk uretim:

```text
gunluk_uretim_kWh = kurulu_guc_kW x peak_sun_hour x performans_orani
```

Ornek:

```text
5 kW x 4.5 saat x 0.78 = 17.55 kWh/gun
```

## Mini uygulama

4.5 kWh/m2/gun ortalama guneslenmeye sahip bir bolgede, aylik 450 kWh tuketen
bir ev icin gerekli PV kapasitesini `scripts/pv_sistem_boyutlandirma.py` ile
tahmin et.

