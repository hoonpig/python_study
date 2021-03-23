import pygame

pygame.init() # 초기화(반드시 필요)

#화면크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("hoonpig game")  # 게임이름

# 이벤트 루프
running = True
while(running):
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

# pygame 종료
pygame.quit()