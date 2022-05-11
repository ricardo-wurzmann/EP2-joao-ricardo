#normalizando base países
import Funcoes
from Funcoes import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
#print(dados)

chances = 20 
print(" ============================")
print("|                            |")
print("| Bem-vindo ao Insper Países |")
print("|                            |")
print(" ==== Design de Software ==== ")
print(" Comandos:")
print("    dica       - entra no mercado de dicas")
print("    desisto    - desiste da rodada")
print("    inventario - exibe sua posição")
print("Um país foi escolhido, tente adivinhar!")
print("Você tem {0} tentativa(s)".format(chances) )
print("Qual seu palpite?")


from Funcoes import sorteia_pais
sorteado = Funcoes.sorteia_pais(Base_países.DADOS)
chute = input('Qual o seu palpite? ')
while chute != sorteado:
    print('Distâncias:')
#    print('     haversine')
    print('Dicas:')
    print('Você tem {0} tentativa(s)'.format(chutes-1))
    chute = input('Qual o seu palpite? ')


'''jogo_denovo = input('Você quer jogar novamente? [s/n]')
if jogo_denovo == 'n':
    break
else:
    continue'''
