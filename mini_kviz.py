pitanja = [
    ("Koja je najveća planina u Hrvatskoj?","DINARA"),
    ("Koja je najduža rijeka u Hrvatskoj?","SAVA"),
    ("Koji je glavni grad u Hrvatskoj?","ZAGREB")
    ]

bodovi = 0

for pitanje,tocan_odgovor in pitanja:
    print(pitanje)
    odgovor = input("Tvoj odgovor : ")
    if odgovor.upper() == tocan_odgovor :
       bodovi += 1
print(f"Tvoji bodovi {bodovi}/3")

if bodovi == 3:
    print("ODLIČNO")
elif bodovi == 2:
    print("DOBRO")
else:
    print("POKUŠAJ PONOVO"
          "")




