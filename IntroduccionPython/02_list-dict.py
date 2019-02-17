# Creación de listas
listStr = ["beca", "digitaliza", "cisco"]
listInt = [1, 2, 3, 4, 5]
listTypes = ["programacion", 4, "redes", 9.5, "python", 2]

# Imprimir por pantalla la información de las listas
print (listStr)
print (listInt)
print (listTypes)

# Asignar a una variable el último valor de cada lista
lastStr = listStr[-1]
lastInt = listInt[-1]
lastTypes = listTypes[-1]

# Imprimir por pantalla un texto y contatenar variable

print ("Ultimos valores de cada lista:", lastStr, str(lastInt), str(lastTypes))

# Diccionario de peliculas: autor -película

films = {
  "Sidney Lumet": "Doce hombres sin piedad",
  "Charles Chaplin": "Luces de la ciudad",
  "Quentin Tarantino": "Pulp Fiction",
  "Billy Wilder": "El apartamento"
}
# Imprimir por pantalla
print (films)
print (films.keys())
print (films.values())

