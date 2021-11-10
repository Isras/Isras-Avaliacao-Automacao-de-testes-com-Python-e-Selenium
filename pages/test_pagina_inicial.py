from pages.test_pagina_de_login import *

class Testpagina_inicial:
    def test_verificar_paginainicial(self):
        if browser.current_url != 'https://www.saucedemo.com/inventory.html':
            print('URL Diferente detectada! Encerrando Programa!')
            exit()
        try:
            browser.find_element_by_class_name('title')
            print("Login feito com Sucesso!")
            print("Página inicial carregada com sucesso!")
        except OSError:
            print("Página Inicial não foi carregada corretamente!")
            print("Encerrando Programa!")
            exit()
    
    def test_adicionar_mochila(self):
        mochila = browser.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]')
        mochila.click()
        try:
            browser.find_element_by_name('remove-sauce-labs-backpack')
            print('Mochila Adicionada com Sucesso')
        except:
            print('Ocorreu um erro ao tentar adicionar a mochila ao carrinho!')

    def test_adicionar_camiseta_preta(self):
        camiseta = browser.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        camiseta.click()
        try:
            browser.find_element_by_name('remove-sauce-labs-bolt-t-shirt')
            print('Camiseta Preta Adicionada com Sucesso')
        except:
            print('Ocorreu um erro ao tentar adicionar a Camiseta Preta ao carrinho!')

    def test_acessar_carrinho(self):
        botao_carrinho = browser.find_element_by_id('shopping_cart_container')
        botao_carrinho.click()