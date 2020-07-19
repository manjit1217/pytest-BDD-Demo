import os
import pytest
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Pom import Baseclass

# Constants
amazon = 'https://www.amazon.com/'


# Scenarios

# scenarios('../features/test_demo.feature')


# Fixtures

# Given Steps
@scenario('../features/test_demo.feature', 'Basic amazon Search')
def test_search(browser):
    pass


@scenario('../features/test_demo.feature', 'login to the amazon application')
def test_login(browser):
    pass



@given('go to the login page')
def go_to_login_page(browser):
    login_button = '//*[@id="nav-link-accountList"]'
    login_b=browser.find_element_by_xpath(login_button)
    login_b.click()
    
    # Baseclass.click_element(browser, login_button)


@when(parsers.parse('user enter the email "{email_id}"'))
def enter_phone_number(browser, email_id):
    email_id_field = '//*[@id="ap_email"]'
    continue_btn = '//*[@id="continue"]'
    emaild_id_fi=browser.find_element_by_xpath(email_id_field)
    emaild_id_fi.send_keys(email_id)
    continue_btn=browser.find_element_by_xpath(continue_btn)
    continue_btn.click()
    # Baseclass.click_element(browser, continue_btn)


@when(parsers.parse('user enter the password"{password}"'))
def enter_password(browser, password):
    password_field = '//*[@id="ap_password"]'
    login_btn = '//*[@id="signInSubmit"]'
    password_fi=browser.find_element_by_xpath(password_field)
    login_b=browser.find_element_by_xpath(login_btn)
    password_fi.send_keys(password)
    login_b.click()



@then(parsers.parse('login successfull "{success_msg}"'))
def login_success(browser, success_msg):
    get_success_msg = '//*[@id="nav-link-accountList"]/div/span'
    x=browser.find_element_by_xpath(get_success_msg)
    # user_name = Baseclass.get_text(browser, get_name)
    assert x.text == success_msg


@given('the amazon home page is displayed')
def amazon_home(browser):
    browser.get(amazon)

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    xpath = '//*[@id="twotabsearchtextbox"]'
    # Baseclass.set_text(browser,xpath,value=phrase + Keys.RETURN)
    search_input = browser.find_element_by_xpath(xpath)
    search_input.send_keys(phrase + Keys.RETURN)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    x = '//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[3]'
    search_input = browser.find_element_by_xpath(x)
    x = search_input.text
    assert x[1:-1] == phrase
