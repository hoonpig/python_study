import pygame

pygame.init() # 초기화(반드시 필요)

#화면크기 설정
screen_width = 480  # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("hoonpig game")  # 게임이름

#배경이미지 불러오기
background = pygame.image.load("./pygame_basic/background.png")

# 이벤트 루프
running = True
while(running):
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

    screen.blit(background, (0,0))     # 배경그리기 : 이미지 삽입
    #screen.fill((0, 0, 255))            # 배경 색칠 지정 RGB 값으로 정의
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.

# pygame 종료
pygame.quit()