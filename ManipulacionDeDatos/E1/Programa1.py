# Resolver el siguiente ejercicio de programación
# El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. 



# En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa que calcule el sueldo promedio del empleado Juan. Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:



# a. Sueldo bajo: por debajo de 300 dólares.

# b. Sueldo normal:  entre 300 a 900.

# c. Sueldo mejor de lo normal: más de 900 dólares.



# Tip: se debe utilizar estructuras condicionales.

 

total_sueldo_ano = (300*6) + (500*4) + (700*2)
total_sueldo_promedio = total_sueldo_ano / 12
print(f'El sueldo total del año de Juan es ${total_sueldo_ano}')
print(f'El sueldo promedio de juan por mes es ${total_sueldo_promedio}')

if(total_sueldo_promedio >= 900):
    print("El sueldo de juan es mejor de lo normal")
elif(total_sueldo_promedio >= 300):
    print("El sueldo de juan es normal")
else:   
    print("El sueldo de juan es bajo")