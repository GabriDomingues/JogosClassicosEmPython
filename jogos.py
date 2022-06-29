import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu game!*******")
print("*********************************")

print("(1) forca (2) adivinhação")

jogo = int(input("qual jogo você quer jogar? "))

if(jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando adivinhação")
    adivinhacao.jogar()




