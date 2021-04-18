# 그림판실행 (단축기 : win + r, 입력값 : mspaint) 및 최대화
# 상단의 텍스트 기능을 이용하여 흰영역 아무곳에다가 글자입력 
# 입력글자 : 참 잘했어요
# 5초 대기후 그림판 종료
# 이떄, 저장하지않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함.

import pyautogui
import pyperclip
import os

pyautogui.hotkey("win","r")

w1 = pyautogui.getWindowsWithTitle("실행")[0]
w1.activate()
pyautogui.write("mspaint")
pyautogui.hotkey("enter")

pyautogui.sleep(1)
w2 = pyautogui.getWindowsWithTitle("제목 없음")[0]
w2.maximize()

print(w2.size)

pyautogui.sleep(1)
input_btn = pyautogui.locateOnScreen("input_text_btn.PNG")
pyautogui.moveTo(input_btn)
pyautogui.click(input_btn)
pyautogui.move(100,500)

pyautogui.click()
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl","v")


pyautogui.sleep(2)
w2.close()
pyautogui.sleep(0.5)
pyautogui.hotkey("right","enter")

#pyautogui.move(w2.width, )



 



