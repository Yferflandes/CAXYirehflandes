print("welcome to oxxo")
name=input ()
print ("cashier:",name)

item1=input () 
item2=input ()
item3=input ()
item4=input ()
item5=input ()

price1=int(input("add price"))
price2=int(input("add price 2"))
price3=int(input("add price 3"))
price4=int (input("add price 4"))
price5=int (input ("add price 5")) 

IVA=0.16

print ("the total amount to pay is",price1+price2+price3+price4+price5+IVA)

print ("##########ticket########")
print ("you bought",item1,price1,item2,price2,item3,price3,item4,price4,item5,price5)

print ("the total amount to pay is",price1+price2+price3+price4+price5+IVA)
