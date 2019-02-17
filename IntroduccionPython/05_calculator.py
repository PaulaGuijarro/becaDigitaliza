def solicitaNum():
  num = (float)(input("Escribe un número: "))
  return num

def suma(num1,num2):
  print ("La suma es",num1 + num2)

def resta(num1,num2):
  print ("La resta es",num1 - num2)

def multiplicacion(num1,num2):
  print ("La multiplicación es",num1 * num2)

def division(num1,num2):
  print ("La división es",num1 / num2)

def exponencial(num1,num2):
  print ("El exponencial es",num1 ** num2)

operaciones={1:suma,2:resta,3:multiplicacion,4:division,5:exponencial}
calculadoraON = True

while (calculadoraON):
  try:
    print ("CALCULADORA")
    print ("Selecciona la operación a realizar:")
    print ("1.- Suma")
    print ("2.- Resta")
    print ("3.- Multiplicacion")
    print ("4.- División")
    print ("5.- Exponencial")
    print ("q.- Salir")
    opcion =input("Escoge una opción: ")
    if (opcion == "q"):
      print("Saliendo...")
      calculadoraON = False
    else:
      opcion = int(opcion)
      if (0 < opcion <= 5):
        num1 = solicitaNum()
        num2 = solicitaNum()
        operaciones[opcion](num1,num2)
      else:
        print("No has escogido una opción correcta")
  except ZeroDivisionError:
    print ("Error: no se puede dividir por cero")
  except ValueError:
    print ("Error: el valor introducido no es adecuado")
  except:
    print ("Se ha producido un error")