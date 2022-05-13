#normalizando base países
from operator import itemgetter
import Funcoes
import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
#print(dados)
 
#criando variaveis para rodar no while
distancias= []
dicas = []
Tentativa=''
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

sorteado = Funcoes.sorteia_pais(dados)
print(sorteado)


while Tentativa != sorteado and chances>0:
    print('Você ainda tem {} tentativas'.format(chances))
    Tentativa=input('digite seu comando ou sua tentativa: ')
    #ainda precisa fazer códico dando dica para o mano
    if Tentativa=='dica':
        escolha_dica=10
        lista_escolha_dica=[0,1,2,3,4,5]
        while escolha_dica not in lista_escolha_dica: 
            print('    Mercado de Dicas')
            print('----------------------------------------')
            print('1. Cor da bandeira  - custa 4 tentativas')
            print('2. Letra da capital - custa 3 tentativas')
            print('3. Área             - custa 6 tentativas')
            print('4. População        - custa 5 tentativas')
            print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica')
            print('----------------------------------------')
            escolha_dica = int(input('Escolha sua opção [0|1|2|3|4|5]: '))
            if escolha_dica == 0:
                print('Não tem dica')
            elif escolha_dica == 1:
                print('as cores da bandeira são:{}'.format(dados[sorteado]['bandeira']))
                chances-=4
            elif escolha_dica == 2:
                #falta dar um random para só dar uma letra da capital
                print('A capital é: {}'.format(dados[sorteado]['capital']))
                chances-=3
            elif escolha_dica == 3:
                print('A Área é: {}'.format(dados[sorteado]['area']))
                chances-=6
            elif escolha_dica == 4:
                print('A População é: {}'.format(dados[sorteado]['populacao']))
                chances-=5  
            elif escolha_dica == 5:
                print('O continente é: {}'.format(dados[sorteado]['continente']))
                chances-=7
            else:
                print('você escolheu um número inválido.')
        
         

    
        #mo burrão se desistir claramente não faz insper
    elif Tentativa=='desisto':
        desistencia=input('Você quer mesmo desistir? [s/n]')
        if desistencia == 's':
            break

    
        # se estiver nao acontece nada só volta para o inicio do while
    elif Tentativa in lista_tentativas_paises:
        print('Você já tentou esse País')
        print('Distâncias: ')
        print('Dicas: {0}'.format(dicas))
        print("Você tem {0} tentativa(s)".format(chances) )
        

        #caso acertar sair do while
    elif Tentativa==sorteado:
        print("*** Parabéns! Você acertou depois de {0} tentativas".format((20-chances)))
        break

    # se ele existir contabilizar ele na quantidade de tentativas, calcular a distancia de haverstine 
    # e colocar diferentes cores para as diferentes distancias  
        # depois do else ver se o pais tentado existe,
        # se ele existir contabilizar ele na quantidade de tentativas, calcular a distancia de haverstine 
        # e colocar diferentes cores para as diferentes distancias  
    else:
        if Tentativa in dados:
            chances-=1
            print('esse não é o país')
            lista_tentativas_paises.append(Tentativa)
            distancia_pais = Funcoes.haversine(sorteado - Tentativa)
            distancias.append(distancia_pais)
            distancias = adiciona_em_ordem(distancias):

        else:
            print('esse não é um país válido')



'''jogo_denovo = input('Você quer jogar novamente? [s/n]')
if jogo_denovo == 'n':
    break
else:
    continue'''