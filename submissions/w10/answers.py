"""Jawaban w10 — Distribusi Sampling & Teorema Limit Pusat

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w10/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Teorema Limit Pusat menyatakan bahwa rata-rata sampel akan mendekati
distribusi Normal jika ukuran sampel cukup besar (n 30)."""
    # TRUE — CLT: X̄ → N(μ, σ²/n) jika n besar
    return True


def q02() -> bool:
    """[T/F] Rata-rata dari distribusi sampling rata-rata ( ) selalu sama dengan rata-rata
X populasi ()."""
    # TRUE — E[X̄] = μ (tidak bias)
    return True


def q03() -> bool:
    """[T/F] Semakin besar ukuran sampel, semakin besar pula Standard Error-nya."""
    # FALSE — SE = σ/√n → SE MENGECIL saat n membesar
    return False


def q04() -> str:
    """[MC] Jika populasi memiliki = 10 dan ukuran sampel n = 100, maka Standard Error ( )
X adalah:

A) 10
B) 1
C) 0,1
D) 100"""
    # SE = σ/√n = 10/√100 = 10/10 = 1
    return "B"


def q05() -> str:
    """[MC] Distribusi sampling dari proporsi sampel p akan mendekati Normal jika:

A) n sangat kecil.
B) np 5 dan n(1−p) 5.
C) Populasi sangat heterogen.
D) p = 0,5."""
    # Syarat aproksimasi Normal: np ≥ 5 dan n(1-p) ≥ 5
    return "B"


def q06() -> str:
    """[MC] Faktor n dalam rumus Standard Error menunjukkan bahwa:

A) Error berkurang secara linear dengan n.
B) Untuk mengurangi error menjadi setengahnya, kita butuh sampel 4 kali lebih banyak.
C) Error tidak dipengaruhi oleh n.
D) Sampel besar selalu buruk."""
    # SE = σ/√n → untuk SE/2 butuh n×4 (karena √(4n) = 2√n)
    return "B"


def q07() -> str:
    """[MC] Statistik sampel yang digunakan untuk menduga parameter populasi disebut:

A) Estimator.
B) Variabel.
C) Konstanta.
D) Bias."""
    return "A"


def q08() -> float:
    """[Numeric] Jika = 50 dan = 10, berapakah nilai rata-rata dari distribusi sampling rata-
rata untuk n = 25?"""
    # E[X̄] = μ = 50
    return 50.0


def q09() -> float:
    """[Numeric] Hitung Standard Error jika = 12 dan n = 36."""
    # SE = σ/√n = 12/√36 = 12/6 = 2
    return 2.0


def q10() -> float:
    """[Numeric] Jika rata-rata populasi 100 dan Standard Error 2, berapakah skor-Z untuk
rata-rata sampel X = 104?"""
    # Z = (X̄ - μ) / SE = (104 - 100) / 2 = 2.0
    return 2.0


def q11() -> float:
    """[Numeric] Jika ukuran sampel adalah 64 dan simpangan baku populasi 8, berapakah
simpangan baku distribusi rata-rata sampel?"""
    # SE = σ/√n = 8/√64 = 8/8 = 1
    return 1.0


def q12() -> float:
    """[Numeric] Berapakah nilai rata-rata sampel X jika skor-Z nya adalah 1,5, = 80, dan
Standard Error = 4?"""
    # X̄ = μ + Z×SE = 80 + 1.5×4 = 80 + 6 = 86
    return 86.0
