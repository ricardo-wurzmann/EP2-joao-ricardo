#normalizando base países
import Funcoes
import Base_países
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

sorteado = Funcoes.sorteia_pais(Base_países.DADOS)

#criando variaveis para rodar no while
Tentativa='o'
quantidade_tentativa=0
lista_tentativas_paises=[]

while Tentativa != sorteado or quantidade_tentativa<20:
    print('Você já fez {} tentativas'.format(quantidade_tentativa))
    Tentativa=input('digite seu comando ou sua tentativa: ')
    #ainda precisa fazer códico dando dica para o mano
    if Tentativa=='dica':
        quantidade_tentativa+=1
    
    #mo burrão se desistir claramente não faz insper
    elif Tentativa=='desisto':
        quantidade_tentativa+=1
        break

    #não sei o que faz no inventário (coloquei aqui pq vc meteu nas instruções)
    elif Tentativa=='inventario':
        Tentativa=0
    
    # se estiver nao acontece nada só volta para o inicio do while
    elif Tentativa in lista_tentativas_paises:
        Tentativa=0

    #caso acertar sair do while
    elif Tentativa==sorteado:
        quantidade_tentativa+=1
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