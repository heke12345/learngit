from selenium import webdriver
import selenium.webdriver.support.ui as ui

driver_item = webdriver.Firefox()
url = "https://movie.douban.com/"
wait = ui.WebDriverWait(driver_item, 10)
driver_item.get(url)
wait.until(lambda driver: driver.find_element_by_xpath(
    "//div[@class='fliter-wp']/div/form/div/div/label[5]"))
driver_item.find_element_by_xpath(
    "//div[@class='fliter-wp']/div/form/div/div/label[5]").click()
