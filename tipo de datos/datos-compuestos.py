#creando una lista se puede modificar
lista = ["lucas dalto","soy dalto",True,3.42]

#creando una  tupla no se puede modificar
tupla = ("lucas dalto","soy dalto",True,3.42)

#esto es valido
#lista [3] = "maquinola"

#esto no es valido
#tupla [3] = "maquinola"

#creando un conjunto (set) (no se accede por indice y no permite repetidos)
conjunto = {"lucas dalto","soy dalto",True,1.85,"soy dalto"}

#print(conjunto[3])--> no se puede acceder al elemento 

#creando un diccionario (dict)
diccionario = {
    "nombre": "lucas dalto",
    "canal": "soy dalto",
    "esta_emocionado": True,
    "altura": 1.84,
    "dato_duplicado": "soy dalto"
}
print(diccionario["nombre"])