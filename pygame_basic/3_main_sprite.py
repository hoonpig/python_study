import pygame

pygame.init() # 초기화(반드시 필요)

#화면크기 설정
screen_width    = 480  # 가로
screen_height   = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정  
pygame.display.set_caption("hoonpig game")  # 게임이름

#배경이미지 불러오기
background      = pygame.image.load("./pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character       = pygame.image.load("./pygame_basic/character.png")
chracter_size   = character.get_rect().size             # 이미지의 크기를 구해옴
chracter_width  = chracter_size[0]                      # 가로
chracter_height = chracter_size[1]                      # 세로
# 캐릭터의 사이즈 만큼 - 해줘야지 표출된다. 이미지가 그려지는 기준은 왼쪽 최상단이 0,0 이 된다.
chracter_x_pos  = (screen_width/2) - (chracter_width/2) # 화면 가로의 절반 크기 - 캐릭터의 width/2 에 해당하는곳에 위치 : 중앙
chracter_y_pos  = screen_height - chracter_height       # 화면 세로의 세로크기 - 캐릭터의 높이 에 위치


# 이벤트 루프
running = True
while(running):
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

    screen.blit(background, (0,0))      # 배경그리기 : 이미지 삽입
    screen.blit(character, (chracter_x_pos,chracter_y_pos))      # 배경그리기 : 캐릭터 삽입
    
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.

# pygame 종료
pygame.quit()