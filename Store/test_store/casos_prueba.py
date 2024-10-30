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


     
    
