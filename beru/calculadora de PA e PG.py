print("Qual as operações a seguir você quer? \nProgressão Aritmétrica (PA)\nProgessão Geométrica(PG)\nPor favor usar sigla")
operação = input("Qual das opções acima? ").upper()

if operação == "PA":
    a1 = float(input("Valor de a1 "))
    a2 = float(input("Valor de a2 "))
    a3 = float(input("Valor de a3 "))
    n = float(input("Qual o termo que quer descobrir "))
    R = a2 - a1
    R2 = a3 - a2
    if R == R2:
        Sn = ((2 * a1 + (n-1) * R) * n )/2
        An = a1 + (n-1) * R
        print("Razão = {}\nValor do termo = {}\nSoma do termo = {}" .format(R, An, Sn))

elif operação == "PG":
    A1 = float(input("Valor de A1: "))
    A2 = float(input("Valor de A2: "))
    A3 = float(input("Valor de A3: "))
    n = float(input("Qual o termo que quer descobrir: "))
    R1PG = A2/A1
    R2PG= A3/A2
    if R1PG == R2PG:
        An = A1 * R1PG**(n-1)
        print("Razão: {}\nValor do termo: {}" .format(R1PG, An))
