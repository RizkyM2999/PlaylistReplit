# Meminta input dari pengguna untuk data sebelum dan setelah di-replace
data_sebelum = input("Masukkan data sebelum replace: ")
data_setelah = input("Masukkan data yang ingin digunakan setelah replace: ")

# Baca isi file .m3u
with open('playlist.m3u', 'r') as file:
    data = file.read()

# Ganti teks yang diinginkan
data = data.replace(data_sebelum, data_setelah)

# Tulis perubahan ke file yang sama
with open('playlist.m3u', 'w') as file:
    file.write(data)