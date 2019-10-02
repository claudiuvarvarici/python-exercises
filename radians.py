import math

def a(degrees):
  radians = degrees / 360.0 * 2 * math.pi
  print(str(degrees)+"°")
  print (radians)
  print(math.sin(radians))
a(45)

def b():
  degrees = input("Please, enter degrees of angle:")
  radians = float(degrees) / 360.0 * 2 * math.pi
  print(str(degrees)+"°")
  print (radians)
  print(math.sin(radians))
b()