from selenium.webdriver.common.keys import Keys
from pages.test_pagina_de_login import *
from pages.test_pagina_inicial import *

class Testpagina_do_carrinho:
    def test_verificar_pagina_do_carrinho(self):
        if browser.current_url != 'https://www.saucedemo.com/cart.html':
            print('URL Diferente detectada! Encerrando Programa!')
            exit()
        else:
            print("Carrinho acessado com sucesso!")

    def test_prosseguir_para_checkout(self):
        botao_checkout = browser.find_element_by_name('checkout')
        botao_checkout.click()
