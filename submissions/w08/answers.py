"""Jawaban w08 — Review Campuran

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w08/quiz.qmd
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
    # FALSE — model probabilistik menghasilkan output yang bisa berbeda meski input sama
    return False


def q02() -> bool:
    """[T/F] Probabilitas dari gabungan dua kejadian selalu lebih besar daripada probabilitas
masing-masing kejadian."""
    # FALSE — jika A ⊂ B maka P(A∪B) = P(B), tidak selalu lebih besar
    return False


def q03() -> bool:
    """[T/F] Pada distribusi kontinu,  selalu sama dengan ."""
    # TRUE — P(X ≤ x) = P(X < x) karena P(X = x) = 0 untuk distribusi kontinu
    return True


def q04() -> str:
    """[MC] Jika = 0, 5, = 0,  dan ,  independen, maka  adalah:
a) 0,9
b) 0,1
c) 0,2
d) 0,5"""
    # P(A∩B) = P(A)×P(B) = 0.5 × 0.4 = 0.2
    return "C"


def q05() -> str:
    """[MC] Variansi dari variabel acak  didefinisikan sebagai:
a) −
b) −
c)
d)"""
    # Var(X) = E[X²] − (E[X])²
    return "A"


def q06() -> str:
    """[MC] Pada distribusi Binomial, probabilitas sukses p harus:
a) Berubah tiap percobaan.
b) Tetap konstan tiap percobaan.
c) Selalu 0,5.
d) Berkurang seiring waktu."""
    # Syarat Binomial: p konstan di setiap percobaan
    return "B"


def q07() -> str:
    """[MC] Jika = 0, 5 pada distribusi Eksponensial, maka nilai harapannya adalah:
a) 0,5
b) 2,0
c) 1,0
d) 0,25"""
    # E[X] = 1/λ = 1/0.5 = 2.0
    return "B"


def q08() -> float:
    """[Numeric] Berapa jumlah elemen dalam ruang sampel jika kita melempar dua buah
dadu bersisi enam?"""
    # |S| = 6 × 6 = 36
    return 36.0


def q09() -> float:
    """[Numeric] Sebuah sistem memiliki probabilitas gagal 0,05. Berapakah probabilitas
sistem tersebut berhasil?"""
    # P(berhasil) = 1 - 0.05 = 0.95
    return 0.95


def q10() -> float:
    """[Numeric] Sebuah sistem memiliki reliabilitas 0,99. Berapa probabilitas kegagalannya?"""
    # P(gagal) = 1 - 0.99 = 0.01
    return 0.01


def q11() -> float:
    """[Numeric] Jika = 0, , = 0,  dan = 0, , hitung  menggunakan Hukum Probabilitas Total."""
    # P(B) = P(B|A)·P(A) + P(B|Ac)·P(Ac)
    #       = 0.7×0.3 + 0.4×0.7 = 0.21 + 0.28 = 0.49
    return 0.49


def q12() -> float:
    """[Numeric] Jika rata-rata kedatangan paket adalah 5 per ms, berapakah variansi jumlah
paket per ms?"""
    # Poisson: Var(X) = λ = 5
    return 5.0
