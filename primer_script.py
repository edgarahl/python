# Este es un comentario
""" Otra forma de comentar """

l=[1,2,3,4]
for x in l:
    print(x)

for x in range(10):
    print("linea ",x)

print("Longitud de la lista ",len(l))

print("Min:",min(l))
print("Max:",max(l))
print(l.index(2))

lista=["Managua","Rivas","Jinotepe","Esteli","Masaya"]
print("la lista es:",lista);
buscar="Rivas"
print(buscar," se encuentra en la posicion ",lista.index(buscar))

for c, value in enumerate(lista,1):
    print(c,value)

diccionario={'nombre':'Ruth','Edad':'34','cursos':["postgres","python","php"]}   
print("Nombre en el diccionario: ",diccionario['nombre'])

dic=dict(nombre='Edgar',Apellido='Luna',edad='52')
print(dic)