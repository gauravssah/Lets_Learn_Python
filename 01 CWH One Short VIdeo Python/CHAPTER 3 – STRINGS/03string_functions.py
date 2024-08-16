name = "Gaurav"

print(len(name)) # 6
print(name.endswith("rav")) # True
print(name.startswith("p")) # False
print(name.count("r")) # 1
print(name.count("A")) # 0
print(name.count("a")) # 2

print(name.find("a")) # 2
print(name.find("z")) # -1

print(name.replace("a","A")) # GAurAv

print(" ".join(name)) # G a u r a v

print(name.upper()) # GAURAV

print(name.lower()) # gaurav

print(name.title()) # Gaurav

print(name.swapcase()) # gAURAV

print(name.center(20,"*")) # *******Gaurav*******

print(name.zfill(20)) # 00000000000000Gaurav

