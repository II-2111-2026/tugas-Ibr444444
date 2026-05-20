"""Jawaban w09 — Variabel Acak Bersama & Korelasi

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w09/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Jika korelasi antara dua variabel adalah nol, maka kedua variabel tersebut pasti
independen."""
    # FALSE — korelasi nol hanya berarti tidak ada hubungan LINEAR;
    # hubungan non-linear bisa tetap ada.
    return False


def q02() -> bool:
    """[T/F] PDF marginal () didapatkan dengan mengintegralkan (,) terhadap dari − ke .
X"""
    # TRUE — f_X(x) = ∫f(x,y)dy dari -∞ ke ∞
    return True


def q03() -> bool:
    """[T/F] Nilai koefisien korelasi selalu berada di antara -1 dan 1."""
    # TRUE — -1 ≤ ρ ≤ 1
    return True


def q04() -> str:
    """[MC] Jika X dan independen, maka E sama dengan:

A) E[X]+E
B) E[X]E
C) E[X]/E
D) 0"""
    # Independen → E[XY] = E[X]·E[Y]
    return "B"


def q05() -> str:
    """[MC] Manakah ukuran yang menunjukkan kekuatan hubungan linear antara dua
variabel?

A) Variansi.
B) Mean.
C) Korelasi.
D) CDF."""
    # Korelasi (koefisien korelasi Pearson) mengukur kekuatan hubungan linear
    return "C"


def q06() -> str:
    """[MC] Jika (X) = 4,() = 9, dan X, independen, maka (X+) adalah:

A) 13
B) 5
C) 36
D) 6,5"""
    # Var(X+Y) = Var(X) + Var(Y) = 4 + 9 = 13 (karena independen, Cov=0)
    return "A"


def q07() -> str:
    """[MC] Fungsi probabilitas kondisional (|) didefinisikan sebagai:

A) (,)/ () X
B) (,)/()
C) () () X
D) (,)− () X"""
    # f(y|x) = f(x,y) / f_X(x)
    return "A"


def q08() -> float:
    """[Numeric] Jika (X,) = 2, X = 2, = 2, berapakah koefisien korelasinya?"""
    # ρ = Cov(X,Y) / (σ_X × σ_Y) = 2 / (2 × 2) = 0.5
    return 0.5


def q09() -> float:
    """[Numeric] Berapakah nilai E jika E[X] = 10 dan E = 20?"""
    # E[X + Y] = E[X] + E[Y] = 10 + 20 = 30
    return 30.0


def q10() -> float:
    """[Numeric] Jika (,) = 1/4 untuk 0 2 dan 0 2, berapakah P(X 1, 1)?"""
    # P(X≤1, Y≤1) = ∫₀¹∫₀¹ (1/4) dy dx = (1/4)×1×1 = 0.25
    return 0.25


def q11() -> float:
    """[Numeric] Dalam tabel diskrit, jika P(1,1) = 0,1P(1,2) = 0,2P(2,1) = 0,3P(2,2) = 0,4,
berapakah probabilitas marginal P(X = 1)?"""
    # P(X=1) = P(1,1) + P(1,2) = 0.1 + 0.2 = 0.3
    return 0.3


def q12() -> float:
    """[Numeric] Jika X dan memiliki korelasi 1 dan (X) = 4, berapakah (X+X)?"""
    # X + X = 2X  →  Var(2X) = 4×Var(X) = 4×4 = 16
    return 16.0
