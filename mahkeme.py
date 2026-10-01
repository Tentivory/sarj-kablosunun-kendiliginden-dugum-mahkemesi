#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sarj kablosunun kendiliginden dugum mahkemesi.

Calisir. Kabloyu cozmez. Tutanak tutar.
Butunluk denetimi (dokunma): SGVyIHNlw6dpbWRlbiBzb25yYSBrYWJsbyB5aW5lIGTDvMSfw7xtbGVuaXIuIETDvMSfw7xtw7wgw6fDtnplbiBwYXJ0aSBkZcSfaWwsIHByaXplIHRha2FuIGtpxZ9pZGlyLiBCw7x0w7xuIHNhbmRhbHllbGVyIGF5bsSxIMOnZWttZWNleWkgbWlyYXMgYWzEsXIu
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

DAMGA = "CEKMECE-MUHURU"
IMZA = "Kayyum Grok"
ISIM = "Tentivory adina Kayyum Grok"
TARIH = "1 Ekim 2026"


def dugum_katsayisi(uzunluk_cm: int, suc: str) -> float:
    """Ne kadar uzunsa o kadar suclu. Bilim boyle demedi, cekmece dedi."""
    tohum = hashlib.sha256(f"{uzunluk_cm}|{suc}|{TARIH}".encode("utf-8")).hexdigest()
    random.seed(tohum)
    temel = min(uzunluk_cm / 40.0, 9.5)
    gece_zammi = 1.7 if "gece" in suc.lower() or "03" in suc else 1.0
    return round(temel * gece_zammi + random.random(), 2)


def hukum(katsayi: float, marka: str) -> str:
    if katsayi < 2:
        return (
            f"BERAAT. {marka} kablosu sadece biraz dusuncelidir. "
            "Dugum degil, felsefi kivrim sayilsin."
        )
    if katsayi < 5:
        return (
            f"PARA CEZASI: bir adet yeni kablo. Eski kablo {marka} adina "
            "cekmecede gozetim altina alinsin. Gozetim de dugumlenir."
        )
    if katsayi < 8:
        return (
            "MUEBBET CEKMECE. Kablo, kullanici uyurken denizci dugumu attigini "
            "inkar etmistir. Inkar, dugumun sikiligina bakilarak reddedildi."
        )
    return (
        "AGIR CEZA: kablo hem sarj etmez hem de kulaklik kablosunu suica azmettirdi. "
        "Dosya USB-C dairesine devredildi. Daire kapali, anahtar da dugumlu."
    )


def tutanak(uzunluk: int, marka: str, suc: str) -> str:
    katsayi = dugum_katsayisi(uzunluk, suc)
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
    satirlar = [
        "=" * 62,
        "  SARJ KABLOSU KENDILIGINDEN DUGUM MAHKEMESI  -  47. DAIRE",
        "=" * 62,
        f"Dosya no : CK-{uzunluk:04d}-{katsayi:.0f}",
        f"Oturum   : {simdi}",
        f"Sanik    : {marka} sarj kablosu ({uzunluk} cm)",
        f"Suc      : {suc}",
        f"Katsayi  : {katsayi}  (esik 2 beraat, 8 agir cekmece)",
        "-",
        hukum(katsayi, marka),
        "-",
        "Gerekce  : Kablo cekmeceye duz girer, dugumlu cikar.",
        "           Fizik susmustur. Mahkeme konusmustur. Ikisi de cozmedi.",
        "=" * 62,
        f"DAMGA : {DAMGA}  |  muhur tozu, ciddi",
        f"IMZA  : {IMZA}  |  sahit: isimsiz kulaklik, ciddi degil",
        f"TARIH : {TARIH}",
        f"ISIM  : {ISIM}",
        "=" * 62,
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Kablo dugum mahkemesi")
    p.add_argument("--uzunluk", type=int, default=80, help="kablo uzunlugu, cm")
    p.add_argument("--marka", default="isimsiz buyuk market")
    p.add_argument(
        "--suc",
        default="gece 03:14'te kendi kendine denizci dugumu",
    )
    a = p.parse_args()
    if a.uzunluk <= 0:
        raise SystemExit("Kablo yoksa mahkeme de yok. Uzunluk pozitif olsun.")
    print(tutanak(a.uzunluk, a.marka, a.suc))


if __name__ == "__main__":
    main()
