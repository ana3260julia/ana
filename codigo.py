def soma(numeroA, numeroB):
  resultado = numeroA + numeroB
  print(f"O resultado da soma é: {resultado}")
  
def multiplicacao(numeroA, numeroB):
  resultado =  numeroA * numeroB 
  print(f"O resultado da multiplição é: {resultado}")
  
def divisao(numeroA, numeroB):
  resultado = numeroA / numeroB
  print(f"O resultado da divisão é: {resultado}")

def raizquadrada(numeroA):
  resultado = numeroA ** 0.5 
  print(f"O resultado da raízquadrada é : {resultado}")

def subtracao(numeroA,numeroB):
  resultado= numeroA -numeroB
  print(f"O resultado da subtracao é:{resultado}")

opcao = int(input("MENU: 1. SOMA\n 2. SUBTRAÇÂO\n 3. MUTIPLICACAO\n 4.DIVISAO\n 5.RAIZQUADRADA"))

if (opcao == 1):
  numeroA = float(input("Digite o 1º número: "))
  numeroB = float(input("Digite o 2º número: "))
  soma(numeroA, numeroB)

elif (opcao == 2):
  numeroA= float(input("Digite o 1º número:"))
  numeroB=float(input("Digite o 2º número:"))
  subtracao(numeroA,numeroB)

elif(opcao==3):
  numeroA= float(input("Digite o 1º número:"))
  numeroB=float(input("Digite o 2º número:"))
  multiplicacao(numeroA,numeroB)

elif(opcao==4):
 numeroA= float(input("Digite o 1º número:"))
 numeroB=float(input("Digite o 2º número:"))
 divisao(numeroA,numeroB)

elif(opcao==5):
  numeroA= float(input("Digite o 1º número:"))
  numeroB=float(input("Digite o 2º número:"))
  raizquadrada(numeroA)
