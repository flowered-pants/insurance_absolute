import time

from selene import browser,be,have

class MortgageInsurancePage:
    def open_page(self):
        browser.open('https://www.absolutins.ru/fizicheskie-lica/strahovanie-pri-ipoteke/ipoteka/')
        time.sleep(5)
        browser.element('.policy--show').execute_script('element.remove()')
        browser.driver.execute_script('window.scrollBy(0, 400)')
        browser.element('button.light-blue:nth-child(1)').should(be.clickable).click()
        time.sleep(4)
        browser.driver.execute_script('window.scrollBy(0, 300)')
        browser.element('div.select-bank__item:nth-child(1) > svg:nth-child(3)').click()