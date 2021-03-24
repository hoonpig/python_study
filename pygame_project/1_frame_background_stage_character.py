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



# 이벤트 루프
running = True
while(running):
    dt = clock.tick(60)                 # 게임화면의 초당 프레임수 설정

    # 캐릭터가 100만큼 이동해야함 ( 일정한 속도 유지를 위해)
    # 10 fps : 1초동안 10번 동작 -> 1번에 10 만큼이동 :  10 * 10 = 100
    # 20 fps : 1초동안 20번 동작 -> 1번에  5 만큼이동 :   5 * 20 = 100 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

    # 3. 게임캐릭터 위치 정의

    # 4. 충돌처리

    # 5. 화면 그리기

    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))
    
    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.


pygame.quit()