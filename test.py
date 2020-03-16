from selenium import webdriver
import unittest
from main import app
import time as tm

# driver=webdriver.Firefox(executable_path="C:/Users/hp-pc/Desktop/geckodriver.exe")
# driver.implicitly_wait(3)
# driver.maximize_window()
#driver.get("http://127.0.0.1:5000/")
# x=driver.find_element_by_id('Home')
# x.click()
# x=driver.find_element_by_id('About')
# x.click()
# x=driver.find_element_by_id('Contact')
# x.click()
# x=driver.find_element_by_id('name')
# x.send_keys('badrishb')
# x=driver.find_element_by_id('email')
# x.send_keys('badrishb@gmail.com')
# x=driver.find_element_by_id('feedback')
# #x.send_keys('Tested navigation')
# x=driver.find_element_by_id('message')
# x.send_keys('Tested navigation')
# x=driver.find_element_by_id('sendres')
# x.click()
# x=driver.find_element_by_id('reg')
# x.click()

# x=driver.find_element_by_id('Register')
# x.click()
# x=driver.find_element_by_id('firstname')
# x.send_keys('mstakatta')
# x=driver.find_element_by_id('lastname')
# x.send_keys('roislatta')
# x=driver.find_element_by_id('email')
# x.send_keys('wotura@gmail.com')
# x=driver.find_element_by_id('password')
# x.send_keys('vinylsnotflags')
# x=driver.find_element_by_id('confirm_password')
# x.send_keys('vinylsnotflags')
# x=driver.find_element_by_id('phone')
# x.send_keys('9199667789')
# x=driver.find_element_by_id('register')
# x.click()
# x=driver.find_element_by_id('Login')
# x.click()
# x=driver.find_element_by_id('email')
# x.send_keys('wotura@gmail.com')
# x=driver.find_element_by_id('password')
# x.send_keys('vinylsnotflags')
# x=driver.find_element_by_id('remember')
# #x.clear()
# x.click()
# x=driver.find_element_by_id('submit')
# x.click()


#clx.submit()







class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_index_con(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_index_reg(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_index_log(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_index_non(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    def test_index_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertTrue(b'About' in response.data)
        self.assertTrue(b'Contact' in response.data)
        self.assertTrue(b'Register' in response.data)
        self.assertTrue(b'Login' in response.data)
    def test_login_page_contact(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')  
        self.assertTrue(b'About' in response.data)
        self.assertTrue(b'Contact' in response.data)
        self.assertTrue(b'Register' in response.data)
        self.assertTrue(b'Login' in response.data)
        self.assertTrue(b'Contact us' in response.data)
        self.assertTrue(b'Name' in response.data)
        self.assertTrue(b'Email' in response.data)
        self.assertTrue(b'Feedback' in response.data)
        self.assertTrue(b'Message' in response.data)
        self.assertTrue(b'Send me a copy of this message' in response.data)
        self.assertTrue(b'send' in response.data)
    def test_login_page_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertTrue(b'About' in response.data)
        self.assertTrue(b'Contact' in response.data)
        self.assertTrue(b'Register' in response.data)
        self.assertTrue(b'Login' in response.data)
        self.assertTrue(b'Sign Up' in response.data)
        #self.assertTrue(b'Name' in response.data)
        self.assertTrue(b'Email' in response.data)
        self.assertTrue(b'First name' in response.data)
        self.assertTrue(b'Last name' in response.data)
        self.assertTrue(b'Password' in response.data)
        self.assertTrue(b'Confirm Password' in response.data)
        self.assertTrue(b'Phone number' in response.data)
        #self.assertTrue(b'Register' in response.data)
    def test_login_page_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'About' in response.data)
        self.assertTrue(b'Contact' in response.data)
        self.assertTrue(b'Register' in response.data)
        self.assertTrue(b'Login' in response.data)
        self.assertTrue(b'Password' in response.data)
        self.assertTrue(b'Remember Me' in response.data)
        self.assertTrue(b'Email' in response.data)

class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Users/hp-pc/Desktop/geckodriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("http://127.0.0.1:5000/")
    # As per unittest module, individual test should start with test_
    def test_contact(self):
        driver = self.driver

        # time.sleep(10) 
        name='test1'
        testemail='testzz@gmail.com'
        testmsg='Tested navigation'
        x=driver.find_element_by_id('Contact')
        x.click()
        tm.sleep(1)
        x=driver.find_element_by_id('name')
        x.send_keys(name)
        x=driver.find_element_by_id('email')
        x.send_keys(testemail)
        x=driver.find_element_by_id('feedback')
        #x.send_keys('Tested navigation')
        x=driver.find_element_by_id('message')
        x.send_keys(testmsg)
        x=driver.find_element_by_id('sendres')
        x.click()
        x=driver.find_element_by_id('reg')
        x.click()
        tm.sleep(3)
        dr=driver.page_source
        x= driver.find_element_by_id("Login")
        x.click()
        tm.sleep(1)
        x=driver.find_element_by_id('email')
        x.send_keys('admin@gmail.com')
        x=driver.find_element_by_id('password')
        x.send_keys('admin')
        x=driver.find_element_by_id('remember')
        #x.clear()
        x.click()
        x=driver.find_element_by_id('submit')
        x.click()
        tm.sleep(3)
        x=driver.find_element_by_id("drop")
        x.click()
        x=driver.find_element_by_id("fdb")
        x.click()
        # search_criteria.clear()
        # search_criteria.send_keys("Lambda Test")
 
        # Check if the search returns any result
        self.assertTrue(testmsg in driver.page_source)
        self.assertTrue(name in driver.page_source)
        self.assertTrue(testemail in driver.page_source)
        self.assertTrue( "FeedBack sent successfully" in dr)
        # driver.get("http://127.0.0.1:5000/")
        # time.sleep(10) 
 

    def test_loginz(self):
        driver = self.driver
        # driver.get("http://127.0.0.1:5000/")
        # time.sleep(10) 
        ml='zezzkkz@gmail.com'
        x=driver.find_element_by_id('Register')
        x.click()
        tm.sleep(1)
        x=driver.find_element_by_id('firstname')
        x.send_keys('totezazz')
        x=driver.find_element_by_id('lastname')
        x.send_keys('hagez-coz-conizz')
        x=driver.find_element_by_id('email')
        x.send_keys(ml)
        x=driver.find_element_by_id('password')
        x.send_keys('vinylsnotflags')
        x=driver.find_element_by_id('confirm_password')
        x.send_keys('vinylsnotflags')
        x=driver.find_element_by_id('phone')
        x.send_keys('9100017619')
        x=driver.find_element_by_id('register')
        x.click()
        c=driver.page_source
        tm.sleep(3)
 
        x= driver.find_element_by_id("Login")
        x.click()
        # tm.sleep(1)
        x=driver.find_element_by_id('email')
        x.send_keys(ml)
        x=driver.find_element_by_id('password')
        x.send_keys('vinylsnotflags')
        x=driver.find_element_by_id('remember')
        #x.clear()
        x.click()
        x=driver.find_element_by_id('submit')
        x.click()
        tm.sleep(3)
        # search_criteria.clear()
        # search_criteria.send_keys("Lambda Test")
 
        # Check if the search returns any result
        self.assertTrue("Login success" in driver.page_source)
        self.assertTrue( "User Registered Successfully" in c)

 
        # search_criteria.submit()
        # time.sleep(10)
    def test_addsch(self):
        driver = self.driver
        # driver.get("http://127.0.0.1:5000/")
        # time.sleep(10) 

        date="91/4/2020"
        ml="aswin@gmail.com"
        exid="m2"
        time="12:30"
        slot="2"

        x= driver.find_element_by_id("Login")
        x.click()
        tm.sleep(1)
        x=driver.find_element_by_id('email')
        x.send_keys('admin@gmail.com')
        x=driver.find_element_by_id('password')
        x.send_keys('admin')
        x=driver.find_element_by_id('remember')
        #x.clear()
        x.click()
        x=driver.find_element_by_id('submit')
        x.click()
        tm.sleep(3)
        x=driver.find_element_by_id("drop")
        x.click()
        x=driver.find_element_by_id("adds")
        x.click()
        x=driver.find_element_by_id("email")
        x.send_keys(ml)
        x=driver.find_element_by_id("examid")
        x.send_keys(exid)
        x=driver.find_element_by_id("date")
        x.send_keys(date)
        x=driver.find_element_by_id("time")
        x.send_keys(time)
        x=driver.find_element_by_id("slot")
        x.send_keys(slot)
        x=driver.find_element_by_id("submit")
        x.click()
        c=driver.page_source
        tm.sleep(3)
        x=driver.find_element_by_id("logout")
        x.click()
        x=driver.find_element_by_id('email')
        x.send_keys(ml)
        x=driver.find_element_by_id('password')
        x.send_keys('aa')
        x=driver.find_element_by_id('remember')
        #x.clear()
        x.click()
        x=driver.find_element_by_id('submit')
        x.click()
        x=driver.find_element_by_id("ps")
        x.click()
        x=driver.find_element_by_id("vs")
        x.click()
        tm.sleep(3)
        # x=driver.find_element_by_id("submit")
        # x.click()



        # search_criteria.clear()
        # search_criteria.send_keys("Lambda Test")
 
        # Check if the search returns any result
        self.assertTrue("Schedule Added Successfully" in c)
        self.assertTrue(exid in driver.page_source)
        self.assertTrue(date in driver.page_source)
        self.assertTrue(time in driver.page_source)

    def test_viewsch(self):
            driver = self.driver
            # driver.get("http://127.0.0.1:5000/")
            # time.sleep(10) 

            date="10/4/2020"
            ml="aswin@gmail.com"
            exid="m2"
            time="9:30"
            slot="1"

            x= driver.find_element_by_id("Login")
            x.click()
            tm.sleep(1)
            x=driver.find_element_by_id('email')
            x.send_keys('admin@gmail.com')
            x=driver.find_element_by_id('password')
            x.send_keys('admin')
            x=driver.find_element_by_id('remember')
            #x.clear()
            x.click()
            x=driver.find_element_by_id('submit')
            x.click()
            tm.sleep(3)
            x=driver.find_element_by_id("drop")
            x.click()
            x=driver.find_element_by_id("adds")
            x.click()
            x=driver.find_element_by_id("email")
            x.send_keys(ml)
            x=driver.find_element_by_id("examid")
            x.send_keys(exid)
            x=driver.find_element_by_id("date")
            x.send_keys(date)
            x=driver.find_element_by_id("time")
            x.send_keys(time)
            x=driver.find_element_by_id("slot")
            x.send_keys(slot)
            x=driver.find_element_by_id("submit")
            x.click()
            c=driver.page_source
            tm.sleep(3)
            x=driver.find_element_by_id("drop")
            x.click()
            x=driver.find_element_by_id("views")
            x.click()
            tm.sleep(3)
        
            # x=driver.find_element_by_id("submit")
            # x.click()



            # search_criteria.clear()
            # search_criteria.send_keys("Lambda Test")
    
            # Check if the search returns any result
            self.assertTrue("Schedule Added Successfully" in c)
            self.assertTrue(exid in driver.page_source)
            self.assertTrue(date in driver.page_source)
            self.assertTrue(time in driver.page_source)
 
    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser. 
        tm.sleep(10)
        self.driver.close()

    # Ensure that Flask was set up correctly
    
    
    
    
if __name__ == '__main__':
    unittest.main()