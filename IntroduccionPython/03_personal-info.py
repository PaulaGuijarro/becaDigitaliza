print ("Datos personales:")
try:
  nombre = input("Nombre: ")
  apellido = input("Apellido: ")
  telefono = int(input("Telefono: "))
  edad = int(input("Edad: "))
  print ("Su nombre es " + nombre + " " + apellido +". Tiene " + str(edad) + " años, y su número de telefono es: " + str(telefono))
except ValueError:
  print ("Error: el valor introducido no es adecuado")
except:
    print ("Se ha producido un error")

