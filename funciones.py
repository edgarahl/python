def calcular_iva(monto):
    iva=monto*0.15
    suma=monto+iva
    return iva, suma

def pedir_nombres():
    nombre=input("Digite su Nombre: ")
    valor=input("Calcular Iva: ")
    return nombre, float(valor)

name,monto=pedir_nombres()
iva, total=calcular_iva(monto)
print(name)
print("valor=",monto)
print("Iva= ",iva)
print("Total= ",total)


