def calcular_iva(monto):
    iva=monto*0.15
    suma=monto+iva
    return iva, suma

def pedir_nombres():
    nombre=input("Digite su Nombre: ")
    valor=input("Calcular Iva: ")
    return nombre, float(valor)

calc_iva = lambda  monto:monto*0.15

name,monto=pedir_nombres()
iva, total=calcular_iva(monto)
otro_iva = calc_iva(float(monto))
print(name)
print("valor=",monto)
print("Iva= ",iva)
print("Otro Iva= ",otro_iva)
print("Total= ",total)
resultado=" {} \n valor={}\n iva={} \nTotal={}".format(name,monto,iva,total)
f=open("data3.txt","w")
f.write(resultado)
f.close()


