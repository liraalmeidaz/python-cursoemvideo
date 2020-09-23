import math
an = float(input('Digite o ângulo que você deseja')
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f} '.format(an, sen))
co = math.cos(math.radians(an))
print('O ângulo tem de {} tem o cosseno de {:.2f}'.format(an, co))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente {} de {:.2f} '.format(an, tan))