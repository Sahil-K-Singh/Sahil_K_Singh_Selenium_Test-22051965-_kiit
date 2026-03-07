from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Question 1
'''driver.get("https://www.amazon.in/")
sleep(4)
a = driver.find_elements("class name", "nav-sprite")
for item in a:
    print(item.text)'''

#Question 2
'''
driver.get("https://www.imdb.com/chart/top/")
driver.maximize_window()
sleep(3)

movies = driver.find_elements(By.XPATH, "//h3[@class='ipc-title__text']")

for i in range(1,11):
    print(movies[i].text)'''


#Question 3
'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_elements("tag name", "img")
print(len(a))'''


# Question 4

'''driver.get("https://demoqa.com/select-menu")
driver.find_element(By.ID, "withOptGroup").click()
sleep(2)
driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()'''

#Question 5

'''driver.get("https://www.amazon.in/")
sleep(4)
links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.get_attribute("href"))'''

#question 6

'''driver.get("https://www.google.com")
search = driver.find_element(By.NAME,"q")
search.send_keys("laptop")
sleep(3)
suggestions = driver.find_elements(By.XPATH,"//li[@role='presentation']")
for s in suggestions:
    print(s.text)'''


# Question 7
'''
driver.get("https://www.amazon.in/")
sleep(5)
account = driver.find_element(By.ID,"nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(account).perform()
sleep(3)
wishlist = driver.find_element(By.LINK_TEXT,"Your Wish List")
wishlist.click()'''

#Question 8

'''driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
sleep(3)
driver.switch_to.frame("iframeResult")
frame = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(frame)
heading = driver.find_element(By.TAG_NAME,"h1")
print(heading.text)'''

# Question 9

'''driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_element("id", "twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
a = driver.find_elements("xpath", "//h2//span")
for i in a:
    print(i.text)'''

