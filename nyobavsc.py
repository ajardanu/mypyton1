import random #import modul random untuk menggunakan fungsi yang disediakan modul tersebut
def start():
    while True: #perulangan untuk jika terjadi kesalahan input atau input tidak sesua kriteria akan terus meminta
        try:
            pilih_banyak = int(input('masukkan banyak soal maksimal 8! '))
        except ValueError:  #jika  terjadi value error yang diinput bukan berupa int
            print('Masukin Angka aja deh jangan macem macem!')
        else:
            if pilih_banyak < 4:
                print('Kedikitan!')
            elif pilih_banyak > 8:
                print('maksimal 8 coy!')
            else:
                print(f'Good choice {pilih_banyak}!')
                new_game(pilih_banyak)
                break #untuk memberhentikan perulangan
#---------------------------------------------------------------
def new_game(k):
    jawaban = [] #menyiapkan list kosong
    jawaban_yang_benar = 0 #menyiapka variabel untuk menyimpan berapa banyak soal yang benar

    test = random.sample(list(soal.keys()),k) #fungsi untuk memilih secara acak dictionary yang di ubah kedalam list
    for key in test:                         #fungsi random.sample() akan memilih secara acak sebanyak k yang ditentukan
        print('---------------------------------------------------')
        print(key)
        index = list(soal.keys()).index(key) #membuat soal menjadi list dan mengambil index dengan parameter v key.
        for j in answer[index]:             #akan mengambil value pada list answer sesuai index yang sesuia dengan yang
            print(j)                        #sudah ditentukan pada V index
        jawab = input('pilih jawaban! ')
        jawab = jawab.upper()
        jawaban.append(jawab)

        jawaban_yang_benar += check_answer(soal.get(key),jawab)

    display_score(test,jawaban_yang_benar,jawaban,k)
#---------------------------------------------------------------
def check_answer(kunci_jawaban,jawab):
    if kunci_jawaban == jawab:
        print('Anda benar :)')
        return 1
    else:
        print('Anda Salah :(')
        return 0
#---------------------------------------------------------------
def display_score(cek,jawaban_yang_benar,jawaban,pil):
    print('---------------------------------------------------')
    print('Hasil!!')
    print('---------------------------------------------------')

    print('Kunci Jawaban: ',end='')
    for i in cek:
        print(soal.get(i),end=' ')
    print()

    print('Jawaban Anda: ',end='')
    for i in jawaban:
        print(i,end=' ')
    print()

    skor = int(jawaban_yang_benar/pil*100)
    print('Skor Anda: ' + str(skor))
#---------------------------------------------------------------
def try_again():
    respon = input('Try Again? (Yes/No) ')
    respon = respon.upper()

    if respon.startswith('Y'):
        return True
    else:
        return False
#---------------------------------------------------------------
soal = {
    'Apa nama ibu kota Indonesia?':'B',
    'Apa warna bendera Indonesia?':'C',
    'Pulau terbesar di Indonesia adalah?':'A',
    'Siapa burung yang menjadi lambang negara Indonesia?':'A',
    'Apa nama lagu kebangsaan Indonesia?':'C',
    'Gunung tertinggi di Indonesia adalah?':'B',
    'Binatang khas dari Pulau Komodo adalah?':'A',
    'Hari Kemerdekaan Indonesia diperingati setiap tanggal?':'B'
}

answer = [
    ['A. Serang','B. Jakarta','C. Bandung'],
    ['A. Putih dan Hijau','B. Merah dan Biru','C. Merah dan Putih'],
    ['A. Kalimantan','B. Bali','C. Sulawesi'],
    ['A. Garuda','B. Elang','C. Burung Puyuh'],
    ['A. Indonesia Pusaka','B. Haari Merdeka','C. Indonesi Raya'],
    ['A. Gunung Merapi','B. Puncak Jaya','C. Gunung Everst'],
    ['A. Komodo','B. Orang utan','C. Kakak Tua'],
    ['A. 1 April','B. 17 Agustus','C. 28 Oktober']
]

start() #awal

while try_again():
    start()

print('GG!')