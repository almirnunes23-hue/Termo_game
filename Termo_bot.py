from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import choice
from time import sleep
import unicodedata
import string



class termo_game: 

    def __init__(self, palavras, driver):

        self.driver = driver
        self.palavras = palavras

        self.uberdict = {
            letra: {
                "certas": set(),
                "erradas": set(),
                "repeticoes": 0
            }
            for letra in string.ascii_lowercase
        }

    
    def play_termo(self):

        self.driver.get("https://term.ooo")
        sleep(3)

        campo = self.driver.find_element(By.TAG_NAME, "body")
        campo.click()

        palavra = choice(self.palavras)
        palavra = self.remover_acentos(palavra)
        campo.send_keys(palavra, Keys.ENTER)

        for row in range(5):
            sleep(3)
            
            indices = self.positions(row, palavra)
            self.uberdict = self.knowledge(indices)
            self.palavras = self.filtering(self.palavras)

            palavra = choice(self.palavras)
            palavra = self.remover_acentos(palavra)
            campo.send_keys(palavra, Keys.ENTER)


    def positions(self, row, palavra):

        board = self.driver.find_element(By.TAG_NAME, "wc-board")
        board_shadow = board.shadow_root

        rows = board_shadow.find_elements(By.CSS_SELECTOR, "wc-row")
        row_shadow = rows[row].shadow_root

        letters = row_shadow.find_elements(By.CSS_SELECTOR, "div")

        indices = {}

        for l in range(5):
            
            valor1 = letters[l].get_attribute("class")
            valor2 = palavra[l]

            indices[l] = (valor1, valor2)

        return indices
    

    def filtering(self, palavras):
        
        for letras, valores in self.uberdict.items():

            if (
                len(valores["certas"]) == 0
                and len(valores["erradas"]) == 0
                and valores["repeticoes"] == 0
        ):
                continue

            for pos in valores["certas"]:
                palavras = [p for p in palavras if p[pos] == letras]

            for pos in valores["erradas"]:
                palavras = [p for p in palavras if p[pos] != letras]
        
            palavras = [p for p in palavras if p.count(letras) >= valores["repeticoes"]]

        return palavras
    

    def knowledge(self, indices):

        aparicoes = {}
        
        for parte in indices.items():
         
            letra = parte[1][1]
            valor = parte[1][0]
            local = parte[0]
            codice = self.uberdict[letra]

            if valor == "letter right":

                aparicoes[letra] = aparicoes.get(letra, 0) + 1
                codice["certas"].add(local)
                codice["erradas"].discard(local) if local in codice["erradas"] else None

            elif valor == "letter place":

                aparicoes[letra] = aparicoes.get(letra, 0) + 1
                codice["erradas"].add(local)

            elif valor == "letter wrong":

                if len(codice["certas"]) < aparicoes.get(letra, 0):
                    codice["erradas"].add(local)

                elif len(codice["certas"]) > 0:
                    codice["erradas"].update({0, 1, 2, 3, 4})
                    for x in codice["certas"]:
                        codice["erradas"].discard(x)

                else:
                    codice["erradas"].update({0, 1, 2, 3, 4})

        for entrada, saida in aparicoes.items():
            self.uberdict[entrada]["repeticoes"] = saida

        return self.uberdict


    def remover_acentos(self, texto):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )


driver = webdriver.Chrome()

with open("respostas_termo.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo]

ll = termo_game(palavras, driver)

ll.play_termo()