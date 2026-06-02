"""Basit PV sistem boyutlandirma araci.

Ornek:
    python scripts/pv_sistem_boyutlandirma.py --aylik-tuketim 450 --psh 4.5
"""

from __future__ import annotations

import argparse


def hesapla_kapasite(
    aylik_tuketim_kwh: float,
    peak_sun_hour: float,
    performans_orani: float,
    gun_sayisi: int,
) -> tuple[float, float]:
    if aylik_tuketim_kwh <= 0:
        raise ValueError("Aylik tuketim pozitif olmalidir.")
    if peak_sun_hour <= 0:
        raise ValueError("Peak sun hour pozitif olmalidir.")
    if not 0 < performans_orani <= 1:
        raise ValueError("Performans orani 0 ile 1 arasinda olmalidir.")
    if gun_sayisi <= 0:
        raise ValueError("Gun sayisi pozitif olmalidir.")

    gunluk_tuketim = aylik_tuketim_kwh / gun_sayisi
    gerekli_kw = gunluk_tuketim / (peak_sun_hour * performans_orani)
    return gunluk_tuketim, gerekli_kw


def main() -> None:
    parser = argparse.ArgumentParser(description="PV sistem kapasitesi tahmini yapar.")
    parser.add_argument("--aylik-tuketim", type=float, required=True, help="Aylik tuketim (kWh)")
    parser.add_argument("--psh", type=float, required=True, help="Peak sun hour (saat/gun)")
    parser.add_argument("--performans-orani", type=float, default=0.78, help="Sistem performans orani")
    parser.add_argument("--gun", type=int, default=30, help="Aylik gun sayisi")
    args = parser.parse_args()

    gunluk_tuketim, gerekli_kw = hesapla_kapasite(
        args.aylik_tuketim,
        args.psh,
        args.performans_orani,
        args.gun,
    )

    print(f"Gunluk ortalama tuketim: {gunluk_tuketim:.2f} kWh/gun")
    print(f"Onerilen minimum PV kapasitesi: {gerekli_kw:.2f} kW")
    print(f"Pratik tasarim araligi: {gerekli_kw * 1.05:.2f} - {gerekli_kw * 1.20:.2f} kW")


if __name__ == "__main__":
    main()

