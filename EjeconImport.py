from iva import calc_iva

def pedir_nombres():
    nombre=input("Digite su Nombre: ")
    valor=input("Calcular Iva: ")
    return nombre, float(valor)

name,monto=pedir_nombres()
iva = calc_iva(float(monto))
total = monto + iva
print(name)
print("valor=",monto)
print("Iva= ",iva)
print("Total= ",total)
