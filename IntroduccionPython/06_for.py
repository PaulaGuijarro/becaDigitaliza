nameList = ["Pepe", "Juan", "Pedro", "Antonio", "Luis"]
selected = []

for name in nameList:
  print ("Nombre:",name)
  if "a" in name.lower():
    selected.append(name)
print ("Lista de nombres que contienen la vocal a",selected)