from selenium import webdriver

browser = webdriver.Chrome()

class Testpagina_de_login:
    def test_iniciar_browser(self):
        browser.get('https://www.saucedemo.com/')
        print('Browser Iniciado com Sucesso!')

    def test_preencher_usuario(self):
        caixa_de_usuario = browser.find_element_by_id("user-name")
        caixa_de_usuario.send_keys('standard_user')
        print("Usuário Preenchido com Sucesso!")

    def test_preencher_senha(self):
        caixa_de_senha = browser.find_element_by_id("password")
        caixa_de_senha.send_keys('secret_sauce')
        print("Senha Preenchida com Sucesso!")

    def test_clicar_login(self):
        botao_de_login = browser.find_element_by_id("login-button")
        botao_de_login.click()