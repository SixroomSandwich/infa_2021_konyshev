import turtle as trt

for i in range (0 , 10):
    for j in range (0 , 4):
        trt.forward(i * 10 + 5)
        trt.left(90)
    trt.penup()
    trt.goto(-5 * i - 5, -5 * i - 5)
    trt.pendown()
