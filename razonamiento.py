
def iniciaMayusculas(nombre):
    nombreAux = nombre.capitalize()
    return nombre == nombreAux

def exite(nombre):
    companeros = ["Marcela", "Martin", "Fernando", "Jose", "Diego", "Hael", "David"]
    return nombre in companeros

'''def valida(nombre):
    iniciaMay = iniciaMayusculas(nombre)
    existe = exite(nombre)
    return iniciaMay & existe, iniciaMay, existe
'''

def valida(nombre):
    companeros = ["Marcela", "Martin", "Fernando", "Jose", "Diego", "Hael", "David"]
    return nombre in companeros


    