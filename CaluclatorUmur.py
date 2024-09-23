
#Nama: Rafael Zefanya Jaya Surya
#Nama: Sebastian Dion


jumlah_kalkulasi = int(input('jumlah kalkulasi yang diinginkan: '))
while True:
    #menerima input dari user tanggal, bulan, tahun lahir dalam bentuk angka
    tbt_hri_ini = input('tanggal hari ini (dd/mm/yyyy): ')
        
    #untuk cek jika input yang dimasukan user hanya nomor
    check_tbt_hri_ini = all([x.isdigit() for x in tbt_hri_ini.split('/')]) and int(tbt_hri_ini.split('/')[0]) <=31 and int(tbt_hri_ini.split('/')[1]) <=12
        
    #jika input sudah benar, akan keluar dari loop dan melanjutkan program
    if check_tbt_hri_ini:
        break
        
    #jika input salah, akan terus meminta input dari user
    else:
        print('input anda kurang cocok...')
        
tgl_hri_ini, bln_hri_ini, thn_hri_ini = tuple(tbt_hri_ini.split('/'))

for x in range(jumlah_kalkulasi):
    while True:
        tbt_lahir = input('tanggal lahir (dd/mm/yyyy): ')
        check_tbt_lahir = all([x.isdigit() for x in tbt_lahir.split('/')]) and int(tbt_lahir.split('/')[0]) <=31 and int(tbt_lahir.split('/')[1]) <=12

        if check_tbt_lahir:
            break

        else:
            print('input anda kurang cocok...')

    tgl_lahir, bln_lahir, thn_lahir = tuple(tbt_lahir.split('/'))
    slisih_thn = int(thn_hri_ini) - int(thn_lahir)

    #untuk cek apakah sudah ulang tahun pada tahun ini
    if int(bln_lahir) > int(bln_hri_ini):
        slisih_thn -=1
        slisih_bln = 12 - (int(bln_lahir) - int(bln_hri_ini))

    elif int(bln_lahir) == int(bln_hri_ini):
        slisih_bln = 0
            
        if int(tgl_lahir) == int(tgl_hri_ini):
            print('selamat ulang tahun!')
            
    else:
        slisih_bln = int(bln_hri_ini) - int(bln_lahir)
            


    print('Umur anda {} tahun dan {} bulan!'.format(slisih_thn,slisih_bln))
