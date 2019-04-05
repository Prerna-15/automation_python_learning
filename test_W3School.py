from selenium import webdriver


def test_environment(self):
    global driver

    driver = webdriver.Chrome("drivers/chromedriver")
    driver.get("https://www.w3schools.com")

    #maximize the browser
    driver.maximize_window()
    driver.implicitly_wait(3)

    # yield
    # driver.close()


# def test_w3schools(test_environment):
    driver.find_element_by_xpath("//*[@class='w3-bar-item w3-button w3-hover-white w3-padding-16 w3-right'][1]").click()
    driver.find_element_by_name("search").send_keys("angular js")

    import time
    time.sleep(3)
    driver.find_element_by_name("search").clear()

    display = driver.find_element_by_name("search").is_displayed()
    print ("the search box is displayed: " + str(display))

    s = driver.find_element_by_name("search").send_keys("css")
    driver.find_element_by_xpath("//*[@class='gsc-search-button']").click()

    lists = driver.find_elements_by_xpath("(//*[@class='gsc-webResult gsc-result'])[1]")
    print ("the length of the searches shown is : " + str(len(lists)))

    a = 0
    for l in lists:
        print ("The attribute is : " + str(l.get_attribute("innerHTML")))
        a = a + 1
        if (a >= 10):
            break

    driver.find_element_by_xpath(
        "(//*[@class='gsc-resultsbox-visible']//*[@class='gs-webResult gs-result'])[1]//*[@class='gs-title']/a").click()

    # driver.refresh()
    driver.save_screenshot("screenshot1.png")
    cookie = driver.get_cookies()
    print ("The cookie is : " + str(cookie))

if __name__ == "__main__":
    test_environment(1)
    print ("test case completed")