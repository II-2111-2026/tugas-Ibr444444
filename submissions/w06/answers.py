"""Jawaban w06 — Distribusi Diskrit (Binomial & Poisson)

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w06/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations
import math


def q01() -> bool:
    """[T/F] Distribusi Binomial digunakan untuk eksperimen dengan jumlah percobaan yang
tidak terbatas."""
    # Salah — Binomial mensyaratkan n percobaan yang TERBATAS dan tetap
    return False


def q02() -> bool:
    """[T/F] Parameter mean dan variansi pada distribusi Poisson memiliki nilai yang sama."""
    # Benar — Poisson: E[X] = λ dan Var(X) = λ
    return True


def q03() -> bool:
    """[T/F] Distribusi Bernoulli adalah kasus khusus dari distribusi Binomial dengan n = 1."""
    # Benar — Bn(1, p) = Bernoulli(p)
    return True


def q04() -> str:
    """[MC] Jika X Bn(10,0,2), maka nilai harapannya adalah:

A) 2
B) 0,2
C) 8
D) 1,6"""
    # E[X] = n·p = 10 × 0.2 = 2
    return "A"


def q05() -> str:
    """[MC] Distribusi yang paling tepat untuk memodelkan jumlah telepon yang masuk ke call
center dalam satu menit adalah:

A) Binomial.
B) Poisson.
C) Uniform.
D) Normal."""
    # Jumlah kejadian per satuan waktu → Poisson
    return "B"


def q06() -> str:
    """[MC] Pada distribusi Binomial, probabilitas sukses p harus:

A) Berubah tiap percobaan.
B) Tetap konstan tiap percobaan.
C) Selalu 0,5.
D) Berkurang seiring waktu."""
    # Syarat Binomial: p konstan di setiap percobaan
    return "B"


def q07() -> str:
    """[MC] Rumus P(X = ) = − adalah untuk distribusi:

A) Binomial.
B) Poisson.
C) Geometrik.
D) Eksponensial."""
    # P(X=k) = e^(-λ) · λ^k / k!  → Poisson
    return "B"


def q08() -> float:
    """[Numeric] Jika X Bn(4,0,5), hitung P(X = 2)."""
    # P(X=2) = C(4,2) · 0.5² · 0.5²
    #         = 6 · 0.25 · 0.25
    #         = 6 × 0.0625
    #         = 0.375
    n, k, p = 4, 2, 0.5
    return math.comb(n, k) * (p**k) * ((1 - p)**(n - k))


def q09() -> float:
    """[Numeric] Untuk distribusi Poisson dengan = 2, berapakah probabilitas P(X = 0)?
(Gunakan 3 desimal)"""
    # P(X=0) = e^(-2) · 2^0 / 0! = e^(-2) ≈ 0.135
    lam = 2
    return round(math.exp(-lam), 3)


def q10() -> float:
    """[Numeric] Hitung variansi dari variabel acak X Bn(100,0,1)."""
    # Var(X) = n·p·(1-p) = 100 × 0.1 × 0.9 = 9.0
    return 100 * 0.1 * 0.9


def q11() -> float:
    """[Numeric] Berapakah nilai maksimum yang mungkin dari variabel acak X Bn(10,0,5)?"""
    # Nilai maks Binomial Bn(n,p) = n = 10 (semua percobaan sukses)
    return 10.0


def q12() -> float:
    """[Numeric] Jika rata-rata kedatangan paket adalah 5 per ms, berapakah variansi jumlah
paket per ms?"""
    # Poisson: Var(X) = λ = 5
    return 5.0