"""Modul untuk memproses sampel data berdasarkan beberapa kondisi."""


def proses_data(flag_a, flag_b, data_c, _param_d, list_e, angka_f):
    """Memproses data jika kondisi kriteria terpenuhi.

    Args:
        flag_a (bool): Parameter kondisi pertama.
        flag_b (bool): Parameter kondisi kedua.
        data_c (object): Parameter kondisi ketiga.
        _param_d (object): Parameter tidak terpakai.
        list_e (list): List berisi angka.
        angka_f (int): Angka penambah.

    Returns:
        int | None: Hasil penjumlahan jika valid, atau None.
    """
    var_l = 1
    var_o = 0

    if flag_a and not flag_b and data_c is None:
        try:
            print(flag_a + flag_b)
            return list_e[0] + angka_f + var_l + var_o
        except (IndexError, TypeError) as err:
            print(f"Terjadi kesalahan: {err}")

    return None


if __name__ == "__main__":
    proses_data(True, False, None, 1, [2], 3)
