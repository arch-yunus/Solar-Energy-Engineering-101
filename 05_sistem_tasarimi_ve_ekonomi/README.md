# Modul 5: Sistem Tasarimi ve Ekonomi

Bu modul, teknik tasarimi ekonomik kararlarla birlestirir. Amac, gercekci
varsayimlarla okunabilir bir fizibilite taslagi hazirlamaktir.

## Ogrenme hedefleri

- Aylik faturadan gunluk enerji ihtiyacini cikarmak.
- Guneslenme, performans orani ve kapasite arasindaki iliskiyi kurmak.
- Alan ihtiyacini panel gucu ve panel verimiyle tahmin etmek.
- Basit geri odeme ve ROI hesaplamak.

## Tasarim akisi

1. Aylik kWh tuketimini belirle.
2. Gunluk ortalama tuketimi hesapla.
3. Konum icin peak sun hour degerini sec.
4. Performans oranini belirle.
5. Gerekli kurulu gucu hesapla.
6. Alan, invertor ve batarya gereksinimini yorumla.
7. Maliyet ve tasarruf varsayimlariyla geri odemeyi hesapla.

## Basit kapasite formulu

```text
gerekli_kW = gunluk_tuketim_kWh / (peak_sun_hour x performans_orani)
```

## Mini uygulama

Aylik 600 kWh tuketen, 4.8 peak sun hour varsayilan ve performans orani 0.78
olan bir ev icin sistem kapasitesini hesapla. Ardindan `scripts/roi_hesaplama.py`
ile amortisman suresini bul.

