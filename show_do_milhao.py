name = input("What is your name ")
dinheiro = 0
qntd_pulos = 3


import requests
import json
import getpass


url = "https://opentdb.com/api.php?amount=5&category=15&difficulty=hard&type=multiple"
response = requests.get(url)
data = json.loads(response.text)

for item in data['results']:
    print(item['question'])
    for answer in item['incorrect_answers']:
        print(answer)
    print(item['correct_answer'])
    print("vc tbm pode pular")
    resposta = input("type your answer ")
    if resposta == item['correct_answer']:
        print("CERTA RESPOSTA!!!")
        dinheiro += 1000
    if resposta == "pular":
        if qntd_pulos > 0:
            print(" blz vc pulou")
            qntd_pulos -= 1
        else:
            print("vai pular a sua mãr")
    if resposta != item['correct_answer']:
        print("ERROUUUUUUU")
        print("vc leva apenas ",dinheiro / 2," para casa")
        break

print("                                                                                                            agora vamos a proxima fase, voceê pode desistir ou levar 5 mil, vc quer desistir?                                                                     ")
desistencia = input('                                                                                                 vc quer ??? ')
if desistencia == "sim":
    print("parabens vc levou 5 mil")
    exit()
else:
    dinheiro = 10000

    for item in data['results']:
        print(item['question'])
        for answer in item['incorrect_answers']:
            print(answer)
    print(item['correct_answer'])
    print("vc tbm pode pular")
    resposta = input("type your answer ")
    if resposta == item['correct_answer']:
        print("CERTA RESPOSTA!!!")
        dinheiro += 10000
    if resposta == "pular":
        if qntd_pulos > 0:
            print(" blz vc pulou")
            qntd_pulos -= 1
        else:
            print("vai pular a sua mãr")
    if resposta != item['correct_answer']:
        print("ERROUUUUUUU")
        print("vc leva apenas ",dinheiro / 2," para casa")
        exit()

print("                                                                                                            agora vamos a proxima fase, voceê pode desistir ou levar 50 mil, vc quer desistir?                                                                     ")
desistencia = input('                                                                                                 vc quer ??? ')
if desistencia == "sim":
    print("parabens vc levou 5 mil")
    exit()
else:
    dinheiro = 100000

    for item in data['results']:
        print(item['question'])
        for answer in item['incorrect_answers']:
            print(answer)
        print(item['correct_answer'])
        print("vc tbm pode pular")
        resposta = input("type your answer ")
        if resposta == item['correct_answer']:
            print("CERTA RESPOSTA!!!")
            dinheiro += 100000
        if resposta == "pular":
            if qntd_pulos > 0:
                print(" blz vc pulou")
                qntd_pulos -= 1
            else:
                print("vai pular a sua mãe")
        if resposta != item['correct_answer']:
            print("ERROUUUUUUU")
            print("vc leva apenas ",dinheiro / 2," para casa")
            exit()

print("vc desiste e sai com 500mil ou vai para a pergunta de 1 milhão e tem a chance de per")
print("vamos para a pergunta final")
