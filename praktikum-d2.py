print('praktikum-2\n\n')
print('==============ini and==============')
a = True
b = False
hasil= a and a
print('Nlai',a,'and',a,'adalah',hasil)
print()
hasil= a and b
print('Nlai',a,'and',b,'adalah',hasil)
print()
hasil= b and a
print('Nlai',b,'and',a,'adalah',hasil)
hasil= b and b
print()
print('Nlai',b,'and',b,'adalah',hasil)
print()
print('\n==============ini and==============')
hasil= a or a
print('Nlai',a,'or',a,'adalah',hasil)
print()
hasil= a or b
print('Nlai',a,'or',b,'adalah',hasil)
print()
hasil= b or a
print('Nlai',b,'or',a,'adalah',hasil)
hasil= b or b
print()
print('Nlai',b,'or',b,'adalah',hasil)
print()
print('\n==============ini not==============')
hasil = not a
print ('hasil not',a,'adalah',hasil)
hasil = not b
print ('hasil not',b,'adalah',hasil)
print('\n==============ini and==============')
hasil= a ^ a
print('Nlai',a,'xor',a,'adalah',hasil)
print()
hasil= a ^ b
print('Nlai',a,'xor',b,'adalah',hasil)
print()
hasil= b ^ a
print('Nlai',b,'xor',a,'adalah',hasil)
hasil= b ^ b
print()
print('Nlai',b,'xor',b,'adalah',hasil)
print()
print('==============ini nand==============')
a = True
b = False
hasil= not (a and a)
print('Nlai',a,'and',a,'adalah',hasil)
print()
hasil= not (a and b)
print('Nlai',a,'and',b,'adalah',hasil)
print()
hasil= not (b and a)
print('Nlai',b,'and',a,'adalah',hasil)
hasil= not (b and b)
print()
print('Nlai',b,'and',b,'adalah',hasil)
print()
print('\n==============ini nor==============')
hasil= not (a or a)
print('Nlai',a,'nor',a,'adalah',hasil)
print()
hasil= not (a or b)
print('Nlai',a,'nor',b,'adalah',hasil)
print()
hasil= not (b or a)
print('Nlai',b,'nor',a,'adalah',hasil)
hasil= not (b or b)
print()
print('Nlai',b,'nor',b,'adalah',hasil)
print()
print('\n==============ini nxor==============')
hasil= not (a ^ a)
print('Nlai',a,'xor',a,'adalah',hasil)
print()
hasil= not(a ^ b)
print('Nlai',a,'xor',b,'adalah',hasil)
print()
hasil= not(b ^ a)
print('Nlai',b,'xor',a,'adalah',hasil)
hasil= not (b ^ b)
print()
print('Nlai',b,'xor',b,'adalah',hasil)
print()
print('============== IS NOT')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
print('============== IS NO')
a = 5
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is  b
print('a is b =',hasil)
a = 6
b = 6
print('nilai',a,'memiliki identitas=',hex(id(a)))
print('nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is  b
print('a is b =',hasil)
print('\n============== IN')
nama= 'Bachruddin Jususf Habibie'
test = 'rud'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'bach'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'a'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'u'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'e'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'o'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
print('\n============== NOT IN')
# tugas buat nama menjadi nama lengkap masing 

nama =  'Ronianto Rombe tasik'
test = 'rud'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'bach'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'a'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'u'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'e'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))
test = 'o'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n============== IN')
data = ['institut',
        'teknologi',
        'Bachruddin',
        'jususf',
        'habibie']
print('data adalah',data)
test1= 'habibie'
test2 = 'parepare'
test3 = 'kampus'
test4 = 'institut'
cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))
print('\n============== NOT IN')
#tugas dengan cara yamg sama buat operator umtuk not in

print('data adalah',data)
test1= 'habibie'
test2 = 'parepare'
test3 = 'kampus'
test4 = 'institut'
cek = test1 not in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 not in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 not in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 not in data
print(test4,'terdapat di data adalah '+str(cek))

# ini operator bitwise
a = 5
b = 10
b += 80
print('\n============== and')
print ('nilai',a,'dalam biner    = ',format(a,'08b'))
print ('nilai',b,'dalam biner   = ',format(a,'08b'))
print('\n==============================AND')
c = a & b
print('nilai',a,'&',b,'biner adalah', format(c,'08b'))

print('\n============== or')
print ('nilai',a,'dalam biner    = ',format(a,'08b'))
print ('nilai',b,'dalam biner   = ',format(a,'08b'))
print('\n==============================or')
c = a & b
print('nilai',a,'&',b,'biner adalah', format(c,'08b'))

# tugas untuk operator XDR, c = a ^ b 
# tugas untuk operator not, c = ^a
# tugas untuk operator not, c = ^b
# tugas untuk operator geser kanan, c = a >> 2
# tugas untuk operator geser kiri, c= a<<2
# tugas untuk operator not and,





























