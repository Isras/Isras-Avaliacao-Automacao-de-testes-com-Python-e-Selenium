from pages.test_pagina_de_login import *

class Testpagina_de_resumo:
    def test_verificar_pagina_de_resumo(self):
        if browser.current_url != 'https://www.saucedemo.com/checkout-step-two.html':
            print('URL Diferente detectada! Encerrando Programa!')
            exit()
        else:
            print("Página de resumo carregada com sucesso")

    def test_finalizar_pedido(self):
        botao_finalizar = browser.find_element_by_id('finish')
        botao_finalizar.click()
        print("Compra Finalizada!")