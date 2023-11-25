import tkinter as tk
import sqlite3


def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_matematika = float(entry_matematika.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_sejarah = float(entry_sejarah.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_ekonomi = float(entry_ekonomi.get())
    nilai_sosiologi = float(entry_sosiologi.get())

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    max_nilai = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_kimia,
                    nilai_sejarah, nilai_geografi, nilai_ekonomi, nilai_sosiologi)
    
    if max_nilai == nilai_biologi:
        hasil_prodi = "Kedokteran"
    elif max_nilai == nilai_fisika:
        hasil_prodi = "Teknik"
    elif max_nilai == nilai_inggris:
        hasil_prodi = "Bahasa"
    elif max_nilai == nilai_matematika:
        hasil_prodi = "Matematika"
    elif max_nilai == nilai_kimia:
        hasil_prodi = "Teknik Kimia"
    elif max_nilai == nilai_sejarah:
        hasil_prodi = "Sejarah"
    elif max_nilai == nilai_geografi:
        hasil_prodi = "Geografi"
    elif max_nilai == nilai_ekonomi:
        hasil_prodi = "Manajemen"
    elif max_nilai == nilai_sosiologi:
        hasil_prodi = "Sosiologi"
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('NilaiSiswa.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS NilaiSiswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        matematika REAL,
                        kimia REAL,
                        sejarah REAL,
                        geografi REAL,
                        ekonomi REAL,
                        sosiologi REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO NilaiSiswa (nama_siswa, biologi, fisika, inggris, matematika, kimia,
                    sejarah, geografi, ekonomi, sosiologi, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika,
                    nilai_kimia, nilai_sejarah, nilai_geografi, nilai_ekonomi, nilai_sosiologi, hasil_prodi))
    conn.commit()
    conn.close()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x600")  # Mengatur ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris: ")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

label_matematika = tk.Label(root, text="Nilai Matematika: ")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

label_kimia = tk.Label(root, text="Nilai Kimia: ")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

label_sejarah = tk.Label(root, text="Nilai Sejarah: ")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

label_geografi = tk.Label(root, text="Nilai Geografi: ")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

label_ekonomi = tk.Label(root, text="Nilai Ekonomi: ")
label_ekonomi.pack()
entry_ekonomi = tk.Entry(root)
entry_ekonomi.pack()

label_sosiologi = tk.Label(root, text="Nilai Sosiologi: ")
label_sosiologi.pack()
entry_sosiologi = tk.Entry(root)
entry_sosiologi.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

root.mainloop()