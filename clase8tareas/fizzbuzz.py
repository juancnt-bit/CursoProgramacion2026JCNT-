#fizzbuzz del 1 al 30 :<<fizz>> si es multiplo de 3. <<buzz>> si es de 5, <<fizzBuzz>> si es de los dos.
num = int(input("ingrese un numero del 1 al 30: "))
mul = num%3
mult = num%5
if mul == 0 and mult==0:
    print("<<fizzbuzz>> ")
elif mul==0:
    print("<<fizz>>")
elif mult==0:
    print("<<buzz>>")
else:
    print("no es multiplo de 3 ni 5")



print("fin")