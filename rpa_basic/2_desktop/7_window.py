import pyautogui

# 현재 활성화된 창 정보 가져오기
# fw = pyautogui.getActiveWindow()
# print(fw.title) # 창의 제목정보
# print(fw.size)
# print(fw.left, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든윈도우 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize() #화면 최대크기

pyautogui.sleep(1)

w.restore() # 화면원복

w.close()
