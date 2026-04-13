"""Jawaban w01 — MAHASISWA
Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w01/quiz.qmd
- Jangan ubah nama fungsi.
Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Dalam model probabilistik, output yang sama akan selalu dihasilkan dari input yang
    sama terlepas dari variasi acak."""
    # FALSE — justru ciri khas probabilistik adalah output BISA berbeda
    # meski input sama, karena ada elemen acak (stokastik).
    return False


def q02() -> bool:
    """[T/F] Ruang sampel dari sebuah eksperimen acak harus mencakup semua hasil yang
    mungkin terjadi tanpa tumpang tindih."""
    # TRUE — definisi ruang sampel: himpunan SEMUA hasil yang mungkin,
    # bersifat mutually exclusive (tak tumpang tindih) dan collectively exhaustive.
    return True


def q03() -> bool:
    """[T/F] Probabilitas empiris mendekati probabilitas teoretis ketika jumlah percobaan
    mendekati tak hingga."""
    # TRUE — inilah isi Hukum Bilangan Besar (Law of Large Numbers):
    # lim_{n→∞} (frekuensi relatif) = probabilitas teoretis.
    return True


def q04() -> str:
    """[MC] Manakah yang merupakan contoh variabel acak dalam sistem STI?
    A) Kapasitas total hard disk 1TB.
    B) Jumlah core pada prosesor Intel i7.
    C) Waktu yang dibutuhkan untuk merespons query database.
    D) Jumlah bit dalam satu byte."""
    # C — response time query berfluktuasi tergantung beban, ukuran data,
    # dsb.; nilainya tidak bisa dipastikan sebelum diukur → variabel acak.
    # A, B, D adalah konstanta deterministik (nilai tetap/hardware spec).
    return "C"


def q05() -> str:
    """[MC] Jika sebuah ruang sampel S terdiri dari 4 kejadian yang memiliki peluang sama,
    maka probabilitas satu kejadian adalah:
    A) 0,5
    B) 0,25
    C) 0,75
    D) 1,0"""
    # B — P(satu kejadian) = 1 / |S| = 1/4 = 0.25
    return "B"


def q06() -> str:
    """[MC] Kejadian yang mustahil terjadi memiliki nilai probabilitas sebesar:
    A) 0
    B) 1
    C) -1
    D) 0,5"""
    # A — P(∅) = 0 (kejadian kosong / impossible event).
    # Sebaliknya P(S) = 1 (pasti terjadi).
    return "A"


def q07() -> str:
    """[MC] Sekumpulan hasil eksperimen yang merupakan subset dari ruang sampel disebut:
    A) Populasi.
    B) Parameter.
    C) Kejadian (Event).
    D) Konstanta."""
    # C — Event/Kejadian adalah subset E ⊆ S dari ruang sampel S.
    return "C"


def q08() -> float:
    """[Numeric] Berapa jumlah elemen dalam ruang sampel jika kita melempar dua buah
    dadu bersisi enam?"""
    # |S| = 6 × 6 = 36  (setiap dadu punya 6 kemungkinan, keduanya independen)
    return 36.0


def q09() -> float:
    """[Numeric] Jika probabilitas sebuah link internet mati adalah 0,01, berapa probabilitas
    link tersebut hidup?"""
    # P(hidup) = 1 - P(mati) = 1 - 0.01 = 0.99  (aksioma komplemen)
    return 0.99


def q10() -> float:
    """[Numeric] Berapa banyak susunan berbeda yang bisa dibuat dari kata "DATA"?"""
    # "DATA" → 4 huruf dengan huruf 'A' muncul 2 kali
    # Permutasi dengan pengulangan: 4! / 2! = 24 / 2 = 12
    return 12.0


def q11() -> float:
    """[Numeric] Jika sebuah server memiliki probabilitas uptime 0,95, berapa probabilitas
    server tersebut downtime dalam satu periode?"""
    # P(downtime) = 1 - P(uptime) = 1 - 0.95 = 0.05
    return 0.05


def q12() -> float:
    """[Numeric] Dalam simulasi 1000 kali login, jika 20 kali gagal, berapa frekuensi relatif
    kegagalan tersebut?"""
    # Frekuensi relatif = frekuensi kejadian / total percobaan = 20 / 1000 = 0.02
    return 0.02