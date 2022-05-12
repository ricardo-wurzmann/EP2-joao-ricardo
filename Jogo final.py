#normalizando base países
import Funcoes
import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
#print(dados)
 
 #criando variaveis para rodar no while
Tentativa='o'
chances = 20
lista_tentativas_paises=[]

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

sorteado = Funcoes.sorteia_pais(Base_países.DADOS)


while Tentativa != sorteado and chances>0:
    print('Você ainda tem {} tentativas'.format(chances))
    Tentativa=input('digite seu comando ou sua tentativa: ')
    #ainda precisa fazer códico dando dica para o mano
    if Tentativa=='dica':
        chances-=1
    
    #mo burrão se desistir claramente não faz insper
    elif Tentativa=='desisto':
        chances-=1
        break

    #não sei o que faz no inventário (coloquei aqui pq vc meteu nas instruções)
    elif Tentativa=='inventario':
        Tentativa=0
    
    # se estiver nao acontece nada só volta para o inicio do while
    elif Tentativa in lista_tentativas_paises:
        Tentativa=0

    #caso acertar sair do while
    elif Tentativa==sorteado:
        chances-=1
        break

    # depois do else ver se o pais tentado existe,
    # se ele existir contabilizar ele na quantidade de tentativas, calcular a distancia de haverstine 
    # e colocar diferentes cores para as diferentes distancias  
    else:
        print('bananão')



'''jogo_denovo = input('Você quer jogar novamente? [s/n]')
if jogo_denovo == 'n':
    break
else:
    continue'''