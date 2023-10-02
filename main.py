import Multiplicaciones

def main():
    valor=True
    while valor==True:
        print("MENÚ DE OPCIONES")
        print("1.- Crear base de datos")
        print("2.- Añadir jugadores")
        print("3.- Añadir partidas")
        print("4.- Ver aciertos")
        print("5.- Salir")
        opcion=int(input("Selecciona una opción: "))
        if opcion==5:
            valor=False
        elif opcion==1:
            Multiplicaciones.crear_db()
        elif opcion==2:
            Multiplicaciones.añadir_jugadores()
        elif opcion==3:
            Multiplicaciones.añadir_partidas()
        elif opcion==4:
            Multiplicaciones.ver_aciertos()
    else:
        print("Has salido del programa")
main()