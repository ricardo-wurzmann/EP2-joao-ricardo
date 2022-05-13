#normalizando base países
from operator import itemgetter
from random import random
import Funcoes
import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
#print(dados)
jogar='s'
while jogar=='s': 
    #criando variaveis para rodar no while
    distancias= []
    dicas = []
    Tentativa=''
    chances = 20
    lista_tentativas_paises=[]

    print("       ============================")
    print("      |                            |")
    print("      | Bem-vindo ao Insper Países |")
    print("      |                            |")
    print("       ==== Design de Software ==== ")
    print("\n Comandos:")
    print("    dica       - entra no mercado de dicas")
    print("    desisto    - desiste da rodada")
    print("    inventario - exibe sua posição")
    print("\n Um país foi escolhido, tente adivinhar!")
    print("\n Você tem {0} tentativa(s)".format(chances) )

    sorteado = Funcoes.sorteia_pais(dados)
    print(sorteado)


    while Tentativa != sorteado and chances>0:
        print('\n Você ainda tem {} tentativas'.format(chances))
        Tentativa=input('\n digite seu comando ou sua tentativa: ')
        #esse if é o da dica
        #precisa ajustar dica da bandeira e a da capital
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

    
            # aqui precisa colocar a distancia do pais que foi tentado, colocar as dicas que já foram
        elif Tentativa in lista_tentativas_paises:
            print('Você já tentou esse País')
            print('Distâncias: ')
            print('Dicas: {0}'.format(dicas))
            print("Você tem {0} tentativa(s)".format(chances) )
        

            #caso acertar sair do while
        elif Tentativa==sorteado:
            print("*** Parabéns! Você acertou depois de {0} tentativas".format((20-chances)))
            break


            #falta colocar a distancia de havertine
            #colocar cores diferentes para cada distancia

        else:
            if Tentativa in dados:
                chances-=1
                lista_tentativas_paises.append(Tentativa)
                #so fiz para testar outra funcionalidade(tirar esse if e else)
                if Tentativa=='brasil':
                    distancia_pais=1
                else:
                    distancia_pais=0
                distancias.append([Tentativa,distancia_pais])
                distancias = Funcoes.adiciona_em_ordem(distancias)

            else:
                print('esse não é um país válido')
        print('\nDistancias:\n')
        for i in range(len(distancias)):
            print('{}km--->{}'.format(distancias[i][1],distancias[i][0]))
    jogar=input('você quer jogar donvo(s/n)')
    