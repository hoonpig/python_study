# 모든 공을 없애면 게임종료(성공)
# 캐릭터는 공에 닿으면 게임종료
# 시간제한 99초 초과시 게임종료

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
character_to_x_LEFT = 0
character_to_x_RIGHT= 0
character_speed = 5

# 무기만들기
weapon          = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size     = weapon.get_rect().size
weapon_width    = weapon_size[0]

# 무기는 한번에 여러발 발사가능
weapons = []

# 무기이동속도
weapon_speed = 10

# 공만들기(4개 크기에 대해서 따로정리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

# 공들
balls = []

# 최초 발생하는 큰공 추가
balls.append({
    "pos_x"     : 50,
    "pos_y"     : 50,
    "img_idx"   : 0,
    "to_x"      : 3,
    "to_y"      : -6,
    "init_spd_y": ball_speed_y[0]
})

# 사라질 무기와 공 정보 저장변수
weapon_to_remove    = -1
ball_to_remove      = -1


# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_tick = pygame.time.get_ticks()

# 게임종료 메세지
# TimeOut           (시간 초과 실패)
# Mission Complete  (성공)
# Game Over         (캐릭터 공에 맞음, 실패)
game_result = "Game Over"


# 이벤트 루프
running = True
while(running):
    dt = clock.tick(30)                 # 게임화면의 초당 프레임수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 파이게임을 쓰기위해 무조건 사용하는구문. 사용자의 입력을 대기하고 있는중. 이벤트 발생여부 체크
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는지 체크
            running = False             # 게임진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: # 이 부분은 모두 다 바뀜
                character_to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0

    # 3. 게임캐릭터 위치 정의
    character_x_pos += character_to_x_LEFT + character_to_x_RIGHT

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

    # 공 위치조정
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x      = ball_val["pos_x"]
        ball_pos_y      = ball_val["pos_y"]
        ball_img_idx    = ball_val["img_idx"]

        ball_size   = ball_images[ball_img_idx].get_rect().size
        ball_width  = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을때 공 이동위치 변경 (튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"]* -1     # 반대방향으로 움직이기
        
        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"]    = ball_val["init_spd_y"]
        else: # 그외에는 속도를 줄여나가고, 다시 증가한다.포물선 곡선 처리를 위함
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌처리
    
    # 캐릭터 rect 정보 업데이트
    character_rect      = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top  = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x      = ball_val["pos_x"]
        ball_pos_y      = ball_val["pos_y"]
        ball_img_idx    = ball_val["img_idx"]

        # 공 rect 정보 업데이트
        ball_rect       = ball_images[ball_img_idx].get_rect()
        ball_rect.left  = ball_pos_x
        ball_rect.top   = ball_pos_y

        # 공과 캐릭터 충돌처리
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x    = weapon_val[0]
            weapon_pos_y    = weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect     = weapon.get_rect()
            weapon_rect.left= weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove    = weapon_idx    # 해당 무기를 없애기위한 값 설정
                ball_to_remove      = ball_idx      # 해당 공 없애기위한 값 설정

                # 가장 작은공이 아니면 다음단계의 공으로 나눠준다.
                if ball_img_idx < 3:
                    # 현재 공 크기 정보를 가져온다.
                    ball_width   = ball_rect.size[0]
                    ball_height  = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect     = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width    = small_ball_rect.size[0]
                    small_ball_height   = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨져 나가는 작은공
                    balls.append({
                        "pos_x"     : ball_pos_x + (ball_width / 2)  - (small_ball_width / 2),
                        "pos_y"     : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx"   : ball_img_idx + 1,
                        "to_x"      : -3, # 음수면 왼쪽, 양수면 오른쪽
                        "to_y"      : -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]
                    })
                    # 오른쪽으로 튕겨져 나가는 작은공
                    balls.append({
                        "pos_x"     : ball_pos_x + (ball_width/2) - (small_ball_width / 2),
                        "pos_y"     : ball_pos_y + (ball_height/2) - (small_ball_height / 2),
                        "img_idx"   : ball_img_idx + 1,
                        "to_x"      : 3, # 음수면 왼쪽, 양수면 오른쪽
                        "to_y"      : -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]
                    })
                
                break 
        else : # 계속 게임을 진행
            continue # 안쪽 for 문에서 조건이 맞지않으면 continue , 바깥쪽 for 문수행
        break # 안쪽 for 문에서 break 를 만나면 여기로 진입 및 최초 for 문 중지

    # 충돌된 공, 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든공을 없앤경우 게임종료
    if len(balls) == 0 :
        game_result = "Mission Complete"
        running = False

    # 5. 화면 그리기

    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"] 
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000
    timer = game_font.render(f"Time : {int(total_time- elapsed_time)}",True,(255, 255, 255))
    screen.blit(timer, (10,10 ))

    # 시간 초과했다면.
    if total_time - elapsed_time  < 0 :
        game_result = "Time Over"
        running = False
    
    

    pygame.display.update()             # 게임화면 계속 그리기. while 문안의 게임이 계속 실행되는동안 화면을 그려줘야한다.

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect =  msg.get_rect(center = (int(screen_width / 2) , int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()