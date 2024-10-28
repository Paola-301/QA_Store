import time
import random
from playwright.sync_api import Page, expect


class Functions_Store:
    def __init__(self, page:Page)-> None:
        self.page = page
        #self.hide_modals()
    
    #validate url 
    def validate_url(self, expect_url, timeUrl)-> None:
        expect(self.page).to_be_url(expect_url)
     
    #Validate page title  
    def validate_title_pag(self, title: str, time_Title: int)-> None:
        expect(self.page).to_have_title(title)
        self.page.wait_for_timeout(time_Title * 1000)
      
    #Control time
    def control_time(self, time_Time)-> None:
        self.page.wait_for_timeout(time_Time * 1000)
    
    #Click on the elements 
    def click(self, selector, timeout: int=500)->None:
        val_click= self.page.locator(selector)
        self.page.wait_for_selector(selector, timeout=timeout)
        expect(val_click).to_be_visible()
        expect(val_click).to_be_enabled()
        val_click.click()
        
    #Scroll the page
    def scroll(self, x: int, y: int)->None:
        self.page.mouse.wheel(x, y) 
          
    #Move the mouse to a specific position
    def mouse_xy(self, x, y, time_Mouse)->None:
        self.page.mouse.click(x,y)
        self.page.wait_for_timeout(time_Mouse * 1000)
     
    #Validar texto 
    def validate_text(self, selector: str, text: str, time_Text)-> None:
        val_Text = self.page.locator(selector)
        expect(val_Text).to_contain_text(text)
        self.page.wait_for_timeout( time_Text*1000)
     
    #Enter text
    def enter_value(self, selector: str, value: str)-> None:
        en_value = self.page.locator(selector)
        self.page.wait_for_selector(selector, timeout=6000)
        expect(en_value).to_be_visible()
        expect(en_value).to_be_enabled()
        expect(en_value).to_be_empty()
        en_value.fill(value)
        self.page.wait_for_timeout(1000)
    
    #select an item from a list
    def combo_value(self, selector, value):
        
        try:
            combo_val = self.page.locator(selector)
            combo_val.wait_for(state="attached", timeout=10000)  # Espera hasta 10 segundos a que esté adjunto
            combo_val.wait_for(state="enabled", timeout=10000)  # Espera hasta 10 segundos a que esté habilitado
            combo_val.select_option(value, force=True)
            self.page.wait_for_timeout(1000)
            combo_val.click()

        except Exception as e:
            print(f"Error al intentar seleccionar el valor '{value}' en el combo: {e}")
            
            
     
    def value_random(self, num_list: list, num: int)-> list:
        if num > len(num_list):
            raise ValueError("Requested more elements than available in num_list.")
        return random.sample(num_list, num)
