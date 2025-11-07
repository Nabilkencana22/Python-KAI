🧮 Analisis Nilai Siswa

Repositori ini berisi hasil praktikum analisis data nilai siswa menggunakan Python.
Tujuannya adalah untuk memahami distribusi, statistik deskriptif, serta visualisasi data nilai siswa berdasarkan mata pelajaran.

📘 Deskripsi Proyek

Dalam praktikum ini dilakukan analisis terhadap data nilai siswa (nilai_siswa.csv) menggunakan pendekatan eksploratif.
Program memanfaatkan pustaka:

Pandas untuk manipulasi data

NumPy untuk perhitungan statistik

Matplotlib & Seaborn untuk visualisasi data

Analisis ini meliputi:

Pengecekan data kosong (missing values)

Perhitungan nilai rata-rata, median, modus, dan standar deviasi

Visualisasi data dengan bar chart dan boxplot

⚙️ Struktur Program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()

📊 Hasil Analisis

Tabel Rata-rata Nilai per Mata Pelajaran

Mata Pelajaran	Rata-rata Nilai
Bahasa Indonesia	77.83
Matematika	85.75
Bahasa Inggris	87.67
Fisika	89.09
Produktif	84.00

✅ Fisika memiliki rata-rata nilai tertinggi yaitu 89.09

⚠️ Bahasa Indonesia memiliki nilai terendah, yaitu 60

Contoh Visualisasi

Grafik batang (Bar Chart) — menampilkan perbandingan rata-rata nilai antar mapel

Boxplot — menunjukkan sebaran nilai serta outlier

💬 Analisis dan Pertanyaan

Mapel mana yang memiliki rata-rata nilai tertinggi?
→ Mata pelajaran Fisika memiliki rata-rata nilai tertinggi (89.09).

Mapel mana yang memiliki nilai terendah?
→ Mata pelajaran Bahasa Indonesia memiliki nilai terendah (60).

Bagaimana visualisasi membantu dalam memahami data?
→ Visualisasi mempermudah dalam melihat perbandingan dan pola nilai antar mapel, serta mengidentifikasi penyebaran nilai dan outlier dengan cepat.

💭 Refleksi Siswa

Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?
→ Saya belajar bagaimana mengolah data menggunakan Python dan membuat grafik visual yang membantu memahami data secara intuitif.

Kesulitan apa yang kamu alami dalam membuat grafik?
→ Kesulitannya adalah memilih jenis grafik yang tepat dan mengatur tampilannya agar menarik serta mudah dibaca.

Menurut kamu, apakah AI membantu dalam analisis sebuah data?
→ Ya, AI sangat membantu dalam proses analisis karena mampu mempercepat perhitungan, mendeteksi pola tersembunyi, dan memberikan rekomendasi otomatis dari data.

🧠 Dibuat Oleh

Nama: Mohammad Kencana
Topik Praktikum: Analisis Data Nilai Siswa
Bahasa Pemrograman: Python
Framework & Tools: Pandas, Numpy, Matplotlib, Seaborn

📁 Cara Menjalankan

Clone repositori:

git clone https://github.com/username/analisis-nilai-siswa.git
cd analisis-nilai-siswa


Jalankan notebook:

jupyter notebook main.ipynb


Pastikan pustaka berikut telah terinstal:

pip install pandas numpy matplotlib seaborn


📈 Analisis ini bertujuan untuk melatih kemampuan analisis data secara profesional menggunakan Python serta memahami bagaimana visualisasi dapat memperjelas makna dari data mentah.