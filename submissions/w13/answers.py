"""Jawaban w13 — Regresi Linear

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w13/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Garis regresi meminimalkan jumlah total selisih absolut antara data dan garis."""
    # FALSE — regresi OLS meminimalkan jumlah kuadrat residual (SSE), bukan nilai absolut
    return False


def q02() -> bool:
    """[T/F] Nilai R2 sebesar 0,85 berarti 85% variasi pada variabel dependen dapat dijelaskan
oleh variabel independen."""
    # TRUE — R² = proporsi variasi Y yang dijelaskan oleh model
    return True


def q03() -> bool:
    """[T/F] Regresi linear berganda menggunakan lebih dari satu variabel independen untuk
memprediksi satu variabel dependen."""
    # TRUE — multiple regression: Y = β0 + β1X1 + β2X2 + ...
    return True


def q04() -> str:
    """[MC] Dalam persamaan = +X, merepresentasikan:

A) Intersep.
B) Kemiringan (slope).
C) Varians.
D) Galat."""
    # ŷ = a + bX → b adalah kemiringan (slope)
    return "B"


def q05() -> str:
    """[MC] Jika korelasi = −0,9, maka hubungan antara kedua variabel adalah:

A) Sangat lemah.
B) Sangat kuat dan negatif.
C) Tidak ada hubungan.
D) Positif."""
    # r = -0.9 → sangat kuat (|r| dekat 1) dan negatif
    return "B"


def q06() -> str:
    """[MC] Manakah nilai R2 yang menunjukkan model paling buruk?

A) 0,99
B) 0,50
C) 0,00
D) -1,00"""
    # R² = 0 → model tidak menjelaskan variasi apapun
    return "C"


def q07() -> str:
    """[MC] Titik di mana garis regresi memotong sumbu disebut:

A) Slope.
B) Intersep.
C) Origin.
D) Outlier."""
    return "B"


def q08() -> float:
    """[Numeric] Jika persamaan regresi adalah = 5+2X, berapakah nilai prediksi untuk
X = 10?"""
    # ŷ = 5 + 2×10 = 5 + 20 = 25
    return 25.0


def q09() -> float:
    """[Numeric] Jika R2 = 0,64, berapakah nilai korelasi (ambil nilai positif)?"""
    # r = √R² = √0.64 = 0.8
    return 0.8


def q10() -> float:
    """[Numeric] Berapakah nilai rata-rata dari residual pada model regresi linear klasik?"""
    # Rata-rata residual OLS selalu = 0 (salah satu syarat OLS)
    return 0.0


def q11() -> float:
    """[Numeric] Jika naik 10 unit ketika X naik 2 unit, berapakah nilai slope ?"""
    # slope = Δy/ΔX = 10/2 = 5
    return 5.0


def q12() -> float:
    """[Numeric] Jika S = 40 dan S = 10, berapakah nilai estimasi slope ?"""
    # b = Sxy / Sxx = 40 / 10 = 4
    return 4.0
