import pyautogui

#pyautogui.mouseInfo()
#pyautogui.FAILSAFE =False # 비추천
pyautogui.PAUSE = 1 # 모든동작에 1초 sleep 적용
for i in range(10):
    pyautogui.move(100,100)
    #pyautogui.sleep(1)