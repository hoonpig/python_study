import pyautogui
import pyperclip # 클립보드 집어넣기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("hoonpig" , interval=0.25)

#pyautogui.write("나도 코딩")
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25)

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")


# pyperclip.copy("나도 코딩")
# pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("후니 코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + q