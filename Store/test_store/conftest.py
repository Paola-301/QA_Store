import os
import json
import pytest
from playwright.sync_api import sync_playwright, expect
from my_functions.functions import Functions_Store

#url = "https://ecommerce-playground.lambdatest.io/"

@pytest.fixture(scope="session")
def playwright():
    """Fixture para inicializar Playwright para pruebas."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    """Fixture para inicializar un navegador Chromium para pruebas."""
    browser = playwright.chromium.launch(headless= False, slow_mo=2)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def sep_up(browser):
    
    """Fixture para configurar el contexto del navegador y la página."""
    context = browser.new_context(
        viewport={
            'width': 1350,
            'height': 1506
        }
    )
    page = context.new_page()
    
    def navigate_to(url):
        page.goto(url)
        page.wait_for_timeout(10) 
        #page.wait_for_load_state('networkidle') 
        #expect(page).to_have_title("A place to practice your automation skills!")
        return page
    
    yield page, navigate_to
    
    # Cierre de la página y contexto
    print("Cerrando la página y el contexto...")
    page.close()
    context.close()

@pytest.fixture(scope="function") 
def user_registration(sep_up):
  
    '''
        """Fixture para navegar a la página de registro y devolver los elementos necesarios para el registro."""
    '''
    page, navigate_to= sep_up
    functions = Functions_Store(page)
    
    try:
        navigate_to("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        page.wait_for_timeout(10) 
    except Exception as e:
        print(f"Navigation error", e)
     
    with open('json/selectors_user_registration.json') as f:
        selectors = json.load(f)
    
    
    return {
        "functions": functions,
        "page": page,
        "selectors": selectors
    }

@pytest.fixture(scope="function") 
def login(sep_up):
    
    page, navigate_to= sep_up
    functions = Functions_Store(page)
    navigate_to("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    page.wait_for_timeout(10) 
    
    email_selector = "//input[contains(@name,'email')]"
    password_selector = "//input[contains(@type,'password')]"
    btn_continue_selector = "//input[contains(@type,'submit')]"
    

@pytest.fixture(scope="function") 
def registered_user(sep_up):
    
    '''Fixture to navigate to the registration page and return the items required 
    for registration'''
    
    page, navigate_to= sep_up
    functions = Functions_Store(page)
    
    try:
        navigate_to("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
        page.wait_for_timeout(10) 
    except Exception as e:
        print(f"Navigation error", e)
        
    with open('json/selectors_registered_user.json') as f:
        selectors = json.load(f)
    
    functions.click(selectors["email_selector"])
    functions.enter_value(selectors["email_selector"], "carloshernandez20241@test.com")
     
    functions.click(selectors["password_selector"])
    functions.enter_value(selectors["password_selector"], "carlos123")
    
    functions.click(selectors["btn_continue_selector"])
    
    page.wait_for_load_state('networkidle')
    
    return {
        "page": page,
        "functions": functions,
    }
