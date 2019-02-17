try:
  num = (int)(input("Escribe un número entero: "))

  if (num < 20):
    print ("El número", str(num),"es menor que 20.")
  elif (20 <= num <= 39):
    print ("El número", str(num),"está estre 20 y 39.")
  elif (40 <= num <= 59):
    print ("El número", str(num), "está estre 40 y 59.")
  else:
    print ("El número", str(num), "es igual o mayor que 60.")
except ValueError:
  print ("Error: el valor introducido no es adecuado")
except:
    print ("Se ha producido un error")

