import time
import pytest
from playwright.sync_api import Page, expect, sync_playwright
from my_functions.functions import Functions_Store


# pytest -v test_store/test_login.py

timeout = 20

# Test Case Nro1
# Successful Login -> The user enters a valid and registered email address and password.
def test_successful_login(login):
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    page.wait_for_load_state('networkidle') 
    functions.click(email_selector)
    functions.enter_value(email_selector,"carloshernandez20241@test.com")
     
    functions.click(password_selector)
    functions.enter_value(password_selector,"carlos123")
    
    functions.click(btn_continue_selector)
    
    expect_selector_confirmation = page.locator("//h2[@class='card-header h5'][contains(.,'My Account')]").inner_text()
    expect_message = ("My Account")
    assert expect_message in expect_selector_confirmation , f"Unexpected error message for confirmation: {expect_message}"
    
# Test Case Nro2
# Session Login Failed- Unregistered User  ->  The user enters an email and password that are not registered in the system.
def test_session_login_failed(login):
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    page.wait_for_load_state('networkidle') 
    functions.click(email_selector)
    functions.enter_value(email_selector,"myaccount1@test.com")
     
    functions.click(password_selector)
    functions.enter_value(password_selector,"123")
    
    functions.click(btn_continue_selector)
    
    expect_selector_no_match = page.locator("//div[@class='alert alert-danger alert-dismissible'][contains(.,'Warning: No match for E-Mail Address and/or Password.')]").inner_text()
    expect_message_match = (" Warning: No match for E-Mail Address and/or Password.")
    assert expect_message_match in expect_selector_no_match, f"Unexpected error message for session login: {expect_message_match}"
    
# Test Case Nro3
# Session Login Failed - Incorrect Password - The user enters a registered email with an incorrect password.

def test_incorrect_password(login):
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    page.wait_for_load_state('networkidle') 
    functions.click(email_selector)
    functions.enter_value(email_selector,"carloshernandez20241@test.com")
     
    functions.click(password_selector)
    functions.enter_value(password_selector,"test123")
    
    functions.click(btn_continue_selector)
    
    expect_selector_warning = page.locator("//div[@class='alert alert-danger alert-dismissible'][contains(.,'Warning: No match for E-Mail Address and/or Password.')]").inner_text()
    expect_message = (" Warning: No match for E-Mail Address and/or Password.")
    assert expect_message in expect_selector_warning , f"Unexpected error message for incorrect password: {expect_message}"
    
   
# Test Case Nro 4
# Required Field Validation - Email - The user attempts to log in without entering an email address.

def test_empty_email_field(login):
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    page.wait_for_load_state('networkidle') 
    functions.click(email_selector)
    functions.enter_value(email_selector,"")
     
    functions.click(password_selector)
    functions.enter_value(password_selector,"carlos123")
    
    functions.click(btn_continue_selector)
    
    expect_selector_warning = page.locator("//div[@class='alert alert-danger alert-dismissible'][contains(.,'Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.')]").inner_text()
    expect_message = (" Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.")
    assert expect_message in expect_selector_warning , f"Unexpected error message for confirmation: {expect_message}"
  
# Test Case Nro 5
# Required Field Validation - Password -> The user attempts to log in without entering a password.
def test_empty_password_field(login):

    functions, page, email_selector, password_selector, btn_continue_selector= login
    functions = Functions_Store(page)
    
    page.wait_for_load_state('networkidle') 
    functions.click(email_selector)
    functions.enter_value(email_selector,"carloshernandez20241@test.com")
     
    functions.click(password_selector)
    functions.enter_value(password_selector,"")
    
    functions.click(btn_continue_selector)
    
    expect_selector_warning = page.locator("//div[@class='alert alert-danger alert-dismissible'][contains(.,'Warning: No match for E-Mail Address and/or Password.')]").inner_text()
    expect_message = ("Warning: No match for E-Mail Address and/or Password.")
    assert expect_message in expect_selector_warning , f"Unexpected error message for confirmation: {expect_message}"
       
# Test Case Nro 5
#def test_session_closing(registered_user):    
#    page = registered_user
    
#    functions = Functions_Store(page)
    
#    functions.click("(//span[@class='title'][contains(.,'My account')])[2]")
#    functions.combo_value("//div[@class='info'][contains(.,'Logout')]", "Logout")
    
#    expect_selector_warning = page.locator("//h1[@class='page-title my-3'][contains(.,'Account Logout')]").inner_text()
#  expect_message = ("Account Logout")
#    assert expect_message in expect_selector_warning , f"Unexpected error message for confirmation: {expect_message}"
       
# Test Case Nro 6
# log out-> User logs out successfully
def test_log_out(registered_user):    
    page = registered_user['page']
    functions = registered_user['functions']
    
    functions.scroll(0, 600)
    functions.click("(//a[contains(.,'Logout')])[2]")
    
    expect_selector_warning = page.locator("//h1[@class='page-title my-3'][contains(.,'Account Logout')]").inner_text()
    expect_message = ("Account Logout")
    assert expect_message in expect_selector_warning , f"Unexpected error message for confirmation: {expect_message}"
    
    page.wait_for_timeout(100) 
    
    
