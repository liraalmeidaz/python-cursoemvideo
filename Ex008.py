medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: {}cm e {:.0f}mm {}dm {}dam {}hm {}km'.format(medida, mm, cm, dm, dam, hm, km, ))