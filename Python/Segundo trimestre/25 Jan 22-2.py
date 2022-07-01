import datetime 

dia=datetime.date.today()

w=dia.weekday()+1

if (w==0):
  print("feliz domingo")

elif (w==2):
  print("ay no,es martes")

elif  (w==3):
  print("ya es miercoles")

elif (w==4):
  print("es jueves chica")

elif (w==5):
  print("¡chica ya es viernes!")

elif (w==1)
  print("es lunes 😒")

else:
  print("yahoo,es sabado")