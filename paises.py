import json
import sys


import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requsição", url)

def parsing(texto_da_resposta):
    try:    
        resultado = json.loads(texto_da_resposta)
        return resultado
    except:
        print("Erro ao fezer o parsing")

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)
       

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])

def mostrar_população(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("{}: {}".format(pais["name"], pais["population"]))
    else:
        print("País não encontrado")

def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais)) 
    if resposta:
        lista_pais_moeda = parsing(resposta)   
        if lista_pais_moeda:
            for pais in lista_pais_moeda:
                print("Moedas do {}".format(pais["name"]))
                moedas = pais["currencies"]
            for moeda in moedas:
                print("{}: {}".format(moeda["name"], moeda["code"]))    
    else:
        print("País não encontrado")

def ler_nome_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais
    except:
        print("Preciso do nome do país")        

if __name__ == "__main__":
    if len(sys.argv) == 1:

        print("Bem vindo ao sistema de paises ##") 
        print("Uso: python paises.py <acao> <nome do país> ") 
        print("Ações disponíveis: contagem, moeda, populaçao") 
    else:
        argumento1 = sys.argv[1]
        argumento2 = sys.argv[2]

        if argumento1 == "contagem":
            numero_paises = contagem_de_paises()
            print("Existem {} paises no mundo todo".format(numero_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "população":
            pais = ler_nome_pais()
            if ler_nome_pais:
                mostrar_população(pais)
        else:
            print("Argumento inválido")    


