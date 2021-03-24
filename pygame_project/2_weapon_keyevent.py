import pygame
import os
#########################################################################################################################
# 기본초기화 ( 반드시 해야하는것들)
pygame.init()

#화면크기 설정
screen_width    = 640   # 가로
screen_height   = 480   # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("pang game")  # 게임이름

# FPS 설정
clock = pygame.time.Clock()
#########################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path    = os.path.dirname(__file__)             # 현재 파일의 위치 반환
image_path      = os.path.join(current_path, "images")  # images 폴더 위치 반환

#배경
background      = pygame.image.load(os.path.join(image_path, "background.png"))

#스태이지 정보
stage           = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size      = stage.get_rect().size
stage_height    = stage_size[1]

#캐릭터 만들기
character       = pygame.image.load(os.path.join(image_path, "character.png"))
character_size  = character.get_rect().size
character_width = character_size[0]
character_height= character_size[1]
character_x_pos = (screen_width/2)- (character_width/2)
character_y_pos = screen_height - character_height- stage_height
character_to_x  = 0
character_speed = 5

# 무기만들기
weapon          = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size     = weapon.get_rect().size
weapon_width    = weapon_size[0]

#무기는 한번에 여러발 발사가능
weapons = []

#무기이동속도
weapon_speed = 10


# 이벤트 루프
running = True
while(running):
    dt = clock.tick(60)                 # 게임화면의 초당 프레임수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 무기 위치를 위로
    # x : 100, y:200 -> y값만 변경되어야 무기 위치가 변한다.
    # 180, 160, 140, ...
    weapons = [[w[0],w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]]  for w in weapons if w[1] > 0]

    # 4. 충돌처리

    # 5. 화면 그리기

    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.


pygame.quit()