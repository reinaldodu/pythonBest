import random
options = ("piedra", "papel", "tijera")
ganaPc=0
ganaUser=0
round=1
puntos=3 #Número de puntos a jugar
print (f"JUEGO PIEDRA PAPEL O TIJERA - (Gana el que tenga {puntos} puntos)")
while ganaPc<puntos and ganaUser<puntos:
  print('-'*10)
  print('Round ', round)
  print('-'*10)
  pc = random.choice(options)
  user = input("piedra, papel o tijera...").lower()
  if not user in options:
    print("Opción invalida (escriba solamente piedra, papel o tijera) \n")
    continue
  round+=1
  if user == pc:
    print(f"Empate! pc=>{pc} user=>{user}")
  elif (user=='piedra' and pc=='tijera') or (user=='papel' and pc=='piedra') or (user=='tijera' and pc=='papel'):
    print (f'Gano! pc=>{pc} user=>{user}')
    ganaUser+=1
  else:
    print(f'Perdio! pc=>{pc} user=>{user}')
    ganaPc+=1
  print(f'puntos: PC=>{ganaPc} User=>{ganaUser}\n')
