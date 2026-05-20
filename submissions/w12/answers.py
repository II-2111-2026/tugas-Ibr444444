"""Jawaban w12 — Uji Hipotesis

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w12/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Jika p-value lebih kecil dari tingkat signifikansi , maka kita gagal menolak hipotesis
nol."""
    # FALSE — jika p-value < α, kita MENOLAK H0 (bukan gagal menolak)
    return False


def q02() -> bool:
    """[T/F] Galat Tipe I adalah kesalahan menolak padahal benar."""
    # TRUE — Type I error: menolak H0 yang sebenarnya benar (false positive)
    return True


def q03() -> bool:
    """[T/F] Meningkatkan ukuran sampel biasanya akan meningkatkan kekuatan uji (power)."""
    # TRUE — sampel lebih besar → SE lebih kecil → lebih mudah mendeteksi perbedaan nyata
    return True


def q04() -> str:
    """[MC] Nilai probabilitas yang menunjukkan kekuatan bukti melawan hipotesis nol disebut:

A) Tingkat kepercayaan.
B) p-value.
C) Statistik uji.
D) Parameter."""
    return "B"


def q05() -> str:
    """[MC] Jika kita menguji = 50 vs 50, maka kita melakukan uji:
0 1

A) Satu arah (kanan).
B) Satu arah (kiri).
C) Dua arah.
D) Tanpa arah."""
    # H0: μ=50 vs H1: μ≠50 → uji dua arah (two-tailed)
    return "C"


def q06() -> str:
    """[MC] Kondisi di mana kita menolak hipotesis nol padahal sebenarnya salah disebut:

A) Keputusan yang benar (Power).
B) Galat Tipe I.
C) Galat Tipe II.
D) Signifikansi."""
    # Menolak H0 yang FALSE = keputusan benar = Power
    return "A"


def q07() -> str:
    """[MC] Tingkat signifikansi yang umum digunakan dalam penelitian adalah:

A) 0,5
B) 0,05
C) 0,95
D) 1,0"""
    # α = 0.05 paling umum digunakan
    return "B"


def q08() -> float:
    """[Numeric] Jika statistik uji = 2,58 dan nilai kritis c = 1,96 untuk uji dua arah, apakah 0
ditolak? (Tulis 1 untuk Ya, 0 untuk Tidak)"""
    # |2.58| > 1.96 → tolak H0 → Ya = 1
    return 1.0


def q09() -> float:
    """[Numeric] Berapakah nilai jika tingkat kepercayaan adalah 99%?"""
    # Confidence level 99% → α = 1 - 0.99 = 0.01
    return 0.01


def q10() -> float:
    """[Numeric] Dalam uji t dengan sampel n = 10, berapakah derajat kebebasannya?"""
    # df = n - 1 = 10 - 1 = 9
    return 9.0


def q11() -> float:
    """[Numeric] Jika p-value = 0,02 dan = 0,05, apakah kita menolak 0? (Tulis 1 untuk Ya, 0
untuk Tidak)"""
    # p-value (0.02) < α (0.05) → tolak H0 → Ya = 1
    return 1.0


def q12() -> float:
    """[Numeric] Jika statistik = 0, berapakah p-value untuk uji dua arah?"""
    # Z=0 → P(|Z|≥0) = 2×P(Z≥0) = 2×0.5 = 1.0
    return 1.0
