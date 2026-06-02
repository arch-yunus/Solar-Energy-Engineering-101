"""Depo iskeletinin temel egitim dosyalarini kontrol eder."""

from __future__ import annotations

from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "PUSULA.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "01_temel_kavramlar_ve_solar_radyasyon/README.md",
    "02_fotovoltaik_pv_sistemler/README.md",
    "03_solar_termal_sistemler/README.md",
    "04_sebeke_entegrasyonu_ve_kurulum_tipleri/README.md",
    "05_sistem_tasarimi_ve_ekonomi/README.md",
    "data/turkiye_gunes_potansiyeli.csv",
    "scripts/pv_sistem_boyutlandirma.py",
    "scripts/roi_hesaplama.py",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED_PATHS if not (root / path).exists()]

    if missing:
        print("Eksik dosyalar:")
        for path in missing:
            print(f"- {path}")
        raise SystemExit(1)

    print(f"Tamam: {len(REQUIRED_PATHS)} temel dosya bulundu.")


if __name__ == "__main__":
    main()
