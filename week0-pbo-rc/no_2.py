jumlah_siswa = int (input ("masukan jumlah siswa : "))
nilai_siswa = {}

for i in range (jumlah_siswa):
    nama = input (f"masukan nama siswa ke-{i+1} : ")
    nilai = int (input (f"masukan nilai {nama} : "))
    print ("")

    nilai_siswa[nama] = nilai

print (f"grades : {nilai_siswa}")