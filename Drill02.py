from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 캐릭터 초기 위치 및 상태
character_x, character_y = 400, 90  # 초기 위치 (원 중심)
radius = 200  # 원의 반지름
angle = 0  # 각도 초기값
is_circle = True  # 원운동 상태

while True:
    clear_canvas()

    # 배경 이미지 그리기
    grass.draw(400, 30)

    # 캐릭터 그리기
    character.draw(character_x, character_y)

    # 원운동과 사각형 운동을 번갈아가며 수행
    if is_circle:
        # 원운동
        character_x = 400 + radius * math.cos(math.radians(angle))
        character_y = 300 + radius * math.sin(math.radians(angle))
        angle += 1
        if angle >= 360:
            angle = 0
            break
    else:
        # 사각형 운동
        character_x += 2
        if character_x > 600:
            is_circle = True

    update_canvas()







