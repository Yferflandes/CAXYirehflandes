import random 
#agregar el resto del abecedario 

#volver el codigo infinito usando un while True

#permite que el usuario seleccione la longitud de su password 
base="abcdefghijklmnñopqrstuvwxyz"
number=input("¿cuántos caracteres debe tener tu password?")

while True:
 passw="" 

 for i in range (int(input)):
  passw=passw+random.choice(base)
  print("password",passw)
  input()
  
  
