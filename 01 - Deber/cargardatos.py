import json

    
def cargar_datos():
    try:
        path="./01 - Deber/datos.json"
        archivo_abierto=open(path,'r')
        lineas=json.loads(archivo_abierto.read())
        archivo_abierto.close
        return lineas
    except:
        print("Error leyendo archivo")
    
def seleccionar_cancion(id):
    try:
        path="./01 - Deber/datos.json"
        archivo_abierto=open(path,'r')
        lineas=json.loads(archivo_abierto.read())
        archivo_abierto.close
        return lineas[id]
    except:
        print("Error leyendo archivo")

def menu_principal():
    print("Menu principal")
    print("Porfavor seleccione una opción");
    print("""
    [L]istar canciones
    [A]gregar cancion
    [E]scoger cancion
    [S]alir
    """)
    eleccion=input().upper()
    def listar_canciones():
        lista=cargar_datos()
        print("Lista de canciones:")
        for cancion in lista:
            print(f"{cancion['index']}) {cancion['nombre_cancion']} - {cancion['autor_cancion']} ")
        
        return menu_principal()
    def agregar_cancion():
        return "Agregar cancion"
    def escoger_cancion():
        print("Ingrese el id de la cancion que desea seleccionar")
        id=int(input())
        cancion_seleccionada=seleccionar_cancion(id) 
        print(f"""
        Cancion seleccionada:
        Id :{cancion_seleccionada['index']})
        Nombre :{cancion_seleccionada['nombre_cancion']}
        Autor/Banda :{cancion_seleccionada['autor_cancion']}
        Genero :{cancion_seleccionada['genero']}
        Acordes :{cancion_seleccionada['acordes']}
        """)   
        return menu_cancion(cancion_seleccionada)
    def salir():
        return print("salir")
    def devolver_respuesta():
        opciones={
            "L":listar_canciones,
            "A":agregar_cancion,
            "E":escoger_cancion,
            "S":salir
        }
        return opciones[eleccion]()
    return devolver_respuesta()
def menu_cancion(cancion):
    print("Menu canción:")
    print("Porfavor seleccione una opción");
    print("""
    [E]eliminar cancion
    [M]odificar cancion
    [V]olver menu principal""")
    eleccion=input().upper()
    def eliminar_cancion():
        return "Eliminar cancion"
    def modificar_cancion():
        return "Modificar cancion"
    
    def volver_al_menu():
        return menu_principal()
    def devolver_respuesta():
        opciones_cancion={
            "E":eliminar_cancion,
            "M":modificar_cancion,  
            "V":volver_al_menu          
        }
        return opciones_cancion[eleccion]()
    return devolver_respuesta()

menu_principal()


