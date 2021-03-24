import pygame

pygame.init() # 초기화(반드시 필요)

#화면크기 설정
screen_width    = 480  # 가로
screen_height   = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("hoonpig game")  # 게임이름

# FPS 설정
clock = pygame.time.Clock()

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

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
charactre_speed = 0.6

# 적 enemy 캐릭터
enemy       = pygame.image.load("./pygame_basic/enemy.png")
enemy_size   = enemy.get_rect().size             # 이미지의 크기를 구해옴
enemy_width  = enemy_size[0]                      # 가로
enemy_height = enemy_size[1]                      # 세로
# 캐릭터의 사이즈 만큼 - 해줘야지 표출된다. 이미지가 그려지는 기준은 왼쪽 최상단이 0,0 이 된다.
enemy_x_pos  = (screen_width/2) - (enemy_width/2) # 화면 가로의 절반 크기 - 캐릭터의 width/2 에 해당하는곳에 위치 : 중앙
enemy_y_pos  = (screen_height/2) - (enemy_height/2)       # 화면 세로의 세로크기 - 캐릭터의 높이 에 위치

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(60)                 # 게임화면의 초당 프레임수 설정

    # 캐릭터가 100만큼 이동해야함 ( 일정한 속도 유지를 위해)
    # 10 fps : 1초동안 10번 동작 -> 1번에 10 만큼이동 :  10 * 10 = 100
    # 20 fps : 1초동안 20번 동작 -> 1번에  5 만큼이동 :   5 * 20 = 100 

    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님
        
        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:      # 왼쪽
                to_x -= charactre_speed
            elif event.key == pygame.K_RIGHT:   # 오른쪽
                to_x += charactre_speed
            elif event.key == pygame.K_UP:      # 위
                to_y -= charactre_speed
            elif event.key == pygame.K_DOWN:    # 아래
                to_y += charactre_speed

        if event.type == pygame.KEYUP:  # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 속도 보정을 위해 dt 값을 곱해준다.
    chracter_x_pos += to_x * dt
    chracter_y_pos += to_y * dt

    # 가로 경계값 처리
    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width  - chracter_width:
        chracter_x_pos = screen_width - chracter_width
    
    #세로 경계값 처리
    if chracter_y_pos < 0:
        chracter_y_pos = 0
    elif chracter_y_pos > screen_height  - chracter_height :
        chracter_y_pos = screen_height - chracter_height


    # 충돌처리를 위한 rect 정보 update
    character_rect = character.get_rect()
    character_rect.left = chracter_x_pos     # 이동하기때문에 좌표정보를 보정
    character_rect.top  = chracter_y_pos     # 이동하기때문에 좌표정보를 보정

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top  = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False


    screen.blit(background, (0,0))                              # 배경그리기 : 이미지 삽입
    screen.blit(character, (chracter_x_pos , chracter_y_pos))   # 배경그리기 : 캐릭터 삽입
    screen.blit(enemy, (enemy_x_pos , enemy_y_pos))             # 배경그리기 : enemy 삽입
    
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.

# pygame 종료
pygame.quit()