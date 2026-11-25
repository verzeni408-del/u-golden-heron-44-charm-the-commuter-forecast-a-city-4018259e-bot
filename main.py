"""Prakiraan cuaca komuter untuk kota fiktif Quizzle.

Kalimat dirakit dari fragmen-fragmen pendek; tiap fragmen membawa
satu suasana: kabut pagi, siang cerah, lalu kereta yang minta maaf.
"""

import os


def susun_kalimat():
    potongan = (
        "In Quizzle, fog until noon, ",
        "then 22\u00b0 and clear. ",
        "The train you missed is the one that was early ",
        "\u2014 today, the timetable apologised.",
    )
    return "".join(potongan)


def simpan(teks, tujuan="/output/entry.txt"):
    os.makedirs(os.path.dirname(tujuan), exist_ok=True)
    with open(tujuan, "w", encoding="utf-8", newline="") as berkas:
        berkas.write(teks)


def main():
    kalimat = susun_kalimat()
    simpan(kalimat)
    print(kalimat)


if __name__ == "__main__":
    main()
