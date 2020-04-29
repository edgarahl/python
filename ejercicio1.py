lista=["Python","Ingenieria Industrial","Ing. en Computacion"]
print("Yo estudio: ")
for i in lista:
    print(i)



print("*********************")
asignaturas=[]
notas=[]
for i in range(10):
    valor=input("Digite los modulos. ")
    if not valor: 
        break
    asignaturas.append(valor)
    valor=input("Digite la nota: ")
    notas.append(valor)

for indice,valor in enumerate(asignaturas,0):
    print("En ",valor," la nota es ",notas[indice])

    
print("Yo estudio las asignaturas ", asignaturas)
print("Y Mis notas son: ", notas)

print("*****************************")
tam=len(asignaturas)
for i in range(tam):
    print("En ",asignaturas[i]," la nota es ",notas[i])