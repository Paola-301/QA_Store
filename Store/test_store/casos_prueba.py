'''
REGISTRO DE USUARIO 

Casos de Prueba para Registro de Nuevo Usuario
Caso de Prueba 1: Registro Exitoso

Objetivo: Verificar que un usuario puede registrarse correctamente.
Pasos:
Navegar a la página de registro.
Completar todos los campos obligatorios con datos válidos.
Enviar el formulario.
Resultado Esperado: Mensaje de confirmación de registro exitoso y el usuario está logueado.

Caso de Prueba 2: Campo de Correo Electrónico Obligatorio
Objetivo: Verificar que no se puede registrar sin un correo electrónico.
Pasos:
Navegar a la página de registro.
Dejar el campo de correo electrónico vacío.
Completar otros campos obligatorios.
Enviar el formulario.
Resultado Esperado: Mensaje de error indicando que el correo electrónico es obligatorio.
Caso de Prueba 3: Correo Electrónico Ya Registrado

Objetivo: Verificar que no se puede registrar con un correo electrónico ya existente.
Pasos:
Navegar a la página de registro.
Ingresar un correo electrónico que ya esté registrado.
Completar otros campos obligatorios.
Enviar el formulario.
Resultado Esperado: Mensaje de error indicando que el correo electrónico ya está en uso.
Caso de Prueba 4: Contraseña No Coincide

Objetivo: Verificar que el registro falla si las contraseñas no coinciden.
Pasos:
Navegar a la página de registro.
Ingresar una contraseña en el campo de contraseña.
Ingresar una contraseña diferente en el campo de confirmación de contraseña.
Completar otros campos obligatorios.
Enviar el formulario.
Resultado Esperado: Mensaje de error indicando que las contraseñas no coinciden.
Caso de Prueba 5: Campos Obligatorios Vacíos

Objetivo: Verificar que no se puede enviar el formulario si hay campos obligatorios vacíos.
Pasos:
Navegar a la página de registro.
Dejar uno o más campos obligatorios vacíos.
Enviar el formulario.
Resultado Esperado: Mensajes de error para cada campo obligatorio vacío.
Caso de Prueba 6: Validación de Formato de Correo Electrónico

Objetivo: Verificar que el sistema valida el formato del correo electrónico.
Pasos:
Navegar a la página de registro.
Ingresar un formato de correo electrónico inválido (ej. "correo@.com").
Completar otros campos obligatorios.
Enviar el formulario.
Resultado Esperado: Mensaje de error indicando que el formato del correo electrónico es inválido.
Resumen
'''

'''
ESCENARIOS DE INICIO DE SESIÓN

Casos de Pruebas
Caso de Prueba 1: Inicio de Sesión Exitoso
Descripción: El usuario ingresa un email y una contraseña válidos y registrados.
Pasos:
Navegar a la página de inicio de sesión.
Introducir un email y contraseña válidos.
Hacer clic en el botón "Login" (Iniciar Sesión).
Resultados Esperados: El usuario debería iniciar sesión correctamente y ser redirigido a la página principal de su cuenta.
Caso de Prueba 2: Inicio de Sesión Fallido - Usuario no Registrado
Descripción: El usuario ingresa un email y contraseña que no están registrados en el sistema.
Pasos:
Navegar a la página de inicio de sesión.
Introducir un email y contraseña que no existen en el sistema.
Hacer clic en el botón "Login".
Resultados Esperados: Debería aparecer un mensaje de error indicando que el usuario o la contraseña son incorrectos.
Caso de Prueba 3: Inicio de Sesión Fallido - Contraseña Incorrecta
Descripción: El usuario ingresa un email registrado con una contraseña incorrecta.
Pasos:
Navegar a la página de inicio de sesión.
Introducir un email registrado y una contraseña incorrecta.
Hacer clic en "Login".
Resultados Esperados: Debería aparecer un mensaje de error que informe de credenciales incorrectas.
Caso de Prueba 4: Validación de Campo Obligatorio - Email
Descripción: El usuario intenta iniciar sesión sin ingresar un email.
Pasos:
Navegar a la página de inicio de sesión.
Dejar el campo de email vacío y proporcionar una contraseña válida.
Hacer clic en "Login".
Resultados Esperados: Debería aparecer un mensaje de error indicando que el campo de email es obligatorio.
Caso de Prueba 5: Validación de Campo Obligatorio - Contraseña
Descripción: El usuario intenta iniciar sesión sin ingresar una contraseña.
Pasos:
Navegar a la página de inicio de sesión.
Ingresar un email válido pero dejar vacío el campo de contraseña.
Hacer clic en "Login".
Resultados Esperados: Debería aparecer un mensaje de error indicando que el campo de contraseña es obligatorio.
Caso de Prueba 6: Cierre de Sesión
Descripción: El usuario intenta cerrar sesión después de haber iniciado sesión correctamente.
Pasos:
Iniciar sesión con email y contraseña válidos.
Navegar a la opción de cerrar sesión (Logout).
Resultados Esperados: El usuario debería ser redirigido a la página de inicio de sesión y no debería tener acceso a la cuenta sin volver a iniciar sesión.


'''




'''
    try:
        elements_state = functions.page.locator(country)
        count_state = elements_state.count()
        for r in range(count_state):
            state_text = elements_state.nth(r).inner_text().strip()  
            if state_text == "Afghanistan":
                functions.click(elements_state.nth(r), timeout=10)
                print("state", state_text)
                break
        else:
            print("No se encontró elemento")
        functions.control_time(20) 
    except Exception as e:
        print(f"Error al intentar hacer clic en {state_text}: {e}")  
    elements_country = functions.page.locator(country)
    count_country = elements_country.count()
    for c in count_country:
        try:
            functions.click("//option[@value='1'][contains(.,'Afghanistan')]")
            print("Country", c)
            break
        except Exception as e:
            print(f"No se pudo seleccionar {c}: {e}")
    else: 
        print("Elmento no encontrado ")
    
    functions.click(region_state, timeout= 1000)
    for r in region_state:
        if r:
            functions.click("//option[@value='1'][contains(.,'Badakhshan')]")
            print("state", r)
            break
    else:
        print("Elmento no encontrado ")
    
    try:
        elements_state = functions.page.locator(region_state)
        count_state = elements_state.count()
    
        for r in range(count_state):
            state_text = elements_state.nth(r).inner_text().strip()  
            if state_text == "Kara":
                functions.click(elements_state.nth(r), timeout=10) 
                print("state", state_text)
                break
        else:
            print("No se encontró elemento")
        functions.control_time(20) 
    except Exception as e:
        print(f"Error al intentar hacer clic en {state_text}: {e}")   
        
        
    
    try:
        # Esperar a que las opciones sean visibles (ajusta según sea necesario)
        functions.control_time(1)  # Puede ajustar el tiempo de espera

    # Obtener las opciones de la lista
        elements_state = functions.page.locator("//select[contains(@id,'AccountFrm_zone_id')]/option")
        count_state = elements_state.count()

        if count_state > 0:
        # Si hay opciones disponibles, buscar "Uruguay"
            functions.click("//option[@value='225'][contains(.,'Uruguay')]", timeout=10)
            print("Opción seleccionada: Uruguay")
        else:
            print("No hay opciones disponibles en la lista.")

    except Exception as e:
        print(f"Error al intentar seleccionar la opción: {e}")
    try:
        # Obtener las opciones del selector de país
        country_options = functions.page.locator("//select[@name='country_id']/option")
        count_countries = country_options.count()

    # Esperar a que las opciones sean visibles
        if count_countries == 0:
            print("No hay opciones disponibles en el selector de país.")
        else:
            print("Opciones de país disponibles:")
            for r in range(count_countries):
                country_text = country_options.nth(r).inner_text().strip() 
                print(country_text)  

                if country_text == "Colombia": 
                    functions.click("//option[@value='47'][contains(.,'Colombia')]")
                    print("Opción seleccionada: Colombia")
                    break
            else:
                print("Opción 'Colombia' no encontrada en la lista.")

    except Exception as e:
        print(f"Error al intentar seleccionar el país: {e}")
    
    
    try:
    # Hacer clic en el selector de región y esperar a que se despliegue
        functions.click(country, timeout=1000)
        page.wait_for_timeout(1000)

    # Intentar hacer clic directamente en la opción "Colombia"
        if functions.page.locator("//option[@value='222'][contains(.,'United Kingdom')]").is_visible():
            functions.click("//option[@value='222'][contains(.,'United Kingdom')]", timeout=3000)
            print("Opción seleccionada: United Kingdom")
        else:
            print("La opción 'United Kingdom' no está visible.")
    except Exception as e:
        print(f"Error al intentar seleccionar la región: {e}")
    
    try:
    # Hacer clic en el selector de región y esperar a que se despliegue
        functions.click(region_state, timeout=1000)
        page.wait_for_timeout(1000)

    # Intentar hacer clic directamente en la opción "Colombia"
        if functions.page.locator("//option[@value='3513'][contains(.,'Aberdeen')]").is_visible():
            functions.click("//option[@value='3513'][contains(.,'Aberdeen')]", timeout=3000)
            print("Opción seleccionada: Aberdeen")
        else:
            print("La opción 'Aberdeen' no está visible.")
    except Exception as e:
        print(f"Error al intentar seleccionar la región: {e}")
        
    try:
        functions.click(country, timeout=1000)
        page.wait_for_timeout(1000)
        
        if functions.page.locator("//select[@name='country_id'][contains(@id,'id')]").is_visible():
            functions.click("//select[@name='country_id'][contains(@id,'id')]", timeout=3000)
            functions.combo_value("//option[@value='90'][contains(.,'Guinea')]","Guinea")
            print("Opción seleccionada no es visible")
        else:
            print("La opción no está visibles.")
    except Exception as e:
        print(f"Error al intentar seleccionar la región: {e}")    
        
    check = functions.page.locator("//label[contains(.,'Register Account')]")
        if not check.is_checked():
            functions.click("//label[contains(.,'Register Account')]", timeout)
        else: 
            print ("Elemento 'Register Account' no encontrado o ya marcado")

        functions.scroll(0, 800)
        functions.click("//button[contains(.,'Continue')]", timeout)
        expect(page).to_have_title("Create Account")

    except Exception as e:
        print(f"Error durante la prueba: {e}")
        assert False, f"La prueba falló: {e}"  
    finally:
        print("La prueba ha terminado.")
    
    
    
    try:
        page.wait_for_selector("//select[@name='country_id'][contains(@id,'id')]", timeout=20000)
        functions.click("//select[@name='country_id'][contains(@id,'id')]")
        functions.combo_value("//select[@name='country_id'][contains(@id,'id')]", "220")  # Valor correspondiente a 'Ukraine'
    
        print("Opción 'Tonga' seleccionada")

    except Exception as e:
        print(f"Error al intentar seleccionar la región: {e}")
    
    try:
        page.wait_for_selector("//select[@name='zone_id'][contains(@id,'id')]", timeout=20000)
        functions.click("//select[@name='zone_id'][contains(@id,'id')]")
        functions.combo_value("//select[@name='zone_id'][contains(@id,'id')]", "3274")  # Valor correspondiente a 'Tonga'
        print("Opción 'Tongatapu' seleccionada")

    except Exception as e:
        print(f"Error al intentar seleccionar la región: {e}")
    
     
    functions.control_time(20) 

    functions.scroll(0,900)
    functions.click(login_Name)
    functions.enter_value(login_Name, "Demo-3")
    
    functions.click(password)
    functions.enter_value(password, "pass123")
    
    functions.click(pass_confirm)
    functions.enter_value(pass_confirm, "pass123")
    
    if not functions.page.locator(Subcribe).is_checked():
        functions.click("//input[contains(@id,'newsletter0')][@type='radio']", timeout)
    else: 
        print ("Elemento 'Sucribirse' no encontrado o ya marcado")

    if not functions.page.locator(privacy_policy).is_checked():
        functions.click("//input[@type='checkbox'][contains(@id,'agree')]", timeout)
    else: 
        print ("Elemento 'I have read and agree to the Privacy Policy' no encontrado o ya marcado")

    functions.click(btn_continue)
    
    message = page.locator("//span[@class='maintext'][contains(.,'Your Account Has Been Created!')]").inner_text()
    assert(" Your Account Has Been Created!") in message
    print ("Se realizó el registro") 
       
    '''
     
    