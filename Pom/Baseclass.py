#import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
 #from allure import attachment_type
#from allure_commons.types import AttachmentType




def smart_wait(driver,locator = None, wait_seconds=10,  locator_type = None):
    """Performs an explicit wait for a particular element"""
    try:
        loc = split_locator(locator)
        if locator_type == 'button':
            WebDriverWait(driver, wait_seconds).until(EC.element_to_be_clickable((By.XPATH, loc[1])))
        else:
            if(loc[0]=='ID'):
                WebDriverWait(driver, wait_seconds).until(EC.visibility_of_element_located((By.ID, loc[1])))
            else:
                WebDriverWait(driver, wait_seconds).until(EC.presence_of_element_located((By.XPATH, loc[1])))
    except Exception as e:
        print(e + 'Exception')
        return False
    return True


def click_element(driver,locator):
    "Click the button supplied"
    result_flag = False
    try:
        smart_wait(driver, locator, locator_type='button')
        get_element(driver,locator).click()
        result_flag = True
        #time.sleep(wait_time)
    except Exception as e:

        print('Exception when clicking link with path: %s' % locator)
    return result_flag

def split_locator(locator):
    "Split the locator type and locator"
    result = ()
    try:
        result = locator
        result = tuple(locator.split(',', 1))
    except Exception as e:
        print("Error while parsing locator" + e)
    return result

def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

def drag_drop(driver,source,destination):
    #xpath='/html/body/app-root/app-defect-detail/mat-sidenav-container/mat-sidenav-content/div/section/table/tbody/tr[1]'
        ActionChains(driver).drag_and_drop(source, destination).perform()



def get_element(driver, locator,type=None):
    """Return the DOM element of the path or 'None' if the element is not found """
    smart_wait(driver,locator)
    dom_element = None
    if(type=='elements'):
        try:
            locator = split_locator(locator)
            if locator[0] == 'ID':
                dom_element = driver.find_elements(By.ID, locator[1])
            elif locator[0] == 'XPATH':
                dom_element = driver.find_elements(By.XPATH, locator[1])

            elif locator[0] == 'NAME':
                dom_element = driver.find_elements(By.NAME, locator[1])

            else:
                print("No Element type")
        except Exception as e:
            print(e)
        return dom_element

    else:
        try:
            locator = split_locator(locator)
            if locator[0] == 'ID':

                dom_element = driver.find_element(By.ID, locator[1])
            elif locator[0] == 'XPATH':
                dom_element = driver.find_element(By.XPATH, locator[1])
            elif locator[0] == 'NAME':
                dom_element = driver.find_element(By.NAME, locator[1])
            else:
                print("No Element type")
        except Exception as e:
            print(str(e)+'debug')
            ("Check your locator-'%s,%s' in the conf/locators.conf file" % (locator[0], locator[1]))
        return dom_element




def get_text(driver, locator):
    "Return the text for a given path or the 'None' object if the element is not found"
    text = ''
    try:
        text = get_element(driver,locator).text
    except Exception as e:
        print(e)
        return None
    else:
        return text

def set_text(driver, locator, value, clear_flag=True):
    "Set the value of the text field"
    text_field = None
    try:
        text_field = get_element(driver,locator)
        if text_field is not None and clear_flag is True:
            try:
                text_field.clear()
            except Exception as e:
                print(str(e))
    except Exception as e:
        print("Check your locator-'%s,%s' in the conf/locators.conf file" % (locator[0], locator[1]))

    result_flag = False
    if text_field is not None:
        try:
            text_field.send_keys(value)
            result_flag = True
        except Exception as e:
            print('Could not write to text field: %s' % locator)

    return result_flag
def check_element_displayed(driver, locator):
    """This method checks if the web element is present in page or not and returns True or False accordingly"""
    result_flag = False
    try:
        if get_element(driver, locator) is not None:
            element = get_element(driver,locator[1])
            if element.is_displayed() is True:
                result_flag = True
    except Exception as e:
        print(e+locator)

    return result_flag

def take_screenshot(driver, test_name):
    screenshots_dir = "/Users/manjit/Documents/Pycharm_project/fixture_Paintshop/Screenshot"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
    time.sleep(3)
    driver.save_screenshot(screenshot_file_path)

def select_from_list(driver,filter_model_btn,filter_list_model,filter_element):
    click_element(driver, filter_model_btn)
    l = get_element(driver, filter_list_model)
    for li in l.find_elements_by_tag_name('label'):
        if li.text == filter_element:
            li.click()
            break
    click_element(driver, filter_model_btn)


def select_from_dropdown(driver):
    select = Select(driver.find_element_by_name('kategorija'))
    for index in range(len(select.options)):
        select = Select(driver.find_element_by_name('kategorija'))
        select.select_by_index(index)

