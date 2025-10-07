nome=(input("insira o seu nome\n"))
Sexo=(input("qual o seu sexo\n"))
altura=float(input("insira a sua altura em centimetros\n"))



if Sexo != 'm' and Sexo != 'f':
    print("Insira o sexo com m ou f")

else:
   

    if Sexo =="m":
         if altura <=174:
            print("baixo")
         if altura >174 and altura <182:
            print("estatura normal")
         if altura >=183:
            print("alto")


    if Sexo =="f":
         if altura <=164:
            print("baixo")
         if altura >164 and altura <174:
            print("estatura normal")
         if altura >=175:
            print("alto")
            