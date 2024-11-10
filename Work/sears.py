hdinheiro = 0.11 * 0.001
htorre = 442 
n_notas = 1
day = 1

while n_notas*hdinheiro < htorre:
	print (day, n_notas, n_notas*hdinheiro)
	day = day + 1 
	n_notas = n_notas*2
print('Número de dias:', day)
print('Número de notas:', n_notas)
print('Altura final', n_notas*hdinheiro)



#22/10/24
htorre = 442
hdinheiro = 0.11*0.001  #0.11 mm -> 0.00011 m 

n_notas = 1
dias = 1

while n_notas*hdinheiro < htorre:
    print('Dia:', dias, 'Número de notas:', n_notas, 'Altura total:', n_notas*hdinheiro )
    n_notas = n_notas*2
    dias += 1
print(f"Atualmente, no total de {dias} dias, o número de notas é {n_notas}, resultando em {n_notas*hdinheiro} de altura")
