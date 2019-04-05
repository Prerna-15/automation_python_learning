# automation_python_learning

from selenium import webdriver

driver = webdriver.Chrome("drivers/chromedriver")

driver.get('http://www.amazon.in')
driver.maximize_window()
driver.implicitly_wait(2)

# textbox and type
driver.find_element_by_id('twotabsearchtextbox').send_keys('purses')
# click on search
driver.find_element_by_class_name("nav-input").click()
# click on checkbox
kawtra = driver.find_element_by_id('p_89/KAWTRA').click()

from selenium.webdriver.support.ui import Select
s = Select(driver.find_element_by_id('s-result-sort-select'))
s.select_by_value('price-asc-rank')

x1 = "(//*[@class='a-section aok-relative s-image-tall-aspect'])[1]"
driver.find_element_by_xpath(x1).click()

#handling window
driver.switch_to_window(driver.window_handles[-1])
length = len(driver.window_handles)
print (" the number of tabs opened are:  " +str(length))
driver.find_element_by_name('submit.add-to-cart').click()
print ("product is added to cart")

driver.find_element_by_id('hlb-ptc-btn-native').click()
print ("sign in page is opened")

driver.find_element_by_name('email').send_keys("8087880310")
print ("email ID is needed which is written")

driver.find_element_by_id('continue').click()
print ("clicked on SUBMIT button")

driver.find_element_by_id('ap_password').send_keys("9881249202")
print ("the password field is entered")
driver.find_element_by_id('signInSubmit').click()

# going back to first window
driver.switch_to_window(driver.window_handles[0])
x2 = "//*[text()='KAWTRA Fashion Stylish Handbag']"

driver.find_element_by_xpath(x2).click()
print ("Now the new count of windows is: " +str(len(driver.window_handles)))


import time
time.sleep(2)
driver.switch_to_window(driver.window_handles[0])

#logging out
driver.find_element_by_xpath("//*[text()='Sign Out']").click()
driver.refresh()

