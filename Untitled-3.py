f = open("1.txt", "w")
f.write("glaZirOVani pisunczki")
try:
  a = int(input())
  b = int(input())
  print(a/b)
except ZeroDivisionError:
  print("Дура йобана на 0 ділити нізя!") 
 