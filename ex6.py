print("Escolha a função")
print("----------------")
op=input("Soma = + \n Subtraçâo = -\n Multiplicaçâo = * \n Divisâo = / \n")


if op!="+" and op!="-" and op!="*" and op!="/":

    print("insira a funçâo correta")
else:

    Num1=int(input("Numero A\n"))
    Num2=int(input("Numero B\n"))

if op=="+":
    soma=Num1+Num2
    print("Resultado = ",soma)
if op=="-":
    sub=Num1-Num2
    print("Resultado = ", sub)
if op=="*":
    mult=Num1*Num2
    print("Resultado = ", mult)
if op=="/":
    div=Num1/Num2
    print("Resultado = " ,div)
    