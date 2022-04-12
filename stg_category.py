from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome(r'C:\python\workspace\chromedriver.exe')##크롬 호출

driver.implicitly_wait(10)

##staging site 이동
driver.get('https://stg-www-nike.brzc.kr/kr/ko_kr/')

##sitelock 해제
sitelock = driver.find_elements_by_name('password')[0]
sitelock.send_keys('nike2020')
driver.find_element_by_xpath('/html/body/div[3]/form/div/div[2]/button').click()

##로그인
driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li:nth-child(3) > a').click()
ID = driver.find_element_by_xpath('//*[@id="j_username"]')
ID.send_keys('hwany8541@gmail.com')
PW = driver.find_element_by_xpath('//*[@id="j_password"]')
PW.send_keys('890Iop!@!@')
driver.find_element_by_css_selector('#common-modal > div > div > div > div.body > div > div.uk-grid.login_btn_line > div > button').click()

sleep(2)

##MEN 신발 전체 선택
men = driver.find_element_by_css_selector('body > header > div > div.header > div > div.nk_gnb > ul > li:nth-child(2) > a')
shoes = driver.find_element_by_css_selector('body > header > div > div.header > div > div.nk_gnb > ul > li:nth-child(2) > div > div > div:nth-child(2) > ul > li > ul > li:nth-child(1) > a')

try:
    men=ActionChains(driver).move_to_element(men)
    men.perform()
except Exception as error:
    print('men error')

sleep(2)

try:
    shoes=ActionChains(driver).move_to_element(shoes).click()
    shoes.perform()
except Exception as error:
    print('shoes error')
    
sleep(2)

sort1 = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div')

try:
    sort=ActionChains(driver).move_to_element(sort1).click()
    sort.perform()
except Exception as error:
    print('sort1_error')
    
sleep(2)

low_Price = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div > ul > li:nth-child(3) > a')
high_Price = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div > a > span')
new_Prod = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div > ul > li:nth-child(1) > a > span')

try:
    low_Price=ActionChains(driver).move_to_element(low_Price).click()
    low_Price.perform()
    sleep(2)
    driver.save_screenshot('low_Price.png')
except Exception as error:
    print('low Price error')
    
sleep(2)

sort2 = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div > a')

try:
    sort=ActionChains(driver).move_to_element(sort2).click()
    sort.perform()
except Exception as error:
    print('sort2_error')

try:
    high_Price=ActionChains(driver).move_to_element(high_Price).click()
    high_Price.perform()
    sleep(2)
    driver.save_screenshot('high_Price.png')
except Exception as error:
    print('high_Price error')
    
sleep(3)

sort3 = driver.find_element_by_css_selector('body > section > section > section > div > div.section-control > div > a')

try:
    sort=ActionChains(driver).move_to_element(sort3).click()
    sort.perform()
except Exception as error:
    print('sort3_error')

try:
    new_Prod=ActionChains(driver).move_to_element(new_Prod).click()
    new_Prod.perform()
    sleep(2)
    driver.save_screenshot('new_Prod.png')
except Exception as error:
    print('new_Prod error')
    
sleep(5)

print('전체실행 종료')

#브라우저 종료
driver.quit()