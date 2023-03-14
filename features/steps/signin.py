import time

from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'The browser is opened and the website is loaded')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://unacademy.com/")


@when(u'The Login button on the website is clicked')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Log in']").click()
    time.sleep(2)


@when(u'Create your account is selected in the Login menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h6[@class='css-nmgvwj-H6-StyledH6 e1l7v5xe2']").click()
    time.sleep(2)


@when(u'The country dropdown gets clicked')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@role='presentation']//div[1]//div[1]//img[1]").click()
    time.sleep(2)


@when(u'India with the appropriate mobile extension is selected')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//span[contains(@class,'css-1szx4e-Label e10ouzx63')]").click()
    time.sleep(2)


@then(u'The invalid mobile number sequence is entered')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('1122334456')


@then(u'The Continue button is clicked')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[contains(@aria-label,'Continue')]").click()
    time.sleep(2)


@then(u'It should stay in the same page with a warning prompt')
def step_impl(context):
    if context.assertion_comparison_otp_page.__eq__("Verify your mobile number"):
        return False
    else:
        return True


@then(u'The invalid mobile number sequence is entered  (0000000000)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('0000000000')


@then(u'It should stay in the same page with a warning prompt2')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//p[@class='css-5piwwz-StyledP2 ena7kom0']").is_displayed()


@then(u'The invalid mobile number sequence is entered  (nodata)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('')


@then(u'It should stay in the same page with a warning prompt3')
def step_impl(context):
    context.driver.find_element(By.XPATH,'//*[@id="DrawerPaper"]/div[2]/h2').text.__eq__("Join Unacademy")


@then(u'The invalid mobile number sequence is entered  (1)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('1')


@then(u'The invalid mobile number sequence is entered  (11111aaaaa)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('11111aaaaa')


@then(u'The invalid mobile number sequence is entered  (aaa!!!@@@b)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('aaa!!!@@@b')


@then(u'The invalid mobile number sequence is entered  (111!!!@@@2)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('111!!!@@@2')


@then(u'A valid mobile number sequence is entered (9600415148)')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@aria-invalid='false']").send_keys('9600415148')


@then(u'It proceeds to the OTP page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h2[@class='css-18xjf2j-H2-Header e52pvpx0']").text.__eq__("Verify your mobile number")


@then(u'It proceeds to the OTP page & invalid OTP sequence is entered (nodata)')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('')


@then(u'The Submit button is clicked')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/div[2]/button').click()
    time.sleep(2)


@then(u'It stays in the OTP page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h2[@class='css-18xjf2j-H2-Header e52pvpx0']").text.__eq__("Verify your mobile number")


@then(u'It proceeds to the OTP page & invalid OTP sequence is entered (111111)')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('111111')


@then(u'It should stay in the same page with a warning prompt4')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//p[@class='css-5piwwz-StyledP2 ena7kom0']").text.__eq__("This OTP is not valid")


@then(u'It proceeds to the OTP page & invalid OTP sequence is entered (1)')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="DrawerPaper"]/div[2]/form/div/input').send_keys('1')


@then(u'It proceeds to the OTP page & valid OTP sequence is entered')
def step_impl(context):
    time.sleep(20)


@then(u'The account gets logged in')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Crack your goal with India’s top educators']").is_displayed()




