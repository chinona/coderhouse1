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
#git commit para que pase al repositorio