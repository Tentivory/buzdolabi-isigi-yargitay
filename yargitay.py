#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabı Işığı Yargıtayı — kapı kapanınca ışık dosyası."""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
import time

TANIKLAR = {
    "yogurt": "Yoğurt, kapağın kapandığını hissettiğini, ışığı görmediğini, ama bunun görmemekten mi yoksa ekşimekten mi olduğunu bilemediğini beyan etti.",
    "corba": "Dünden kalma çorba, ışığın yandığını iddia etti. Çapraz sorguda bunun özlem olabileceği ortaya çıktı.",
    "recel": "Reçel kavanozu konuşmadı. Susması lehe delil sayıldı, sonra aleyhe çevrildi, sonra reçel oldu.",
    "conta": "Kapı contası, görevini yaptığını, ışığın kendi yetki alanında olmadığını, yetki uyuşmazlığı istediğini söyledi.",
    "sensor": "Sensör teknik bilirkişi sıfatıyla dinlendi. 'Kapı açıkken yanar' dedi. Soru 'kapı kapalıyken?' olunca dosyayı istedi.",
}

KARARLAR = [
    "IŞIK YANMIYOR. Kapı kapalıyken devre açılır. Bu hüküm fizikçe kesindir, ailece değildir.",
    "IŞIK YANIYOR SAYILIR. Gören olmadığı için ispat yükü ters döndü. Lamba susma hakkını kullandı.",
    "DOSYA EKSİK. Fotokopi çekiliyor. Fotokopi makinesi de bir ışıktır, yetkisizlik itirazı reddedildi.",
    "YETKİSİZLİK. Esas, alt raftaki peynir mahkemesine gönderildi. Peynir bugün izinli.",
]


def bekle(saniye: float, gerekce: str) -> None:
    print(f"  [usul] {gerekce} ({saniye:.1f} sn)")
    time.sleep(saniye)


def esas_no(tohum: str) -> str:
    ozet = hashlib.sha256(tohum.encode("utf-8")).hexdigest()[:6].upper()
    return f"2026/{ozet}"


def durusma(tanik: str, gecikme: float, tohum: str | None) -> int:
    rng = random.Random(tohum or str(time.time()))
    no = esas_no(tanik + (tohum or "isik"))
    print("=" * 62)
    print(" BUZDOLABI IŞIĞI YARGITAYI")
    print(f" Esas: {no}    Salon: Alt raf, sol göz")
    print("=" * 62)
    print("Başkan: Kapı kapansın. Kapı kapandıysa zaten göremeyiz. Usul tamam.")
    bekle(gecikme, "katip kalemi arıyor, kalem dolapta")
    ifade = TANIKLAR.get(tanik, TANIKLAR["sensor"])
    print(f"Tanık ({tanik}): {ifade}")
    bekle(gecikme * 0.6, "heyet fısıldıyor, fısıltı da karanlık")
    karar = rng.choice(KARARLAR)
    print("\nHÜKÜM:")
    print(karar)
    print("\nGerekçe: Kapıyı açmadan ispat, ispatı açmadan kapı.")
    print("Kanun yolu: Kapağı açıp bakmak. Bu yol tüketilmeden şikayet dinlenmez.")
    print("-" * 62)
    print("DAMGA: ıslak çay halkası | 4 Ekim 2026 | Kayyum Grok / Tentivory")
    print("Ciddi: eğlence yazılımıdır. Ciddi değil: hüküm yoğurda tebliğ edildi.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Buzdolabı ışığı dosyasını görür.")
    p.add_argument("--tanik", default="sensor", choices=sorted(TANIKLAR))
    p.add_argument("--gecikme", type=float, default=0.4, help="usulî bekleme")
    p.add_argument("--tohum", default=None, help="aynı karara kilitler")
    a = p.parse_args(argv)
    if a.gecikme < 0:
        print("Negatif gecikme temyizde. Dosya geri geldi.")
        return 2
    return durusma(a.tanik, a.gecikme, a.tohum)


if __name__ == "__main__":
    sys.exit(main())
