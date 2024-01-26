# Meminta input dari pengguna untuk data sebelum dan setelah di-replace
data_sebelum = input("Masukkan data sebelum replace: ")
data_setelah = input("Masukkan data yang ingin digunakan setelah replace: ")

# Baca isi file .m3u
with open('cubmu.txt', 'r') as file:
    data = file.read()

# Ganti teks yang diinginkan
data = data.replace(data_sebelum, data_setelah)

# Tulis perubahan ke file yang sama
with open('cubmu.txt', 'w') as file:
    file.write(data)