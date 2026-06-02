# Modul 4: Sebeke Entegrasyonu ve Kurulum Tipleri

Bu modul, PV sistemlerin sebeke ve depolama ile nasil calistigini anlatir.

## Ogrenme hedefleri

- On-grid, off-grid ve hibrit sistemleri ayirt etmek.
- Mahsuplasma, oz tuketim ve fazla uretim kavramlarini aciklamak.
- Batarya kapasitesi ile otonomi suresi arasindaki iliskiyi kurmak.
- Guvenlik, koruma ve mevzuat basliklarini tasarim kararlarina baglamak.

## Sistem tipleri

| Tip | Avantaj | Sinir |
| --- | --- | --- |
| On-grid | Dusuk maliyet, sebeke yedegi | Kesintide calismayabilir |
| Off-grid | Sebekeden bagimsiz | Batarya maliyeti yuksektir |
| Hibrit | Yedekleme ve oz tuketim dengesi | Kontrol ve maliyet daha karmasiktir |

## Batarya yaklasimi

Basit kapasite tahmini:

```text
batarya_kWh = gunluk_yuk_kWh x otonomi_gunu / kullanilabilir_dejarj_orani
```

Ornek:

```text
10 kWh/gun x 2 gun / 0.80 = 25 kWh
```

## Mini uygulama

Gunluk 8 kWh tuketimi olan bir yayla evi icin 2 gun otonomi hedefiyle batarya
kapasitesini hesapla. LFP batarya icin yuzde 80 kullanilabilir deger varsay.

