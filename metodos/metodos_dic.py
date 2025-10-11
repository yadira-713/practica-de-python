diccionario = {
    "nombre" : "lucas",
    "apellido": "dalto",
    "subs" : 1000000
}
#no devuelve un objeto dict_items
claves = diccionario.keys()

#obteniendo un elemento con get() , (si no encunetra nada el programa continua )
valor_de_un_elemento = diccionario.get('jsjssj')
print('hola ')

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre","apellido")

#obteniendo un elemeno dicit_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
