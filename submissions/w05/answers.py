"""Jawaban w05 — Variabel Acak & Nilai Harapan

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w05/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
import math


def q01() -> bool:
    """[T/F] Nilai harapan dari sebuah variabel acak harus merupakan salah satu nilai yang
mungkin muncul dari variabel tersebut."""
    # Salah — contoh: dadu adil, E[X] = 3.5 bukan nilai yang mungkin muncul
    return False


def q02() -> bool:
    """[T/F] Variansi dari sebuah variabel acak tidak pernah bernilai negatif."""
    # Benar — Var(X) = E[(X-μ)²] ≥ 0 selalu
    return True


def q03() -> bool:
    """[T/F] Jika X adalah konstanta c, maka E[X] = c dan (X) = 0."""
    # Benar — konstanta tidak memiliki sebaran, σ = 0
    return True


def q04() -> str:
    """[MC] Jika E[X] = 5, maka E[2X+3] adalah:

A) 10
B) 13
C) 8
D) 5"""
    # E[aX+b] = a·E[X] + b = 2×5 + 3 = 13
    return "B"


def q05() -> str:
    """[MC] Variansi dari variabel acak X didefinisikan sebagai:

A) E[X2]−(E[X])2
B) E[X]−E[X2]
C) E[X]
D) E[X]2"""
    # Var(X) = E[X²] − (E[X])²
    return "A"


def q06() -> str:
    """[MC] Fungsi yang memberikan probabilitas P(X ) disebut:

A) PMF.
B) PDF.
C) CDF.
D) MGF."""
    # Variabel acak diskrit → Probability Mass Function (PMF)
    return "A"


def q07() -> str:
    """[MC] Simpangan baku () adalah:

A) Akar kuadrat dari variansi.
B) Kuadrat dari mean.
C) Selisih antara nilai maksimum dan minimum.
D) Nilai harapan dari X."""
    # σ = √Var(X)
    return "A"


def q08() -> float:
    """[Numeric] Jika X memiliki nilai 0,1 dengan probabilitas 0,4,0,6, berapakah E[X]?"""
    # E[X] = 0×0.4 + 1×0.6 = 0.6
    return 0.6


def q09() -> float:
    """[Numeric] Hitung (X) untuk variabel pada soal nomor 8."""
    # E[X]  = 0.6
    # E[X²] = 0²×0.4 + 1²×0.6 = 0.6
    # Var(X) = E[X²] − (E[X])² = 0.6 − 0.36 = 0.24
    # σ(X)   = √0.24 ≈ 0.4899
    return round(math.sqrt(0.24), 4)


def q10() -> float:
    """[Numeric] Jika E[X] = 10 dan E[X2] = 116, berapakah variansinya?"""
    # Var(X) = E[X²] − (E[X])² = 116 − 100 = 16
    return 16.0


def q11() -> float:
    """[Numeric] Sebuah variabel acak memiliki nilai 1,2,3 dengan peluang sama. Berapakah
nilai harapannya?"""
    # P(X=1) = P(X=2) = P(X=3) = 1/3
    # E[X] = 1×(1/3) + 2×(1/3) + 3×(1/3) = 6/3 = 2.0
    return 2.0


def q12() -> float:
    """[Numeric] Jika (X) = 4, berapakah (3X+5)?"""
    # σ(aX+b) = |a|·σ(X)  → konstanta b tidak mempengaruhi sebaran
    # σ(3X+5) = 3 × 4 = 12
    return 12.0