import sqlite3

def crear_db():
    conexion=sqlite3.connect("multiplicaciones.db")
    cursor=conexion.cursor()
    try:
        cursor.execute("CREATE TABLE jugador (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(255) NOT NULL, apellidos varchar(255) NOT NULL, edad INTEGER, dni varchar(255) NOT NULL)")
        cursor.execute("CREATE TABLE partida (id INTEGER PRIMARY KEY AUTOINCREMENT, dni_jugador INTEGER NOT NULL, num_aciertos INTEGER NOT NULL, FOREIGN KEY (dni_jugador) REFERENCES jugador(dni))")
    except:
        print("Las tablas no han sido creadas o están repetidas")
    else:
        conexion.commit()
        print("Las tablas han sido creadas")
    finally:
        cursor.close()
        conexion.close()

def añadir_jugadores():
    conexion=sqlite3.connect("multiplicaciones.db")
    cursor=conexion.cursor()
    jug1_nombre=input("Dime el nombre del jugador 1: ")
    jug1_apellidos=input("Dime los apellidos del jugador 1: ")
    jug1_edad=input("Dime la edad del jugador 1: ")
    jug1_dni=input("Dime el dni del jugador 1: ")
    jug2_nombre=input("Dime el nombre del jugador 2: ")
    jug2_apellidos=input("Dime los apellidos del jugador 2: ")
    jug2_edad=input("Dime la edad del jugador 2: ")
    jug2_dni=input("Dime el dni del jugador 2: ")
    try:
        cursor.execute("INSERT INTO jugador VALUES(null, '"+jug1_nombre+"', '"+jug1_apellidos+"', '"+jug1_edad+"', '"+jug1_dni+"')")
        cursor.execute("INSERT INTO jugador VALUES(null, '"+jug2_nombre+"', '"+jug2_apellidos+"', '"+jug2_edad+"', '"+jug2_dni+"')")
    except:
        print("Los jugadores no han sido añadidos")
    else:
        conexion.commit()
        print("Los jugadores han sido añadidos")
    finally:
        cursor.close()
        conexion.close()

def añadir_partidas():
    conexion=sqlite3.connect("multiplicaciones.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM jugador")
    jugadores=cursor.fetchall()
    i=1
    print("JUGADORES DISPONIBLES")
    for jugador in jugadores:
        print(jugador[1], end="==>")
        print(jugador[4])
        i+=1
    jug_opcion=input("Dime el dni del jugador a ingresar partida: ")
    aciertos_p1=input("Dime el número de aciertos en la primera partida: ")
    aciertos_p2=input("Dime el número de aciertos en la segunda partida: ")
    try:
        cursor.execute("INSERT INTO partida VALUES(null, '"+jug_opcion+"', '"+aciertos_p1+"')")
        cursor.execute("INSERT INTO partida VALUES(null, '"+jug_opcion+"', '"+aciertos_p2+"')")
    except:
        print("Los datos no han sido introducidos o están repetidos")
    else:
        conexion.commit()
        print("Los datos han sido introducidos")
    finally:
        cursor.close()
        conexion.close()

def ver_aciertos():
    conexion=sqlite3.connect("multiplicaciones.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM jugador")
    jugadores=cursor.fetchall()
    i=1
    print("JUGADORES DISPONIBLES")
    for jugador in jugadores:
        print(jugador[1], end="==>")
        print(jugador[4])
        i+=1
    in_dni=input("Dime el dni del jugador que quieras ver: ")
    cursor.execute("SELECT * FROM partida WHERE dni_jugador='"+in_dni+"'")
    partidas=cursor.fetchall()
    i=1
    print("RESULTADOS")
    for partida in partidas:
        print(partida[0], end=".-")
        print(partida[2])
        i+=1
    cursor.close()
    conexion.close()