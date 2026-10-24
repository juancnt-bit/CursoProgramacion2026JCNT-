i=1000
while i>0:
    print(i)
    nomero=int(input("ingrese su gasto"))
    if nomero > i:
        print("no tines esa cantidad de dinero")
    else:
        i=i-nomero
    print(i)



print("se te acabo el dinero")



