from pages.test_pagina_de_login import *
from pages.test_pagina_de_checkout import *
from pages.test_pagina_do_carrinho import *
from pages.test_pagina_inicial import *
from pages.test_pagina_resumo import *

if __name__ == "__main__":
    teste_pagina_de_login = Testpagina_de_login()
    teste_pagina_de_login.test_iniciar_browser()
    teste_pagina_de_login.test_preencher_usuario()
    teste_pagina_de_login.test_preencher_senha()
    teste_pagina_de_login.test_clicar_login()
    
    teste_pagina_inicial = Testpagina_inicial()
    teste_pagina_inicial.test_verificar_paginainicial()
    teste_pagina_inicial.test_adicionar_mochila()
    teste_pagina_inicial.test_adicionar_camiseta_preta()
    teste_pagina_inicial.test_acessar_carrinho()

    teste_pagina_do_carrinho = Testpagina_do_carrinho()
    teste_pagina_do_carrinho.test_verificar_pagina_do_carrinho()
    teste_pagina_do_carrinho.test_prosseguir_para_checkout()

    teste_pagina_de_checkout = Testpagina_de_checkout()
    teste_pagina_de_checkout.test_verificar_pagina_de_checkout()
    teste_pagina_de_checkout.test_preencher_nome()
    teste_pagina_de_checkout.test_preencher_sobrenome()
    teste_pagina_de_checkout.test_preencher_cep()
    teste_pagina_de_checkout.test_prosseguir_para_resumo()

    teste_pagina_de_revisao = Testpagina_de_resumo()
    teste_pagina_de_revisao.test_verificar_pagina_de_resumo()
    teste_pagina_de_revisao.test_finalizar_pedido()