while True:
  grade1=int(input("write your grade 1:"))
  grade2=int(input("write your grade 2:"))
  grade3=int(input("write your grade 3:"))

  plus=int(grade1+grade2+grade3)
   average=plus/3
   print("This is your average")
 if(average>6):
   print("You ok")
   if(average<6):
     print("Fail")
  if(average>9):
    print("Very good")
  