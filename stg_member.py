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

##멤버가입 선택
driver.find_element_by_xpath('/html/body/header/div/div[1]/div/div/ul/li[2]/a').click()

##이메일입력
account = driver.find_elements_by_xpath('//*[@id="emailAddress"]')[0]
account.send_keys('hwany8541@nate.com')
##패스워드입력
password = driver.find_elements_by_xpath('//*[@id="password"]')[0]
password.send_keys('890Iop!@')
##패스워드확인
confirm = driver.find_elements_by_xpath('//*[@id="confirmPassword"]')[0]
confirm.send_keys('890Iop!@')
##이름입력
username = driver.find_elements_by_xpath('//*[@id="firstName"]')[0]
username.send_keys('김명환')
##휴대폰번호입력
phone = driver.find_elements_by_xpath('//*[@id="phone"]')[0]
phone.send_keys('01051876728')
##약관동의 체크박스 클릭
driver.find_element_by_xpath('//*[@id="checkTerms"]/label/i').click()
driver.find_element_by_xpath('//*[@id="checkPrivacy"]/label/i').click()
##가입버튼 클릭
driver.find_element_by_xpath('/html/body/section/section/section/div/div/div[2]/div[3]/div[3]/div/button').click()

##쇼핑시작하기 클릭
driver.find_element_by_xpath('/html/body/section/section/div[2]/div/div[2]/div/div/a').click()
print('회원가입 완료')

##로그아웃
menu = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu')
logout = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu > div > div > ul > li:nth-child(5) > a')

try:
    action=ActionChains(driver).move_to_element(menu)##우측상단 회원정보 마우스 오버
    action.perform()
    print('마이페이지 메뉴 호출 성공')
except Exception as error:
    print('마이페이지 메뉴 호출 실패')
    
sleep(1)
try:
    action=ActionChains(driver).move_to_element(logout).click()##로그아웃 버튼 클릭
    action.perform()
    print('로그아웃 완료')
except Exception as error:
    print('로그아웃 실패')    
sleep(1)

##sitelock 해제
sitelock = driver.find_elements_by_name('password')[0]
sitelock.send_keys('nike2020')
driver.find_element_by_xpath('/html/body/div[3]/form/div/div[2]/button').click()

##가입한 계정으로 로그인
driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li:nth-child(3) > a').click()
ID = driver.find_element_by_xpath('//*[@id="j_username"]')
ID.send_keys('hwany8541@nate.com')
PW = driver.find_element_by_xpath('//*[@id="j_password"]')
PW.send_keys('890Iop!@')
driver.find_element_by_css_selector('#common-modal > div > div > div > div.body > div > div.uk-grid.login_btn_line > div > button').click()
sleep(1)

##검색
try:
    search = driver.find_element_by_css_selector('#search')
    search.send_keys("조던")
    search.submit()
except Exception as error:
    print('검색오류발생')   

sleep(1)
driver.save_screenshot('search_result.png')
print('검색완료')

##Sorting 확인
men = driver.find_element_by_css_selector('body > header > div > div.header > div > div.nk_gnb > ul > li:nth-child(2) > a')
shoes = driver.find_element_by_css_selector('body > header > div > div.header > div > div.nk_gnb > ul > li:nth-child(2) > div > div > div:nth-child(2) > ul > li > ul > li:nth-child(1) > a')

try:
    men=ActionChains(driver).move_to_element(men)
    action.perform()
except Exception as error:
    print('MEN 키테고리 호출 실패')

sleep(1)

try:
    shoes=ActionChains(driver).move_to_element(shoes).click()
    action.perform()
except Exception as error:
    print('신발전체 클릭 실패')



##마이페이지 이동
sleep(1)
menu = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu')
mypage = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu > div > div > ul > li:nth-child(1) > a')

try:
    action=ActionChains(driver).move_to_element(menu)##우측상단 회원정보 마우스 오버
    action.perform()
    print('마이페이지 메뉴 호출 성공')
except Exception as error:
    print('마이페이지 메뉴 호출 실패')

sleep(1)
try:
    action=ActionChains(driver).move_to_element(mypage).click()##마이페이지 클릭
    action.perform()
    print('마이페이지 진입')
except Exception as error:
    print('마이페이지 진입 실패')

##회원정보 수정
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-aside.mypage.pc-only > div:nth-child(6) > a:nth-child(3)').click()
sleep(1)
driver.save_screenshot('info_before.png')##수정전 회원정보 캡처
sleep(1)

##휴대폰 번호 변경
phone = driver.find_element_by_css_selector('#phoneNumber')
phone.clear() ##입력값삭제
phone.send_keys('1234567890') ##변경하려는 휴대폰 번호

##email,sms 수신동의 체크박스 클릭
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div:nth-child(1) > div > div > form > div:nth-child(10) > div > span > label > i').click()
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div:nth-child(1) > div > div > form > div:nth-child(11) > div > span > label > i').click()
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div.uk-grid.uk-margin-top > div > button').click()
driver.implicitly_wait(3)
driver.find_element_by_css_selector('body > section > section > div.uk-width-1-1.uk-margin-xlarge-top > div > div.body.width-small.uk-margin-xlarge-bottom > div > div > a').click()

sleep(1)

menu = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu')
info = driver.find_element_by_css_selector('body > header > div > div.pre_header > div > div > ul > li.dropMenu > div > div > ul > li:nth-child(2)')

action=ActionChains(driver).move_to_element(menu)##우측상단 회원정보 마우스 오버
action.perform()
sleep(1)
action=ActionChains(driver).move_to_element(info).click()##회원정보관리 클릭
action.perform()
sleep(1)
driver.save_screenshot('info_after.png')##수정후 회원정보 캡처

##회원탈퇴
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-aside.mypage.pc-only > div:nth-child(6) > a:nth-child(5)').click()
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div:nth-child(1) > div > div > form > div:nth-child(6) > div > div:nth-child(1) > label > i').click()

withdrawal=driver.find_element_by_css_selector('#reasonDetail')
withdrawal.send_keys('TEST 계정 생성 후 탈퇴')

driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div:nth-child(1) > div > div > form > div:nth-child(8) > div > span > label > i').click()
driver.find_element_by_css_selector('body > section > section > article.contents.width-xlarge > div > div.customer-contents > div > div > div.uk-grid.uk-margin-large-top > div > button').click()

driver.find_element_by_css_selector('body > div.uk-modal.uk-open > div > div > div.uk-modal-footer.uk-text-right > button.uk-button.uk-button-primary.js-modal-confirm').click()

sleep(1)
print('전체실행 종료')

#브라우저 종료
driver.quit()