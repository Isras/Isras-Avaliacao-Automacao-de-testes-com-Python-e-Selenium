from selenium.webdriver.common.keys import Keys
from pages.test_pagina_de_login import *
from pages.test_pagina_do_carrinho import *

class Testpagina_de_checkout:
    def test_verificar_pagina_de_checkout(self):
        if browser.current_url != 'https://www.saucedemo.com/checkout-step-one.html':
            print('URL Diferente detectada! Encerrando Programa!')
            exit()
        else:
            print("Página de Checkout carregada com sucesso!")
    
    def test_preencher_nome(self):
        caixa_primeiro_nome = browser.find_element_by_id('first-name')
        caixa_primeiro_nome.send_keys('Compasso')
        print("Primeiro nome preenchido com sucesso!")

    def test_preencher_sobrenome(self):
        caixa_sobrenome = browser.find_element_by_id('last-name')
        caixa_sobrenome.send_keys('UOL')
        print("Sobrenome preenchido com sucesso!")

    def test_preencher_cep(self):
        caixa_cep = browser.find_element_by_id('postal-code')
        caixa_cep.send_keys('1234567')
        print("Cep preenchido com sucesso!")

    def test_prosseguir_para_resumo(self):
        botao_continuar = browser.find_element_by_id('continue')
        botao_continuar.click()
        print("Prosseguindo para Resumo!")