#primero cambiamos la terminal a la de bash
#lo primero es configurar tu nombre de usuario en la terminal, esto se configura una unica vez en la computadora, no lo tengo q hacer cada vez q arranque un trabajo en git
#luego hay q abrir la terminal y colocar  git init para crear la carpeta repositorio
def mensaje():
    print(" estoy trabajando con git")
mensaje()

def sumar(n1,n2):
    print("resultado: ", n1 + n2)

sumar(int(input("ingresa el primer numero: ")), input("ingresa el segundo: "))


def multiplicacion(n1,n2):
    print("resultado: ", n1 * n2)

multiplicacion(int(input("ingresa el primer numero: ")), input("ingresa el segundo: "))

#para ver en q estado están mir archivos ecribir en la terminal git status
#para agregarlos git add . o git add nombre del archivo
#git commit -m un mensaje que aclare lo q agregamos a esta version , para que pase al repositorio
#para citar o ver las versiones guardadas poner git log
# si quiero verlas reducidas poner git --oneline
# si quiero volver a una version pasada, debo poner git checkout y el numero o nombre de identificacion de la version, despues podes volver a las versiones actuales con git checkout master (o main si tenes main)
#si vamos ahcia atras, podemos modificar una version, pero, todo lo q sigue, la linea de tiempo que sigue, se borrará, por tanto, para cambiar versiones pasadas y mezclarlas con las del futuro, devemos poner git merge master y luego pasar a los 3 estados, git add y git commit 
# "master" es como la rama madre, como la linea de tiempo original
#para crear otra rama usamos git branch nombre de la rama
# git branch consulta la cantidad de ramas que tenemos
# para posicionarme en la nueva rama ongo git checkout nombre de la rama

def mensaje3():
    print("estoy en la rama chinona")