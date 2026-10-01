"""Modul sederhana untuk menghitung penjumlahan dua angka."""


def hitung_jumlah(angka_a, angka_b):
    """Menghitung dan mencetak hasil penjumlahan dua angka.

    Args:
        angka_a (int | float): Angka pertama.
        angka_b (int | float): Angka kedua.

    Returns:
        int | float: Hasil penjumlahan.
    """
    hasil = angka_a + angka_b
    print(hasil)
    return hasil


if __name__ == "__main__":
    hitung_jumlah(1, 2)
