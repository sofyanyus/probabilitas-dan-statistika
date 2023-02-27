def nilai_terbanyak(deret):
  peta_kemunculan = {}
  for bilangan in deret:
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1

  bilangan_terbesar = deret[0] 
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar

inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []
for bilangan in inputan.split(','):
    data.append(int(bilangan))

print(f'Data -> {data}')
print(f'Modus -> {nilai_terbanyak(data)}')
