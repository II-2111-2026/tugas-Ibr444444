"""Jawaban w02 — MAHASISWA

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w02/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Jika dua kejadian A dan B saling lepas, maka P(A∩B) = 0."""
    # TRUE — "saling lepas" (mutually exclusive) berarti A dan B tidak bisa
    # terjadi bersamaan, sehingga irisan A∩B = ∅ dan P(A∩B) = 0.
    return True


def q02() -> bool:
    """[T/F] Probabilitas dari gabungan dua kejadian selalu lebih besar daripada
    probabilitas masing-masing kejadian."""
    # FALSE — jika A ⊂ B maka P(A∪B) = P(B), bukan lebih besar dari P(B).
    # Secara umum P(A∪B) = P(A)+P(B)-P(A∩B), jadi bisa sama dengan salah satu
    # jika kejadian itu sudah mencakup yang lain.
    return False


def q03() -> bool:
    """[T/F] Hukum komplemen menyatakan bahwa P(A)+P(Ac) = 1."""
    # TRUE — aksioma probabilitas: P(S) = 1 dan A ∪ Ac = S serta A ∩ Ac = ∅,
    # sehingga P(A) + P(Ac) = 1.
    return True


def q04() -> str:
    """[MC] Jika P(A) = 0,4 dan P(B) = 0,3 serta keduanya saling lepas, maka
    P(A∪B) adalah:
    A) 0,7
    B) 0,12
    C) 0,1
    D) 0,5"""
    # A — karena saling lepas: P(A∪B) = P(A)+P(B) = 0.4+0.3 = 0.7
    # (tidak ada pengurangan P(A∩B) karena P(A∩B) = 0)
    return "A"


def q05() -> str:
    """[MC] Manakah simbol yang merepresentasikan irisan antara kejadian A dan B?
    A) A∪B
    B) A∩B
    C) A∖B
    D) Ac"""
    # B — A∩B adalah irisan (intersection): himpunan elemen yang ada di A DAN B.
    # A∪B = gabungan, A∖B = selisih, Ac = komplemen.
    return "B"


def q06() -> str:
    """[MC] Jika A ⊂ B, maka manakah pernyataan yang benar?
    A) P(A) > P(B)
    B) P(A∩B) = P(A)
    C) P(A∪B) = P(A)
    D) P(A)+P(B) = 1"""
    # B — jika A ⊂ B maka A∩B = A (semua elemen A juga ada di B),
    # sehingga P(A∩B) = P(A).
    # A salah (P(A) ≤ P(B)), C salah (P(A∪B) = P(B)), D salah (tidak ada relasi itu).
    return "B"


def q07() -> str:
    """[MC] Dalam diagram Venn, area di luar lingkaran A merepresentasikan:
    A) Kejadian A.
    B) Komplemen kejadian A (Ac).
    C) Irisan A dengan B.
    D) Ruang sampel kosong."""
    # B — Ac berisi semua hasil dalam S yang TIDAK termasuk dalam A,
    # yang dalam diagram Venn berada di luar lingkaran A.
    return "B"


def q08() -> float:
    """[Numeric] Jika P(A) = 0,6, P(B) = 0,5, dan P(A∩B) = 0,2, berapakah P(A∪B)?"""
    # Rumus penjumlahan umum (Addition Rule):
    # P(A∪B) = P(A) + P(B) - P(A∩B) = 0.6 + 0.5 - 0.2 = 0.9
    return 0.9


def q09() -> float:
    """[Numeric] Sebuah sistem memiliki probabilitas gagal 0,05. Berapakah probabilitas
    sistem tersebut berhasil?"""
    # P(berhasil) = 1 - P(gagal) = 1 - 0.05 = 0.95  (hukum komplemen)
    return 0.95


def q10() -> float:
    """[Numeric] Jika kejadian A dan B saling lepas dengan P(A) = 0,2 dan P(B) = 0,5,
    berapakah P(A∩B)?"""
    # Saling lepas (mutually exclusive) ⟹ A∩B = ∅ ⟹ P(A∩B) = 0
    return 0.0


def q11() -> float:
    """[Numeric] Berapa probabilitas munculnya angka genap pada pelemparan satu dadu
    adil?"""
    # Angka genap pada dadu: {2, 4, 6} → 3 dari 6 kemungkinan
    # P(genap) = 3/6 = 0.5
    return 0.5


def q12() -> float:
    """[Numeric] Jika P(A∪B) = 0,8, P(A) = 0,5, dan A serta B saling lepas, berapakah
    P(B)?"""
    # Saling lepas ⟹ P(A∪B) = P(A) + P(B)
    # 0.8 = 0.5 + P(B)  ⟹  P(B) = 0.8 - 0.5 = 0.3
    return 0.3