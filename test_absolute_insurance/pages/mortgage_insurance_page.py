from selene import browser

class MortgageInsurancePage:
    def open_page(self):
        browser.open('https://www.absolutins.ru/fizicheskie-lica/strahovanie-pri-ipoteke/ipoteka/')
        browser.driver.execute_script('window.scrollBy(0, 400)')
