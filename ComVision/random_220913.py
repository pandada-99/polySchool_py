import random
import turtle as t

def rand_stamp(posX, posY):
    t.goto(posX, posY)
    icon_num = random.randint(0, num_of_icon-1)
    t.shape("icons/icon-0" + str(icon_num) + ".gif")
    t.stamp()

def draw_ans(posX, posY):
    t.goto(posX, posY)
    t.shape("icons/icon-0" + str(ans_index) + ".gif")
    t.stamp()

def start_game():
    t.reset()
    t.penup()
    t.hideturtle()

    global ans_index
    ans_index = random.randint(0, num_of_icon - 1)
    total_index = 0

    # 10줄 반복
    for line in range(num_of_icon-1):
        # 줄이 바뀔 때 마다 y의 좌표가 100씩 감소함
        posX = start_x_pos
        posY = start_y_pos - (line * 100)

        # 모양 변경하여 10회 출력
        for i in range(num_of_icon+1):
            total_index += 1
            if total_index % 9 == 0:
                draw_ans(posX, posY)
            else:
                rand_stamp(posX, posY)
            posX += 100
    draw_board()

def show_ans():
    t.reset()

def draw_line(startX, startY, endX, endY):
    t.goto(startX, startY)
    t.pendown()
    t.goto(endX, endY)
    t.penup()

def draw_board():
    for x in range(-550, -550+(100*12), 100):
        draw_line(x, 450, x, -450)
    for y in range(-450, 450+(100*10), 100):
        draw_line(-550, y, -550+(100*11), y)

if __name__ == "__main__":
    t.title("Window mini game")
    # t.shape("turtle")
    t.setup(width=1100, height=900)
    t.speed(10)

    num_of_icon = 10

    # 아이콘 등록
    for i in range(num_of_icon):
        t.register_shape("icons/icon-0" + str(i) + ".gif")

    # 최초 위치
    start_x_pos = -500
    start_y_pos = 400

    t.onkey(start_game(), "space")
    t. listen()

    t.onkey(show_ans(), "a")
    t.listen()

    t.done()