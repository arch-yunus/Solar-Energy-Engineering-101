"""Basit solar yatirim geri odeme hesabi.

Ornek:
    python scripts/roi_hesaplama.py --kurulum-maliyeti 180000 --yillik-tasarruf 42000
"""

from __future__ import annotations

import argparse


def hesapla_geri_odeme(
    kurulum_maliyeti: float,
    yillik_tasarruf: float,
    yillik_bakim: float,
) -> tuple[float, float]:
    if kurulum_maliyeti <= 0:
        raise ValueError("Kurulum maliyeti pozitif olmalidir.")
    if yillik_tasarruf <= 0:
        raise ValueError("Yillik tasarruf pozitif olmalidir.")
    if yillik_bakim < 0:
        raise ValueError("Yillik bakim negatif olamaz.")

    net_yillik_fayda = yillik_tasarruf - yillik_bakim
    if net_yillik_fayda <= 0:
        raise ValueError("Net yillik fayda pozitif olmalidir.")

    geri_odeme_yili = kurulum_maliyeti / net_yillik_fayda
    yillik_roi = net_yillik_fayda / kurulum_maliyeti
    return geri_odeme_yili, yillik_roi


def main() -> None:
    parser = argparse.ArgumentParser(description="Solar yatirim geri odeme suresi hesaplar.")
    parser.add_argument("--kurulum-maliyeti", type=float, required=True, help="Toplam kurulum maliyeti")
    parser.add_argument("--yillik-tasarruf", type=float, required=True, help="Yillik fatura tasarrufu")
    parser.add_argument("--yillik-bakim", type=float, default=0, help="Yillik bakim gideri")
    args = parser.parse_args()

    geri_odeme_yili, yillik_roi = hesapla_geri_odeme(
        args.kurulum_maliyeti,
        args.yillik_tasarruf,
        args.yillik_bakim,
    )

    print(f"Tahmini geri odeme suresi: {geri_odeme_yili:.1f} yil")
    print(f"Basit yillik ROI: %{yillik_roi * 100:.1f}")


if __name__ == "__main__":
    main()

