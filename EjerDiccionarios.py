monedas={"euro":"E","dolar":"$","Yen":"Y"}
divisa=input("Digite una divisa (euro,dolar,Yen): ")
valor=monedas.get(divisa)
if valor:
    print("Su simbolo es ",valor)
else:
    print(" Unknow money!..")    

print("**********************************")

nombre=input("Nombre: ")
edad=input("Edad: ")
dir=input("Direccion: ")
tel=input("Telefono: ")
d=dict(nombre=nombre,edad=edad,Direccion=dir, telefono=tel)
print(d.get("nombre")," tiene ",d.get("edad")," años y vive en ",\
    d.get("Direccion")," su numero de telegono es ",d.get("telefono"))
