# 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임종료
# 5. FPS 는 30으로 고정

# [게임이미지]
# 1. 배경 : 480 * 640 - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 :     70 * 70 - enemy.png

import pygame
import random

class EnemyClass:
    def __init__(self, screen_width, number):
        self.enemy        = pygame.image.load("./pygame_basic/dung.png")
        self.enemy_name   = str(number) + " 번째 똥"
        self.enemy_size   = self.enemy.get_rect().size             # 이미지의 크기를 구해옴
        self.enemy_width  = self.enemy_size[0]                      # 가로
        self.enemy_height = self.enemy_size[1]                      # 세로
        # 캐릭터의 사이즈 만큼 - 해줘야지 표출된다. 이미지가 그려지는 기준은 왼쪽 최상단이 0,0 이 된다.
        self.enemy_x_pos  = random.randrange(1,screen_width - self.enemy_width) # x 좌표 임의로 생성
        self.enemy_y_pos  = 0#(screen_height/2) - (enemy_height/2)       # 화면 세로의 세로크기 - 캐릭터의 높이 에 위치
#########################################################################################################################
# 기본초기화 ( 반드시 해야하는것들)
pygame.init()

#화면크기 설정
screen_width    = 480  # 가로
screen_height   = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Quiz game")  # 게임이름

# FPS 설정
clock = pygame.time.Clock()
#########################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("./pygame_basic/bg.png")

# 스프라이트(캐릭터) 불러오기
character       = pygame.image.load("./pygame_basic/dog.png")
chracter_size   = character.get_rect().size             # 이미지의 크기를 구해옴
chracter_width  = chracter_size[0]                      # 가로
chracter_height = chracter_size[1]                      # 세로
# 캐릭터의 사이즈 만큼 - 해줘야지 표출된다. 이미지가 그려지는 기준은 왼쪽 최상단이 0,0 이 된다.
chracter_x_pos  = (screen_width/2) - (chracter_width/2) # 화면 가로의 절반 크기 - 캐릭터의 width/2 에 해당하는곳에 위치 : 중앙
chracter_y_pos  = screen_height - chracter_height       # 화면 세로의 세로크기 - 캐릭터의 높이 에 위치

# 이동할 좌표
to_x = 0
to_y = 0

enemy_y = 0

# 이동속도
charactre_speed = 0.6
enemy_speed = 0.3

# 적 enemy 캐릭터 생성 제한
min_enemy_val = 0
max_enemy_val = 7
enemy_arr = []

# 1초마다 응가 생성을 위해 만듬
start_ticks = pygame.time.get_ticks()        # 시작 tick 을 받아옴

# 이벤트 루프
running = True
while(running):
    dt = clock.tick(60)                 # 게임화면의 초당 프레임수 설정

    elased_time = (pygame.time.get_ticks() - start_ticks)  / 1000       # 밀리세컨(ms) 이기 때문에 100으로 나눔 > 초(s)단위로 표시

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:      # 왼쪽
                to_x -= charactre_speed
            elif event.key == pygame.K_RIGHT:   # 오른쪽
                to_x += charactre_speed

        if event.type == pygame.KEYUP:  # 키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임캐릭터 위치 정의

    # 속도 보정을 위해 dt 값을 곱해준다.
    chracter_x_pos += to_x * dt

    # 가로 경계값 처리
    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width  - chracter_width:
        chracter_x_pos = screen_width - chracter_width

    # 응가 생성
    if elased_time > 0.5: # 1초마다 한번씩 생성
    
        enemy = EnemyClass(screen_width, min_enemy_val)
        enemy_arr.append(enemy)
        
        print(f"{min_enemy_val} 번째 똥이 생성됩니다.")
        start_ticks = pygame.time.get_ticks()        # 시작 tick 초기화
        min_enemy_val += 1
    
    # 응가 경계값 처리
    if len(enemy_arr) > 0 :
        for loof_enemys in enemy_arr :
            if loof_enemys.enemy_x_pos < 0:
                loof_enemys.enemy_x_pos = 0
            elif loof_enemys.enemy_x_pos > screen_width  - loof_enemys.enemy_width:
                loof_enemys.enemy_x_pos = screen_width - loof_enemys.enemy_width

            if loof_enemys.enemy_y_pos < 0 :
                chracter_y_pos = 0
            elif loof_enemys.enemy_y_pos > screen_height:
                #loof_enemys.enemy_y_pos = screen_height
                enemy_arr.remove(loof_enemys)
                print(f"{loof_enemys.enemy_name} 번째 똥이 삭제됩니다.")
                print(enemy_arr)

    # 응가 떨어지는효과
    if len(enemy_arr) > 0 :
        enemy_y = enemy_speed
        for down_enemy in enemy_arr :
            down_enemy.enemy_y_pos += enemy_y * dt

    # 4. 충돌처리
    # 캐릭터 충돌처리
    character_rect = character.get_rect()
    character_rect.left = chracter_x_pos     # 이동하기때문에 좌표정보를 보정
    character_rect.top  = chracter_y_pos     # 이동하기때문에 좌표정보를 보정

    # 응가 개수만큼 응가의 위치를 가져온다.
    enemy_rect_arr = []
    if min_enemy_val > 0:
        for loof_enemy in enemy_arr:
            enemy_rect = loof_enemy.enemy.get_rect()
            enemy_rect.left = loof_enemy.enemy_x_pos
            enemy_rect.top  = loof_enemy.enemy_y_pos

            enemy_rect_arr.append(enemy_rect)

    # 충돌 체크
    if len(enemy_rect_arr) > 0 :
        for i in range(0, len(enemy_rect_arr)):
            if character_rect.colliderect(enemy_rect_arr[i]) :
                print("충돌 했어요")
                running = False

    # 5. 화면 그리기
    screen.blit(background, (0,0))                              # 배경그리기 : 이미지 삽입
    screen.blit(character, (chracter_x_pos , chracter_y_pos))   # 배경그리기 : 캐릭터 삽입
    
   
    for enemy in enemy_arr :       
        screen.blit(enemy.enemy, (enemy.enemy_x_pos , enemy.enemy_y_pos))            
   
    
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.

#pygame.time.delay(4000) 
pygame.quit()

