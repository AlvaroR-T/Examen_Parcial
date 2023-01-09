#Entrada
print("La suma que se genera a partir de los valores digitados será, a partir de los datos brindados")
#Declaración de una variable
num=int(input("Cuántos números se desea registrar por su persona: "))
#Proceso
if num<=0:
    print("Número no válido")
else:
    sum=0
    for i in range(1,num+1): #En python de consideera desde cero el conteo
        a=float(input(f"Escriba el número {i} :"))
        sum=sum+a
    print("la suma que se proporciona,a partir de los datos brindados es:", sum)
