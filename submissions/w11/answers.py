"""Jawaban w11 — Interval Kepercayaan

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w11/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Semakin tinggi tingkat kepercayaan yang diinginkan, semakin lebar interval
kepercayaan yang dihasilkan."""
    # TRUE — confidence level lebih tinggi → z* lebih besar → interval lebih lebar
    return True


def q02() -> bool:
    """[T/F] Interval kepercayaan 95% berarti ada peluang 95% bahwa parameter populasi
berada dalam rentang tersebut untuk satu interval yang sudah dihitung."""
    # FALSE — untuk CI yang sudah terhitung, parameter ada atau tidak di dalamnya (tidak ada probabilitas);
    # interpretasi yang benar: 95% dari interval yang dibuat dengan prosedur ini akan memuat parameter.
    return False


def q03() -> bool:
    """[T/F] Distribusi t-Student mendekati distribusi Normal saat derajat kebebasan () menjadi
sangat besar."""
    # TRUE — t(df) → N(0,1) saat df → ∞
    return True


def q04() -> str:
    """[MC] Jika kita ingin mempersempit interval kepercayaan tanpa mengubah tingkat
kepercayaan, kita harus:

A) Mengurangi ukuran sampel.
B) Meningkatkan ukuran sampel.
C) Meningkatkan simpangan baku.
D) Tidak melakukan apa-apa."""
    # ME = z* × σ/√n → untuk memperkecil ME, perbesar n
    return "B"


def q05() -> str:
    """[MC] Nilai kritis untuk tingkat kepercayaan 95% adalah:

A) 1,645
B) 1,96
C) 2,58
D) 1,00"""
    # z* = 1.96 untuk CI 95% (dua arah, α/2 = 0.025)
    return "B"


def q06() -> str:
    """[MC] Derajat kebebasan () untuk interval kepercayaan rata-rata satu sampel berukuran
n adalah:

A) n
B) n+1
C) n−1
D) n/2"""
    # df = n - 1
    return "C"


def q07() -> str:
    """[MC] Estimasi titik terbaik untuk rata-rata populasi adalah:

A) Median sampel.
B) Modus sampel.
C) Rata-rata sampel ( X).
D) Standar deviasi sampel."""
    # X̄ adalah estimator tak bias terbaik (BLUE) untuk μ
    return "C"


def q08() -> float:
    """[Numeric] Jika X = 100, Margin Error = 5, berapakah batas bawah interval
kepercayaan?"""
    # Batas bawah = X̄ - ME = 100 - 5 = 95
    return 95.0


def q09() -> float:
    """[Numeric] Untuk sampel n = 16 dan simpangan baku sampel = 4, berapakah nilai
estimasi Standard Error-nya?"""
    # SE = s/√n = 4/√16 = 4/4 = 1
    return 1.0


def q10() -> float:
    """[Numeric] Berapakah derajat kebebasan jika ukuran sampel adalah 25?"""
    # df = n - 1 = 25 - 1 = 24
    return 24.0


def q11() -> float:
    """[Numeric] Jika interval kepercayaan adalah , berapakah nilai estimasi titik rata-ratanya?"""
    # Titik tengah CI (40, 60) = (40 + 60) / 2 = 50
    return 50.0


def q12() -> float:
    """[Numeric] Jika margin error adalah 2 dan nilai kritis = 2, berapakah Standard Error-
nya?"""
    # ME = z* × SE  →  2 = 2 × SE  →  SE = 1
    return 1.0
