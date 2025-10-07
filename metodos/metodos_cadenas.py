
#los metodos son el dato.el nombre del metodo y los parentesis

cadena1="hola,soy Yadira"
cadena2= "bienvenidos a python"

#convierte a mayusculas
mayust = cadena1.upper()
 
#convierte a minusculas
minusc = cadena1.lower() 

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1 si no encuentra un valor 
busqueda_find = cadena1.find("d") 
 
#buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepcion 
busqueda_index = cadena1.index("d")
 
#si es numerico, devolvemos true si no devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true ,sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de veces que se coincide
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada , si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada , si es asi devuelve true
termina_con = cadena1.endswith("a")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma,por el valor 2
cadena_nueva = cadena1.replace("Yadira","Angela")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada[0])