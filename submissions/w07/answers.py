"""Jawaban w07 — Distribusi Kontinu (Normal & Eksponensial)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w07/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Total luas di bawah kurva fungsi padat probabilitas (PDF) selalu sama dengan 1."""
    # TRUE — aksioma: ∫f(x)dx dari -∞ ke ∞ = 1
    return True


def q02() -> bool:
    """[T/F] Distribusi Normal Standar memiliki mean 0 dan variansi 1."""
    # TRUE — Z ~ N(0, 1): μ=0, σ²=1
    return True


def q03() -> bool:
    """[T/F] Pada distribusi kontinu, P(X ) selalu sama dengan P(X )."""
    # TRUE — untuk distribusi kontinu, P(X=x)=0, sehingga P(X≤x) = P(X<x)
    return True


def q04() -> str:
    """[MC] Nilai yang bersesuaian dengan nilai pada distribusi
(,2) adalah:

A) (−)/
B) (+)/
C) /(−)
D) −"""
    # Z = (X - μ) / σ  → standardisasi nilai X dari N(μ, σ²)
    return "A"


def q05() -> str:
    """[MC] Distribusi mana yang sering digunakan untuk memodelkan waktu antar kejadian
dalam proses Poisson?

A) Binomial.
B) Normal.
C) Eksponensial.
D) Uniform."""
    # Waktu antar kejadian Poisson ~ Eksponensial
    return "C"


def q06() -> str:
    """[MC] Sekitar 95% data dalam distribusi Normal berada dalam rentang:

A)
B) 2
C) 3
D) 0 1"""
    # Aturan empiris: μ ± 2σ ≈ 95%
    return "B"


def q07() -> str:
    """[MC] Jika = 0,5 pada distribusi Eksponensial, maka nilai harapannya adalah:

A) 0,5
B) 2,0
C) 1,0
D) 0,25"""
    # E[X] = 1/λ = 1/0.5 = 2.0
    return "B"


def q08() -> float:
    """[Numeric] Jika (0,1), berapakah P( 0)?"""
    # Z ~ N(0,1), P(Z ≥ 0) = 0.5 (simetri)
    return 0.5


def q09() -> float:
    """[Numeric] Sebuah komponen memiliki rata-rata waktu hidup 100 jam (Eksponensial).
Berapakah parameter -nya?"""
    # E[X] = 1/λ = 100  →  λ = 1/100 = 0.01
    return 0.01


def q10() -> float:
    """[Numeric] Nilai untuk probabilitas kumulatif 0,975 adalah sekitar... (Gunakan 2 desimal)"""
    # Φ(z) = 0.975  →  z = 1.96
    return 1.96


def q11() -> float:
    """[Numeric] Jika X (10,4), berapakah nilai skor-Z untuk = 12?"""
    # X ~ N(10, 4): μ=10, σ²=4, σ=2
    # Z = (12 - 10) / 2 = 1.0
    return 1.0


def q12() -> float:
    """[Numeric] Pada distribusi Normal Standar, berapakah nilai P( > 3) mendekati?
(Gunakan 4 desimal)"""
    # P(Z > 3) ≈ 0.0013
    return 0.0013
