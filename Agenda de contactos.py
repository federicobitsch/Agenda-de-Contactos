import os 

def limpiar():  
    os.system('cls')
 

menu = {} 

def agregar (menu): 
    nombre = input("Ingrese el Nombre: ") 
    apellido = input("Ingrese el Apellido: ")
    telefono = int(input("Ingrese el numero Telefonico: "))
    correo = input("Ingrese el EMAIL: ")
    menu.update({nombre: (apellido,telefono, correo)})

    return menu


def mostrar(menu):
    for i in menu: 
        print(f""" 
            Nombre: {i} 
            Apellido: {menu[i][0]}                          
            Telefono: {menu[i][1]}
            Correo: {menu[i][2]}     
            """)
 

def buscar(menu): 
    i = input("Ingrese el nombre a BUSCAR : ") 
    for j in menu:
        if i in menu:
            print(f"""
            Nombre: {i}
            Apellido: {menu[i][0]}
            Telefono: {menu[i][1]}
            Correo: {menu[i][2]} """)       
            return                 
    print("*** NO SE ENCONTRO NINGUN CONTACTO ***")


def eliminar (menu):
    mostrar(menu)
    nom=input("Ingresar el contacto a eliminar: \n") 
    if nom in menu:
        menu.pop(nom)

     
    else:
        print(" ¡¡NO HAY NINGUN CONTACTO LLAMADO ASI!! ")


def imprimir_menu():
    print("""
*******AGENDA DE CONTACTOS*******
-----------------------
1- Agregar Contacto 
2- Mostrar Contactos
3- Buscar Contactos
4- Eliminar contactos
5- Salir 
-----------------------
*******AGENDA DE CONTACTOS********* 
""")

def main():
    while True:
        imprimir_menu()
        opcion  = int(input('Ingrese una opcion del MENU: '))
        if opcion == 1: #AGREGAR CONTACTO
            limpiar()
            print('*Vamos a Agregar el Contacto*')
            agregar(menu)
            
        elif opcion == 2: #Mostrar Contactos 
            limpiar()
            
            print('*Vamos a Mostrar los Contactos* : ')
            mostrar(menu)

        elif opcion == 3: #Buscar Contactos
            print('Vamos a Buscar los Contactos: ')
            buscar(menu)
        
        elif opcion == 4: #Eliminar Contactos
            print('Vamos a Eliminar los Contactos: ')
            eliminar(menu)
            
        elif opcion == 5: #Salir del programa.
            print('Vamos a Salir del programa ¡Adios!')
            break
            
        else:
            print("Por favor, ¡Introduzca una opcion valida! ")
        
main()
