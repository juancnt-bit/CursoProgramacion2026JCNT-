

# es primo contar cuantos divisores tiene un numero. si tiene exactamente 2 es primo
mult=0
num = int (input("ingrese un numero: "))
for i in range (1,num+1,1): 
    res = num %(i)
    if res ==0:
          mult=mult+1
print("tiene ",mult, "divisores ") 
if mult==2:
     print(num," es un numero primo")
else:
     print(num, " no es un numero primo")
