# Modulos
import random
import json
from time import sleep

def menu():
    print('''      ----- MENU ------
[1] ... Lotomania
[2] ... Quina
[3] ... Mega-Sena
[4] ... Lotofácil
[5] ... Dupla Sena
[6] ... Timemania
[7] ... Dia de Sorte
[8] ... Super Sete
[9] ... + Milionária

[0] ... Sair do Programa
        ''')
    entr = input('Digite a Opção Desejada: ')
    
    try:
        num_retorno = int(entr)
        return(num_retorno)
    except ValueError:
        return("Opção invalida")

#Funções de sorteio:
# Função para interar lista e comparar
def sortear_n(ns_sorteio, lista):
    lista_jogo = []
    while len(lista_jogo) != ns_sorteio:
        y = random.choice(lista)
        lista_jogo = [i for i in lista_jogo if i != y] #Função de busca em lista
        lista_jogo.append(y)
    return(lista_jogo)

# Função para chamar a função sortear_n passando os parametros e "cleanar" numeros
def chamada_sorteio(num_s, t_m):
    l_jogo = sortear_n(num_s, range(1, t_m))
    l_jogo.sort()        
    return(l_jogo)

# Função Para Sortear Time do TimeMania
def Timemania():
    times = []
    with open('Timemania.json', 'r',encoding="utf-8") as t:
        times = json.load(t)
        lista = times['timess']
        time_s = random.choice(lista)
    return(time_s)

def meses():
    with open('Meses.json', 'r',encoding="utf-8") as t:
        mes = json.load(t)
        m_sortei = mes['Meses']
        me_s= random.choice(m_sortei)
        return(me_s)

frases = ["Boa Sorte!","Voçê Pode Ser o Proximo Milhonário", "Sorte é Só um Detalhe",
"Nunca Desista!", "A Sorte Baterá a Sua Porta"]
# Variaveis // PARCIAL
#lista_jogo = []
#num_sorteados = 5 #definida pelo menu
#tm_mx = 15 #definida pelo menu

while menu != 0:
    opcao = menu()
    match opcao:

        case 1:
            print(f'''\n          LOTOMANIA  
Numeros da Sorte:''')
            lotomania = chamada_sorteio(20, 100)
            for l in lotomania:
                said = str(print(l, end=" "))
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)

        case 2:
            print(f'''\n          QUINA  
Numeros da Sorte:''')
            quina = chamada_sorteio(5, 81)
            for l in quina:
                said = str(print(l, end=" "))
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)
            

        case 3:
            print(f'''\n          MEGA-SENA  
Numeros da Sorte:''')
            mgs = chamada_sorteio(6, 61)
            for l in mgs:
                said = str(print(l, end=" "))
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)
            

        case 4:
            print(f'''\n          LOTOFÁCIL  
Numeros da Sorte:''')
            ltf = chamada_sorteio(15, 26)
            for l in ltf:
                    said = str(print(l, end=" "))
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)
            
        case 5:
            print(f'''\n          DUPLA SENA  
Numeros da Sorte:''')
            x = 0
            while x != 2:
                dps = chamada_sorteio(6, 51)
                for l in dps:
                    said = str(print(l, end=" "))
                print(said[:-50])    # gambiarra
                x += 1
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)

        case 6:
            print(f'''\n          TIME MANIA  
Numeros da Sorte:''')
            time_sorteado = Timemania()
            tmn = chamada_sorteio(7, 81)
            for l in tmn:
                said = str(print(l, end=" "))
            print(f'\nTime Do Coração: {time_sorteado}')
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)

        case 7:
            print(f'''\n          DIA DE SORTE  
Numeros da Sorte:''')
            mes = meses()
            dds = chamada_sorteio(7, 32)
            for l in dds:
                    said = str(print(l, end=" "))
            print(f'\nMês da Sorte: {mes}')
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)
            
        case 8:
            print(f'''\n          SUPER SETE  
Colunas da Sorte:''')
            x = 0
            while x != 7:
                sst = chamada_sorteio(1, 10)
                for l in sst:
                    print(f"Coluna: {x + 1}")
                    said = str(print(l, end=" "))
                print(said[:-50])    # gambiarra
                x += 1
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)

        case 9:
            print(f'''\n          + MILIONÁRIA  
Numeros da Sorte:''')
            num_1 = random.choice(range(1,7))
            num_2 = random.choice(range(1,7))
            mlnr = chamada_sorteio(6, 51)
            for l in mlnr:
                    said = str(print(l, end=" "))
            print(f'\nTrevo Sorteados: {num_1}  {num_2} ')
            msg_final = random.choice(frases)
            print(f"\n{msg_final}\n\n")
            sleep(3)
            

            
            
        
        
        
        
        
        
        
        case 0:
            print('Saindo...')
            menu = 0
