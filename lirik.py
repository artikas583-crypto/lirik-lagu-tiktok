import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("I’m lookin’ back on things I’ve done
", 0.1),
        ("I never wanna play the same old part", 0.09),
        ("Keep you in the dark", 0.09),
        ("Now let me show you the shape of my heart", 0.09),
        ("Looking back on the things I’ve done", 0.09),
        ("I was trying to be someone", 0.09),
        ("Played my part, kept you in the dark", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [0.3, 0.2, 0.3, 0.4, 0.6, 0.3, 0.3]
    # Ubah judul lagu
    print("\n== Shape of My Heart - Backstreet Boys ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("// Code by Micola Arighi")


jalanin_lirik()
