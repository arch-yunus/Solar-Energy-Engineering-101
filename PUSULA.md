# Gunes Enerjisi Muhendisligi 101 Pusulasi

Bu pusula, depoyu bir egitim yol haritasi gibi kullanmak isteyenler icin hazirlandi.
README genel resmi verir; bu dosya ise nereden baslanacagini, neyin hangi sirayla
calisilacagini ve pratiklerin nasil kontrol edilecegini tarif eder.

## Onerilen ilerleme sirasi

1. `01_temel_kavramlar_ve_solar_radyasyon`
   - Gunes enerjisi potansiyeli, radyasyon birimleri ve insolation kavramlari.
   - Cikis becerisi: Bir konum icin kabaca gunluk/aylik enerji potansiyeli okumak.

2. `02_fotovoltaik_pv_sistemler`
   - PV hucre, panel, invertor, sicaklik ve golgeleme kayiplari.
   - Cikis becerisi: Basit bir PV sisteminin beklenen uretimini tahmin etmek.

3. `03_solar_termal_sistemler`
   - Su isitma, pasif mimari, termal kutle ve CSP sistemleri.
   - Cikis becerisi: PV ile solar termal arasindaki uygun kullanim farkini aciklamak.

4. `04_sebeke_entegrasyonu_ve_kurulum_tipleri`
   - On-grid, off-grid, hibrit mimariler ve batarya boyutlandirma mantigi.
   - Cikis becerisi: Bir kullanim senaryosu icin dogru sistem tipini secmek.

5. `05_sistem_tasarimi_ve_ekonomi`
   - Yuk analizi, alan-kapasite tahmini, CAPEX/OPEX, amortisman ve ROI.
   - Cikis becerisi: Kucuk bir konut sistemi icin taslak kapasite ve geri odeme hesabi yapmak.

## Pratik araclar

- `scripts/pv_sistem_boyutlandirma.py`: Aylik tuketimden gerekli PV kapasitesini tahmin eder.
- `scripts/roi_hesaplama.py`: Kurulum maliyeti, yillik tasarruf ve bakim gideri ile geri odeme hesaplar.
- `scripts/validate_academy.py`: Depodaki temel dosya ve klasorlerin varligini kontrol eder.

## Calisma onerisi

Her modul icin su donguyu kullan:

1. Modul README'sini oku.
2. Birimleri ve temel formulleri not al.
3. Mini uygulamayi kagit ustunde coz.
4. Varsa script ile sonucu kontrol et.
5. Sonucu kendi sehrin, catin veya tuketim degerlerinle tekrar hesapla.

## Bitirme projesi

Kucuk bir konut veya atolye icin asagidaki teslimleri hazirla:

- Aylik elektrik tuketimi ve gunluk ortalama yuk.
- Konum icin guneslenme varsayimi.
- Panel kapasitesi ve yaklasik alan ihtiyaci.
- Invertor secim mantigi.
- Batarya gerekip gerekmedigi.
- Kurulum maliyeti, yillik tasarruf ve tahmini amortisman suresi.

