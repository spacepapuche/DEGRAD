from math import *

def cs(x):
  for i in range(x+1):
    print("")

cs(10)

print("         CONVERTISSEUR")
print("       DEGRÉS -> RADIANS")
print("       RADIANS -> DEGRÉS\n")

print("\"1\" POUR DEGRÉS VERS RADIANS")
print("\"2\" POUR RADIANS VERS DEGRÉS\n")
print("        COPYRIGHT 2021\n")

reponse=int(input())

while reponse<1 or reponse>2:
  reponse=int(input())
if reponse==1:
  deg=int(input("Indiquez le nombre de degrés :"))
  rad=radians(deg)
  print(rad,"radians")
elif reponse==2:
  rad=int(input("Indiquez le nombre de radians :"))
  deg=degrees(rad)
  print(deg,"degrés")
