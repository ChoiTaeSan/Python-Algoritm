import random
import turtle as t

# 화면 초기화
t.clear()

# 터틀을 원래 위치로 이동하고, 초기 모양 설정
t.home()
t.shape('turtle')

# 원 그리기
t.circle(50, 360)  # 반지름 50인 원을 360도 그리기
t.circle(-50, 360) # 반지름 -50인 원을 360도 그리기 (반대 방향)

# 펜을 들어서 이동 중에는 선을 그리지 않도록 설정
t.penup()

# 터틀 속도를 최대(0)로 설정
t.speed(0)

# 색상을 0~255 범위로 설정하기 위해 컬러 모드를 255로 변경
t.colormode(255)

# 터틀이 있는 위치에 점 찍기
t.dot(20)

# 랜덤한 위치와 색상으로 50번 터틀 찍기
for i in range(50):
    # 랜덤한 RGB 색상 생성
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # 터틀 색상 설정
    t.color(r, g, b)
    
    # 랜덤한 위치로 이동
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.goto(x, y)
    
    # 랜덤한 방향 설정
    d = random.randint(0, 360)
    t.setheading(d)
    
    # 랜덤한 크기로 터틀 크기 설정
    t.shapesize(random.randint(1, 5))
    
    # 터틀 모양 도장 찍기
    t.stamp()

# 메인 루프 실행, 창이 닫히지 않도록 유지
t.mainloop()
