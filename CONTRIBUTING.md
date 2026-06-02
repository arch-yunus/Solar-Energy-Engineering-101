# Katkida Bulunma Rehberi

Katkilar; yeni ders notu, duzeltme, hesaplama ornegi, veri kaynagi veya mini proje
seklinde olabilir.

## Icerik ilkeleri

- Teknik ifadeleri once sade dille acikla, sonra formulu ver.
- Birim belirtmeden sayisal deger kullanma.
- Varsayimlari acik yaz: konum, guneslenme saati, sistem verimi, fiyat vb.
- Kaynak eklerken mumkunse resmi kurum, akademik yayin veya uretici veri sayfasi kullan.
- Hesap orneklerinde sonucu tek sayi olarak degil, adim adim ver.

## Dosya duzeni

- Her yeni konu ilgili modul klasorune eklenmelidir.
- Kapsamli bir hesaplama araci eklenecekse `scripts/` altina konmalidir.
- Tekrarlanabilir veri setleri `data/` altinda tutulmalidir.

## Kontrol

Degisiklikten sonra su komutu calistirilabilir:

```powershell
python scripts\validate_academy.py
```

