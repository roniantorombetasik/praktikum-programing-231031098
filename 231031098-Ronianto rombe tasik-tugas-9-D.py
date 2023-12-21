
print('\n')
biodata = { 'nama'  : 'Ronianto Rombe Tasik',
'nim'   : '231031098',
'kelas' : 'S123-D',
'tempat,tanggal lahir' : 'Parepare,05 Oktober 2004',
'suku' : 'toraja',
'jenis kelamin' : 'Laki-laki',
'agama' : 'kristen',
'alamat': 'jalan Andi Cammi no.33',
'email' : 'roniantorombetasik@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)




