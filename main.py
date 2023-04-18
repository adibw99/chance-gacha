import random

# Daftar reward dengan presentase masing-masing
rewards = {
    "Reward Back Item": 0.6,
    "Reward Weapon": 0.3,
    "Reward Emblem": 0.1
}

# Loop utama program
while True:
    # Menampilkan menu gacha dan meminta pemain memilih
    print("Selamat datang di Gacha!")
    print("1. Tarik Gacha")
    print("2. Keluar")
    choice = input("Pilih menu (1/2): ")

    if choice == "1":
        # Memilih reward acak
        reward = random.choices(list(rewards.keys()), weights=list(rewards.values()))[0]

        # Menampilkan reward yang didapat
        print(f"Selamat! Kamu mendapatkan {reward}!")

    elif choice == "2":
        # Keluar dari loop jika pemain memilih keluar
        break

    else:
        # Menampilkan pesan jika pemain memilih pilihan yang tidak valid
        print("Pilihan tidak valid, silakan coba lagi.")
