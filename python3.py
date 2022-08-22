# Python program to demonstrate tangent circle drawing
import time
import threading
import turtle
import sys

# khoa luong
threadLock = threading.Lock()
# số rùa
global n
# dem so rua toi dich
global global_counter


# hàm vẽ hinh tròn
def draw_circle(radius, t, orientation,color):
    global n
    # dem so rua toi dich
    global global_counter
    half = radius/2
    k = radius/(radius+40)

    t.pencolor("black")

    if(orientation==0):
        t.setx(radius)
        t.left(90)
    if(orientation==1):
        t.sety(radius)
        t.left(180)
    if(orientation==2):
        t.setx(-radius)
        t.left(270)
    if(orientation==3):
        t.sety(-radius)   

    t.pencolor(color)

    while(radius>half-1):
        # vẽ hinh tròn
        t.circle(radius)
        
        radius = radius-k
 
    #  đồng bộ
    with threadLock:
        global_counter += 1     #khi rùa tới dích += 1
        if global_counter==n:   #nếu số rùa tới đích đủ thì dừng
            turtle.bye()
    pass


if __name__ == '__main__':

    turtle.bgcolor("black")
    # dem so rua toi dich
    global_counter = 0
    start = time.time() # dem thoi gian bắt đầu
    crl = ["blue","red","yellow","green"]

    # bán kính
    r = int(sys.argv[1])

    n = 4

    # khởi tạo mảng n con rùa
    t = [turtle.Turtle() for i in range(n)]
    #khởi tạo mảng Luồng
    threadArr = []
      
    # loop for printing tangent circles 
    for i in range(1, n + 1, 1):
        t[i-1].hideturtle()
        t[i-1].speed(0)
        t1 = threading.Thread(target=draw_circle, args=(r,t[i-1],int(i%4),crl[int(i%4)]))
        t1.setDaemon(True)
        threadArr.append(t1)
    for i in threadArr:
        i.start()


    turtle.done()

    end = time.time()
    #print("thoi gian xu ly")
    #print(end - start, "s")
    n = (int)((end - start)*1000)
    print(n)
    sys.exit(n) 







