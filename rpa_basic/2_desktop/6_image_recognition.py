import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")

# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 여러개 찾는다
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i,duration=0.25)

# 하나만
#checkbox = pyautogui.locateOnScreen("checkbox.png")

# 속도개선
# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도개선 1
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region = (1565, 633, 1889 - 1565, 765-633))
# pyautogui.moveTo(trash_icon)
 
#pyautogui.mouseInfo()

#1565,633 30,30,30 #1E1E1E
#1889,765 30,30,30 #1E1E1E

# 3. 정확도조정
# pip install opencv-python 설치 필요
#run_btn = pyautogui.locateOnScreen("run_button.png", confidence = 0.9) #90 퍼센트
#pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 바로 보여지지 않는 경우
# 1. 계속기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견실패")

# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견실패")
# pyautogui.click(file_menu_notepad)
# 2. 일정시간동안 기다리기(Time out)

import time
import sys
#timeout = 10
#start = time.time() # 시작시간 설정
#file_menu_notepad = None #pyautogui.locateOnScreen("file_menu_notepad.png")
#while file_menu_notepad is None:
#    file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#    end = time.time()
#    if end - start > timeout:
#        print("시간종료")
#        sys.exit()

def find_target(img_file, timeout=30):
    start = time.time() # 시작시간 설정
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout} s] Target not Found ({img_file}) . Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)

