import percepcion
import razonamiento
import accion

def run ():
    nombre = ""
    while True:
        nombre = percepcion.leerNombre()

        if(nombre == "salir"):break

        if(razonamiento.valida(nombre)):
            accion.darBienvenida(nombre)
        else:
            accion.error(nombre)


if __name__ == "__main__":
    run()

