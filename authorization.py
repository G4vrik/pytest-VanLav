from pages.login_page import LoginPage

def authorization(browser):
    login_page = LoginPage(browser)
    
    login_page.open()

    login_page.enter_username("тестпользователь21")

    login_page.enter_password("тестпользователь21")

    login_page.click_login()
    
    header_text = login_page.get_header_text()
    assert header_text == "Главная", f"Expected 'Главная', but got '{header_text}'"