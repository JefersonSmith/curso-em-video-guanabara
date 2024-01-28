import math

angulo = float(input('Escolha um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}')