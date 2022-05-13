#normaliza base países
def normaliza(dicionario):
    d={}
    for k in dicionario.keys():
        for t,c in dicionario[k].items():
            d[t]=c
            d[t]['continente']=k
    return d

#sorteia Paises
import random
def sorteia_pais(dicio):
    randomkeys=random.choice(list(dicio.keys()))
    return randomkeys


#distancia de haverstine
import math
def haversine (p1, l1, p2, l2):
    r = 6371
    p1_rad = math.radians(p1)
    l1_rad = math.radians(l1)
    p2_rad = math.radians(p2)
    l2_rad = math.radians(l2)

    seno = (math.sin((p2_rad-p1_rad)/2))**2
    mais = math.cos(p1_rad)*math.cos(p2_rad)*(math.sin((l2_rad-l1_rad)/2))**2
    d = 2 * r * math.asin(math.sqrt(seno+mais))
    return d

#adicionando lista ordenada
from operator import itemgetter
def adiciona_em_ordem(lista):
    return(sorted(lista,key=itemgetter(1)))

#esta na lista?
def esta_na_lista(pais,lista):
    for i in lista:
        if pais in i:
            return True
    return False