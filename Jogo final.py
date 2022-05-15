#normalizando base países
from operator import itemgetter
from random import random
import Funcoes
import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
#print(dados)
jogar='s'
while jogar=='s': 
    #criando variaveis para rodar no while
    distancias= []
    letras_sorteadas = []
    dicas_compradas=[]
    Tentativa=''
    chances = 20
    lista_tentativas_paises=[]

    print("       ============================")
    print("      |                            |")
    print("      | Bem-vindo ao Insper Países |")
    print("      |                            |")
    print("       ==== Design de Software ==== ")
    print("\nComandos:")
    print("    dica       - entra no mercado de dicas")
    print("    desisto    - desiste da rodada")
    print("    inventario - exibe sua posição")
    print("\nUm país foi escolhido, tente adivinhar!")

    sorteado = Funcoes.sorteia_pais(dados)
    print(sorteado)


    while Tentativa.lower() != sorteado and chances>0:
        print('Você tem \033[35m{}\033[m tentativas'.format(chances))
        Tentativa=input('\ndigite seu comando ou sua tentativa: ')
        esta_na_lista=Funcoes.esta_na_lista(Tentativa,lista_tentativas_paises)
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
                    #precisa só aparecer uma cor de bandeira
                    dicas_compradas.append([dados[sorteado]['bandeira'],1,'cor da bandeira',''])
                    chances-=4
                elif escolha_dica == 2:
                    strcap=dados[sorteado]['capital']
                    letra_sorteada = Funcoes.sorteia_letra(strcap,letras_sorteadas)
                    if letra_sorteada=='':
                        print('\033[31mnão tem mais letras disponíveis\033[m')
                    else:
                        letras_sorteadas.append(letra_sorteada)
                        dicas_compradas.append([letra_sorteada,2,'uma letra da capital',''])
                        chances-=3
                elif escolha_dica == 3:
                    dicas_compradas.append([dados[sorteado]['area'],3,'Área',' km2'])
                    chances-=6
                elif escolha_dica == 4:
                    dicas_compradas.append([dados[sorteado]['populacao'],4,'Populacao',' habitantes'])
                    chances-=5  
                elif escolha_dica == 5:
                    dicas_compradas.append([dados[sorteado]['continente'],5,'Continente',''])
                    chances-=7
                else:
                    print('\033[31mvocê escolheu um número inválido.\033[m')
            #parte de dar print em distancias
            print('\n\033[35mDistancias:\033[m\n')
            for i in range(len(distancias)):
                if distancias[i][1]<1000:
                    print('   \033[32m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                elif distancias[i][1]<2000:
                    print('   \033[33m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                elif distancias[i][1]<5000:
                    print('   \033[34m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                else:
                    print('   \033[36m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
        
            #parte de dar print em dicas
            print('\n\033[35mDicas:\033[m\n')
            dicas_compradas=Funcoes.adiciona_em_ordem(dicas_compradas)
            for i in range(len(dicas_compradas)):
                print('-{}:  {}{}'.format(dicas_compradas[i][2],dicas_compradas[i][0],dicas_compradas[i][3]))
         

    
            #mo burrão se desistir claramente não faz insper
        elif Tentativa=='desisto':
            desistencia=input('Você quer mesmo desistir? [s/n]')
            if desistencia == 's':
                break

        #inventário
        elif Tentativa == 'inventario':
           #parte de dar print em distancias
            print('\n\033[35mDistancias:\033[m\n')
            for i in range(len(distancias)):
                if distancias[i][1]<1000:
                    print('   \033[32m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                elif distancias[i][1]<2000:
                    print('   \033[33m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                elif distancias[i][1]<5000:
                    print('   \033[34m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                else:
                    print('   \033[36m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
        
            #parte de dar print em dicas
            print('\n\033[35mDicas:\033[m\n')
            dicas_compradas=Funcoes.adiciona_em_ordem(dicas_compradas)
            for i in range(len(dicas_compradas)):
                print('-{}:  {}{}'.format(dicas_compradas[i][2],dicas_compradas[i][0],dicas_compradas[i][3]))
         


    
        # caso ele tente um pais que já foi tentado    
        
        elif esta_na_lista==True:
            print('\033[31mVocê já tentou esse País\033[m')
        

            #caso acertar sair do while
        elif Tentativa==sorteado:
            print("*** Parabéns! Você acertou depois de \033[35m{0}\033[m tentativas".format((20-chances)))
            break

        else:
            if Tentativa in dados:
                chances-=1
                lista_tentativas_paises.append(Tentativa)
                distancia_pais = Funcoes.haversine(dados[Tentativa]['geo']['latitude'],dados[Tentativa]['geo']['longitude'], dados[sorteado]['geo']['latitude'], dados[sorteado]['geo']['longitude'])
                distancias.append([Tentativa,distancia_pais])
                distancias = Funcoes.adiciona_em_ordem(distancias)

                #parte de dar print em distancias
                print('\n\033[35mDistancias:\033[m\n')
                for i in range(len(distancias)):
                    if distancias[i][1]<1000:
                        print('   \033[32m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                    elif distancias[i][1]<2000:
                        print('   \033[33m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                    elif distancias[i][1]<5000:
                        print('   \033[34m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                    else:
                        print('   \033[36m{:.0f}km--->{}\033[m'.format(distancias[i][1],distancias[i][0]))
                #parte de dar print em dicas
                print('\n \033[35mDicas:\033[m\n')
                dicas_compradas=Funcoes.adiciona_em_ordem(dicas_compradas)
                for i in range(len(dicas_compradas)):
                    print('-{}:  {}{}'.format(dicas_compradas[i][2],dicas_compradas[i][0],dicas_compradas[i][3]))
         

            else:
                print('\033[31messe não é um país válido\033[m')
        
            
    if chances == 0 and sorteado != Tentativa:
        print ('\nVocê perdeu, tente melhorar, o país era \033[35m{}\033[m'.format(sorteado))

    #parte para jogar denovo
    
    jogar=input('você quer jogar donvo(s/n)')
    