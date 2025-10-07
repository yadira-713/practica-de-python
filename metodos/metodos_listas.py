
#creando una lista con list()
lista = list(["hola","yadira",20,"ramen"])

#devuelve la cantidad e elementos de la lista
cantidad_elementos = len(lista)

#agregando un elementos a la lista
lista.append("mariscos")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"elemento distinto")

#agregar varios elementos a la lista
lista.extend(["escobedo","quispe"])

#eliminar un elemento de la lista(por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el penultimo y asi sucesiamente

#removiendo un elemento de la lista por su valor
lista.remove("mariscos")

#elimininando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True, ordena en reversa) deben ser numeros
lista.sort()

#invirtiendo los elementos de una lista 
lista.reverse()



print(lista)