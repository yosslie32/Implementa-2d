texto=input("Tu texto: ")
if texto== texto.upper():
    abc="0123456789"
else:
    abc="1234567890"
k=int(input("Valor de desplazamiento "))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("Texto cifrado: ", cifrad)
                    
