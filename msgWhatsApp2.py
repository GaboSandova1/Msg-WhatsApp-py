
# Si quieres enviar un mensaje varias veces de forma consecutiva usa este codigo
import pywhatkit
import pyautogui
import time

numero = "+584243811068" 
mensaje = "Alo"
veces = 100  

# Abre el chat sin cerrar la pestaña después del primer envío
pywhatkit.sendwhatmsg_instantly(numero, mensaje, wait_time=7, tab_close=False)

# Espera un poco para asegurarse de que el chat se cargue
time.sleep(8)

# Envía el mensaje varias veces con pyautogui
for _ in range(veces - 1):  
    pyautogui.write(mensaje)
    pyautogui.press("enter")
    time.sleep(0.1)  
