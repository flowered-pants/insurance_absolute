from test_absolute_insurance.pages.mortgage_insurance_page import MortgageInsurancePage
import allure

mortgage_insurance_page = MortgageInsurancePage()

def test_of_making_mortgage_insurance_application(browser_managment):
    mortgage_insurance_page.open_page()

