print("tempo do primeiro trecho: 8min e 15seg")
minutoPrimeiroTrecho = 8 * 60
segundoPrimeiroTrecho = 15

print("tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundotrecho = 12 * 3

print("tempo do terceiro trecho: 8min e 15seg")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15

# Soma o total de minutos e converte todos os segundos em minutos
totalTempoTodosTechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

# Soma o valor total dos segundos
totalTempoTodosTechosSegundos = (segundoPrimeiroTrecho + segundosSegundotrecho + segundoTerceiroTrecho)

restanteMinutos = int(totalTempoTodosTechosSegundos / 60)
restanteSegundos = totalTempoTodosTechosSegundos % 60

totalMinutos = totalTempoTodosTechosMinutos + restanteMinutos
totalSegundos = restanteSegundos

print("soma de tempo de todos os trechos: ", totalMinutos , "minutos")
print("soma de tempo de todos os trechos: ", totalSegundos , "segundos")

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos
tempoTrechoMinutosSegundos = totalMinutos * 60
horaChegada = int(((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos)/60) % 60)

print("o tempo de chegada foi de ", horaChegada,":", minutoChegada, restanteSegundos)