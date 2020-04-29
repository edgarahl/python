archivo=open("data.txt")
nombre=archivo.readline()
edad=archivo.readline()
dir=archivo.readline()
tel=archivo.readline()
d=dict(nombre=nombre,edad=edad,Direccion=dir, telefono=tel)
print(d.get("nombre")," tiene ",d.get("edad")," años y vive en ",\
    d.get("Direccion"))
archivo.close()