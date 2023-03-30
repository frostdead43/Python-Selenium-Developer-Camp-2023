from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest


class Test_DemoTest:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()
        
    def test_demo_Test1(self):
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("12321321")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        UnameError= self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+ "/test-1.png")
        testResult = UnameError.text == "Epic sadface: Username is required"

    def test_demo_Test2(self):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("asdsadsadas")
        self.waitforElementVisible((By.ID,"password"),15)
        passwordInput = self.driver.find_element(By.ID,"password")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        PasswordError = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath+ "/test-2.png")
        testResult = passwordInput.text == "Epic sadface: Password is required"

    def test_demo_Test3(self):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput =self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        self.waitforElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        lockedError = self.driver.find_element (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
        self.driver.save_screenshot(self.folderPath+ "/test-3.png")
        testResult = lockedError == "Epic sadface: Sorry, this user has been locked out."
    
    def test_demo_Test4(self):
        self.waitforElementVisible((By.ID,"user-name"))
        self.waitforElementVisible((By.ID,"password"),10)
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        clickX = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        clickX.click()
        self.driver.save_screenshot(self.folderPath+ "/test-4.png")
    
    def test_demo_Test5(self):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        self.waitforElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        self.driver.save_screenshot(self.folderPath+ "/test-5.png")
        EnvanterSayi = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        numberOfInventory = len(EnvanterSayi)
        assert(f"Number of invertory: {numberOfInventory}")

    @pytest.mark.parametrize("username,password",[("asd","123"),("mako123","kutahya43"),("asdas2131","12312asdasda")])
    def test_demo_Test6(self,username,password):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitforElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    
    def test_demo_Test7(self):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        self.waitforElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        time.sleep(1)
        sortButton = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        sortButton.click()
        self.driver.save_screenshot(self.folderPath+ "/test-7.png")
        sorthightolow = self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]")
        sorthightolow.click()
        time.sleep(1)
    
    def test_demo_Test8(self):
        self.waitforElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        self.waitforElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginbtn = self.driver.find_element(By.ID,"login-button")
        loginbtn.click()
        addProduct = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")
        addProduct.click()
        time.sleep(1)
        cartLogo = self.driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container > a")
        cartLogo.click()
        time.sleep(1)
        checkoutbtn = self.driver.find_element(By.ID,"checkout")
        checkoutbtn.click()
        firstnameInput = self.driver.find_element(By.ID,"first-name")
        firstnameInput.send_keys("Makif")
        lastnameInput = self.driver.find_element(By.ID,"last-name")
        lastnameInput.send_keys("yilmaz")
        zipcodeInput = self.driver.find_element(By.ID,"postal-code")
        zipcodeInput.send_keys("12345")
        continuebtn= self.driver.find_element(By.ID,"continue")
        time.sleep(1)
        continuebtn.click()
        time.sleep(1)
        self.driver.save_screenshot(self.folderPath+ "/test-8.png")
        finishbtn = self.driver.find_element(By.ID,"finish")
        finishbtn.click()
        time.sleep(1)
        self.driver.save_screenshot(self.folderPath+ "/test-8-finish.png")
        homebtn = self.driver.find_element(By.ID,"back-to-products")
        homebtn.click()
        time.sleep(1)
        





                                             
        


    



        
    def waitforElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))
    


# testClass = Test_DemoTest()
# # testClass.loginSauceTest()
# testClass.test_demo_Test1()
# testClass.test_demo_Test2()
# testClass.test_demo_Test3()
# testClass.test_demo_Test4()
# testClass.test_demo_Test5()
# testClass.test_demo_Test6()



        
      
        
    

  