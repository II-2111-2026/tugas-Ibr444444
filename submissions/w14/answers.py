"""Jawaban w14 — Aplikasi Probabilitas & Statistika di Bidang IT

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di weeks/w14/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F    -> bool  (True=Benar, False=Salah)
- MC     -> str   ("A"/"B"/"C"/"D")
- Numeric-> int/float (desimal pakai '.')
"""
from __future__ import annotations


def q01() -> bool:
    """[T/F] Pengujian A/B adalah aplikasi nyata dari uji hipotesis dua sampel."""
    # TRUE — A/B test membandingkan dua versi menggunakan uji hipotesis dua sampel
    return True


def q02() -> bool:
    """[T/F] Metrik "Presisi" mengukur seberapa banyak dari total prediksi positif yang benar-
benar positif."""
    # TRUE — Precision = TP / (TP + FP)
    return True


def q03() -> bool:
    """[T/F] Dalam monitoring sistem, kita biasanya mengabaikan outlier karena itu bukan
bagian dari pola normal."""
    # FALSE — outlier dalam monitoring justru PENTING; bisa menandakan anomali/insiden
    return False


def q04() -> str:
    """[MC] Metrik evaluasi yang tepat untuk dataset dengan kelas yang tidak seimbang
(imbalanced) adalah:

A) Akurasi.
B) F1-Score.
C) Mean.
D) Range."""
    # F1-Score menyeimbangkan Precision dan Recall, cocok untuk kelas tidak seimbang
    return "B"


def q05() -> str:
    """[MC] Dalam deteksi anomali, data yang berada di luar 3 biasanya dianggap:

A) Data normal.
B) Outlier atau anomali.
C) Nilai rata-rata.
D) Sampel ideal."""
    # Aturan 3-sigma: data di luar μ±3σ dianggap anomali
    return "B"


def q06() -> str:
    """[MC] Pengujian A/B dilakukan untuk:

A) Mengurangi biaya server.
B) Menentukan versi produk mana yang memberikan performa/konversi lebih baik.
C) Menghapus bug secara otomatis.
D) Mengganti peran programmer."""
    return "B"


def q07() -> str:
    """[MC] Jika sebuah sistem memiliki presisi 1,0, berarti:

A) Tidak ada false positive.
B) Tidak ada false negative.
C) Akurasi 100%.
D) Sistem sempurna."""
    # Precision = TP/(TP+FP) = 1.0 → FP = 0 → tidak ada false positive
    return "A"


def q08() -> float:
    """[Numeric] Jika TP = 80 dan FP = 20, berapakah nilai presisinya?"""
    # Precision = TP / (TP + FP) = 80 / (80 + 20) = 80/100 = 0.8
    return 0.8


def q09() -> float:
    """[Numeric] Jika akurasi model adalah 0,95 dan ada 1.000 data, berapa banyak prediksi
yang benar?"""
    # Jumlah benar = 0.95 × 1000 = 950
    return 950.0


def q10() -> float:
    """[Numeric] Hitung F1-score jika Presisi = 0,8 dan Recall = 0,8."""
    # F1 = 2 × P × R / (P + R) = 2×0.8×0.8 / (0.8+0.8) = 1.28/1.6 = 0.8
    return 0.8


def q11() -> float:
    """[Numeric] Berapakah nilai skor-Z untuk data point 110 jika rata-rata 100 dan simpangan
baku 5?"""
    # Z = (110 - 100) / 5 = 10/5 = 2.0
    return 2.0


def q12() -> float:
    """[Numeric] Jika dalam pengujian A/B, p-value yang didapat adalah 0,001, apakah ada
perbedaan signifikan pada = 0,05? (Tulis 1 untuk Ya, 0 untuk Tidak)"""
    # p-value (0.001) < α (0.05) → ada perbedaan signifikan → Ya = 1
    return 1.0
