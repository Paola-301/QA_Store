import time
import pytest
from playwright.sync_api import Page, expect, sync_playwright
from my_functions.functions import Functions_Store

# pytest -v test_store/test_registration.py

timeout = 50

# Tet Case Nro1
# login link redirection ->Verify that the login link redirects to the registration page.
@pytest.mark.skip(reason="no hay forma de probar esto actualmente")   
def test_login_link_redirection(sep_up):
    
    '''
        Test No. 1: Login link redirection.
    '''
    
    page, navigate_to= sep_up
    functions = Functions_Store(page)
    
    try:
        navigate_to ("https://ecommerce-playground.lambdatest.io/")
        expect(page).to_have_title("Your Store")
        page.wait_for_load_state('networkidle') 
        #page.wait_for_timeout(10) 
        expect(page.locator("(//span[contains(.,'My account')])[2]")).to_be_visible(timeout=5000)

        # Hacer clic en "My account" y luego en "Register"
        functions.click("(//span[contains(.,'My account')])[2]", timeout=5000)
        functions.click("(//a[contains(.,'Register')])[2]", timeout=5000)
        print("Start Registration")
        
        message = page.locator("//h1[@class='page-title h3'][contains(.,'Register Account')]").inner_text()
        assert("Register Account") in message
        print ("Navigation to the registration page is correct") 

    except Exception as e:
        print(f"Error during test: {e}")
        assert False, f"The test failed: {e}"  
    finally:
        print("The test has finished.")
 
        
# Test Case Nro2
# Verify that the registration form is completed correctly.
#@pytest.mark.skip(reason="There is currently no way to test this")        
def test_registration_form(user_registration):

    '''
        Test No. 2: Fill out registration form.
    '''
    data = user_registration
    functions = data["functions"]
    page = data["page"]
    selectors = data["selectors"]

    functions.click(selectors["first_name"])
    functions.enter_value(selectors["first_name"],"Carlos")
    
    functions.click(selectors["last_name"])
    functions.enter_value(selectors["last_name"], "Hernandez")
    
    functions.click(selectors["email"])
    functions.enter_value(selectors["email"], "carloshernandez20241112@test.com")
    
    functions.click(selectors["telephone"])
    functions.enter_value(selectors["telephone"], "23485567")
    
    functions.click(selectors["password"])
    functions.enter_value(selectors["password"], "carlos123")
    
    functions.click(selectors["password_confirm"])
    functions.enter_value(selectors["password_confirm"], "carlos123")
    
    functions.click(selectors["subscribe"])
    
    if not functions.page.locator(selectors["privacy_policy"]).is_checked():
        functions.click("//label[contains(.,'I have read and agree to the Privacy Policy')]", timeout)
    else: 
        print ("Elemento 'I have read and agree to the Privacy Policy' no encontrado o ya marcado")

    functions.click(selectors["btn_continue"])
    
    message = page.locator("//h1[@class='page-title my-3'][contains(.,'Your Account Has Been Created!')]").inner_text()
    assert(" Your Account Has Been Created!") in message
    print ("Se realizó el registro") 


# Test Case Nro3 
# Verify that the required fields show errors if they are empty.
@pytest.mark.skip(reason="no hay forma de probar esto actualmente")      
def test_required_fields_validation(user_registration):
    
    '''
        Test No. 3: Validation of required fields.
    '''
    data = user_registration
    functions = data["functions"]
    page = data["page"]
    selectors = data["selectors"]
    
    functions.click(selectors["btn_continue"])
    
    try:
        functions.click(selectors["first_name"])
        functions.enter_value(selectors["first_name"],"")
        expected_first_name_message = page.locator("(//div[contains(@class,'text-danger')])[1]").inner_text()
        assert("First Name must be between 1 and 32 characters!") in expected_first_name_message, f"Unexpected error message for name: {expected_first_name_message}"
       
        functions.click(selectors["last_name"])
        functions.enter_value(selectors["last_name"], "")
        expected_last_name_message = page.locator("(//div[contains(@class,'text-danger')])[2]").inner_text()
        assert ("Last Name must be between 1 and 32 characters!") in expected_last_name_message, f"Unexpected error message for last name: {expected_last_name_message}"
        
        functions.click(selectors["email"])
        functions.enter_value(selectors["email"], "")
        expected_email_message = page.locator("(//div[contains(@class,'text-danger')])[3]").inner_text()
        assert ("E-Mail Address does not appear to be valid!") in expected_email_message, f"Unexpected error message for e-mail: {expected_email_message}"
        
        functions.click(selectors["telephone"])
        functions.enter_value(selectors["telephone"], "")
        expected_telephone_message = page.locator("(//div[contains(@class,'text-danger')])[4]").inner_text()
        assert ("Telephone must be between 3 and 32 characters!") in expected_telephone_message, f"Unexpected error message for telephone: {expected_telephone_message}"
        
        functions.click(selectors["password_confirm"])
        functions.enter_value(selectors["password_confirm"], "")
        expected_password_message = page.locator("(//div[contains(@class,'text-danger')])[5]").inner_text()
        assert ("Password must be between 4 and 20 characters!") in expected_password_message, f"Unexpected error message for password: {expected_password_message}"
        
    except Exception as e:
        print(f"Error durante la prueba: {e}")
        assert False, f"The test has finished: {e}"
  
  
# Test Caso Nro4
# Verify that the passwords entered match.
def test_match_password(user_registration):

    '''
        Test No. 4: Validate that the passwords match.
    '''
    data = user_registration
    functions = data["functions"]
    page = data["page"]
    selectors = data["selectors"]

    functions.click(selectors["first_name"])
    functions.enter_value(selectors["first_name"],"Carlos")
    
    functions.click(selectors["last_name"])
    functions.enter_value(selectors["last_name"], "Hernandez")
    
    functions.click(selectors["email"])
    functions.enter_value(selectors["email"], "carloshernandez202411@test.com")
    
    functions.click(selectors["telephone"])
    functions.enter_value(selectors["telephone"], "23485567")
    
    functions.click(selectors["password"])
    functions.enter_value(selectors["password"], "carlos123")
    
    functions.click(selectors["password_confirm"])
    functions.enter_value(selectors["password_confirm"], "123")
    
    functions.click(selectors["subscribe"])
    
    if not functions.page.locator(selectors["privacy_policy"]).is_checked():
        functions.click("//label[contains(.,'I have read and agree to the Privacy Policy')]", timeout)
    else: 
        print ("Element 'I have read and agree to the Privacy Policy' not found or already marked")

    
    functions.click(selectors["btn_continue"])
    expected_message = "Password confirmation does not match password!"
    error_message_locator = page.locator("//div[@class='text-danger'][contains(., 'Password confirmation does not match password!')]")
    error_message_locator.wait_for(timeout=60000)

    actual_message = error_message_locator.inner_text()
    assert expected_message in actual_message, f"Unexpected error message for password: {actual_message}"
  
    print("not match password!")
 
    
# Caso Nro 5
# Verify that a message is displayed if the privacy policy has not been accepted.
def test_Privacy_Policy_Subscription(user_registration):

    '''
        Test No. 5: Validate the notice of non-acceptance of the privacy policy.
    '''
    data = user_registration
    functions = data["functions"]
    page = data["page"]
    selectors = data["selectors"]

    functions.click(selectors["first_name"])
    functions.enter_value(selectors["first_name"],"Carlos")
    
    functions.click(selectors["last_name"])
    functions.enter_value(selectors["last_name"], "Hernandez")
    
    functions.click(selectors["email"])
    functions.enter_value(selectors["email"], "carloshernandez202411@test.com")
    
    functions.click(selectors["telephone"])
    functions.enter_value(selectors["telephone"], "23485567")
    
    functions.click(selectors["password"])
    functions.enter_value(selectors["password"], "carlos123")
    
    functions.click(selectors["password_confirm"])
    functions.enter_value(selectors["password_confirm"], "carlos123")
    
    functions.click(selectors["subscribe"])
    
    functions.click(selectors["btn_continue"])
    
    expected_message = "Warning: You must agree to the Privacy Policy!"
    error_message_locator = page.locator("//div[@class='alert alert-danger alert-dismissible'][contains(.,'Warning: You must agree to the Privacy Policy!')]")
    error_message_locator.wait_for(timeout=60000)

    actual_message = error_message_locator.inner_text()
    assert expected_message in actual_message, f"Unexpected error message for the privacy policy: {actual_message}"

