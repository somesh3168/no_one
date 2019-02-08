from pywinauto import application
import pyautogui as pya
import time

app = application.Application()
vm= 'VALAR MORGHULIS'
vd='VALAR DOHAERIS'
app.start("Notepad.exe")
pya.press('enter', 3)
pya.press('tab', 3)
pya.typewrite(vm, 0.11)
time.sleep(1)
pya.press('backspace', len(vm))
pya.typewrite(vd, 0.11)
time.sleep(2)
app.Notepad.MenuSelect("File ->Exit")
time.sleep(0.23)
app.Notepad.Dontsave.click()
