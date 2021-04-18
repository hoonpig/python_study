import pyautogui

#img=pyautogui.screenshot() # 스크린샷
#img.save("screenshor.png") # 파일로 저장


#pyautogui.mouseInfo()
#24,16 54,166,242 #36A6F2

pixel = pyautogui.pixel(24,16)
print(pixel)

print(pyautogui.pixelMatchesColor(24,16, (54,166,242)))
print(pyautogui.pixelMatchesColor(24,16, pixel))