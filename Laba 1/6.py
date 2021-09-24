import turtle as trt

n = int(input("Введите кол-во ног: "))
angle = 360 / n
for i in range (0 , n):
    trt.left(angle)
    trt.forward(50)
    trt.stamp()
    trt.penup()
    trt.goto(0 , 0)
    trt.pendown()
