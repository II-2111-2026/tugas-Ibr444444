"""Jawaban w04 — Probabilitas Kondisional & Teorema Bayes

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w04/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Jika kejadian A dan B independen, maka P(A|B) = P(A)."""
    return True


def q02() -> bool:
    """[T/F] Probabilitas kondisional P(A|B) selalu sama dengan P(B|A)."""
    return False


def q03() -> bool:
    """[T/F] Teorema Bayes memungkinkan kita untuk membalik kondisi probabilitas dari
P(B|A) menjadi P(A|B)."""
    return True


def q04() -> str:
    """[MC] Jika P(A) = 0,5,P(B) = 0,4 dan A,B independen, maka P(A∩B) adalah:

A) 0,9
B) 0,1
C) 0,2
D) 0,5"""
    # P(A∩B) = P(A) × P(B) = 0.5 × 0.4 = 0.2
    return "C"


def q05() -> str:
    """[MC] Rumus Bayes menyatakan bahwa P(A|B) sama dengan:

A) P(B|A)P(A)/P(B)
B) P(A|B)P(B)/P(A)
C) P(A)+P(B)
D) P(A∩B)"""
    # Teorema Bayes: P(A|B) = P(B|A)·P(A) / P(B)
    return "A"


def q06() -> str:
    """[MC] Kejadian di mana hasil satu eksperimen tidak mempengaruhi hasil eksperimen
lainnya disebut:

A) Saling lepas.
B) Independen.
C) Kondisional.
D) Komplementer."""
    return "B"


def q07() -> str:
    """[MC] Jika sebuah tes medis memiliki sensitivitas tinggi, maka:

A) Banyak hasil false positive.
B) Probabilitas mendeteksi orang sakit sangat tinggi.
C) Probabilitas mendeteksi orang sehat sangat tinggi.
D) Tes tersebut tidak berguna."""
    # Sensitivitas = True Positive Rate = P(+|Sakit)
    return "B"


def q08() -> float:
    """[Numeric] Jika P(A∩B) = 0,2 dan P(B) = 0,5, berapakah P(A|B)?"""
    # P(A|B) = P(A∩B) / P(B) = 0.2 / 0.5
    return 0.4


def q09() -> float:
    """[Numeric] Probabilitas hujan adalah 0,1. Jika hujan, probabilitas jalan macet adalah 0,8.
Berapa probabilitas (Hujan DAN Macet)?"""
    # P(H∩M) = P(H) × P(M|H) = 0.1 × 0.8
    return 0.08


def q10() -> float:
    """[Numeric] Dalam sebuah populasi, 1% menderita penyakit. Sebuah tes memiliki akurasi
99% (baik untuk yang sakit maupun sehat). Jika seseorang dites positif, berapa
probabilitas dia benar-benar sakit?"""
    # P(D)  = 0.01,  P(Dc) = 0.99
    # P(+|D)  = 0.99 (sensitivitas)
    # P(+|Dc) = 0.01 (false positive rate = 1 - spesifisitas)
    # P(+) = P(+|D)·P(D) + P(+|Dc)·P(Dc)
    #       = 0.99×0.01 + 0.01×0.99 = 0.0099 + 0.0099 = 0.0198
    # P(D|+) = P(+|D)·P(D) / P(+) = 0.0099 / 0.0198
    return 0.5


def q11() -> float:
    """[Numeric] Jika P(A) = 0,3,P(B|A) = 0,7 dan P(B|Ac) = 0,4, hitung P(B)
menggunakan Hukum Probabilitas Total."""
    # P(B) = P(B|A)·P(A) + P(B|Ac)·P(Ac)
    #       = 0.7×0.3 + 0.4×0.7
    #       = 0.21 + 0.28
    return 0.49


def q12() -> float:
    """[Numeric] Dari soal nomor 11, hitung P(A|B) menggunakan Teorema Bayes (Gunakan
3 desimal)."""
    # P(A|B) = P(B|A)·P(A) / P(B) = 0.21 / 0.49 ≈ 0.42857...
    return round(0.21 / 0.49, 3)