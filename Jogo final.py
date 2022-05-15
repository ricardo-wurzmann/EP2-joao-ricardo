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
                    letras_sorteadas = Funcoes.sorteia_letra(dados[sorteado],2,['capital'],letras_sorteadas)
                    dicas_compradas.append(letras_sorteadas)
                    #falta dar um random para só dar uma letra da capital, acho que fiz
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
                    print('você escolheu um número inválido.')
            #parte de dar print em distancias
            print('\nDistancias:\n')
            for i in range(len(distancias)):
                print('   {:.0f}km--->{}'.format(distancias[i][1],distancias[i][0]))
        
            #parte de dar print em dicas
            print('\n Dicas:\n')
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
            print('\nDistancias:\n')
            for i in range(len(distancias)):
                print('   {:.0f}km--->{}'.format(distancias[i][1],distancias[i][0]))
        
            #parte de dar print em dicas
            print('\n Dicas:\n')
            dicas_compradas=Funcoes.adiciona_em_ordem(dicas_compradas)
            for i in range(len(dicas_compradas)):
                print('-{}:  {}{}'.format(dicas_compradas[i][2],dicas_compradas[i][0],dicas_compradas[i][3]))


    
        # caso ele tente um pais que já foi tentado    
        
        elif esta_na_lista==True:
            print('Você já tentou esse País')
        

            #caso acertar sair do while
        elif Tentativa==sorteado:
            print("*** Parabéns! Você acertou depois de {0} tentativas".format((20-chances)))
            break

        else:
            if Tentativa in dados:
                chances-=1
                lista_tentativas_paises.append(Tentativa)
                distancia_pais = Funcoes.haversine(dados[Tentativa]['geo']['latitude'],dados[Tentativa]['geo']['longitude'], dados[sorteado]['geo']['latitude'], dados[sorteado]['geo']['longitude'])
                distancias.append([Tentativa,distancia_pais])
                distancias = Funcoes.adiciona_em_ordem(distancias)

                #parte de dar print em distancias
                print('\nDistancias:\n')
                for i in range(len(distancias)):
                    print('   {:.0f}km--->{}'.format(distancias[i][1],distancias[i][0]))
        
                #parte de dar print em dicas
                print('\n Dicas:\n')
                dicas_compradas=Funcoes.adiciona_em_ordem(dicas_compradas)
                for i in range(len(dicas_compradas)):
                    print('-{}:  {}{}'.format(dicas_compradas[i][2],dicas_compradas[i][0],dicas_compradas[i][3]))

            else:
                print('esse não é um país válido')
        
            
    if chances == 0 and sorteado != Tentativa:
        print ('\n Você perdeu, tente melhorar, o país era {}'.format(sorteado))

    #parte para jogar denovo
    
    jogar=input('\n você quer jogar donvo(s/n)')
    