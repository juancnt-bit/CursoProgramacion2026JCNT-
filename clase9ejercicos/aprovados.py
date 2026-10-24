#vaprobados.py pedir 5 notas y contar cuantos aprobaron

aprobado = 0
reprobado = 0
for i in range (1,6):
    nota =int(input("ingrese una nota"))
    if nota >= 61:
        aprobados =aprobados+1
    else:
        reprobados =reprobados +1
print("los aprobados son: ",aprobados)
print("los reprobados son: ",reprobados)