import turtle as trt

spiral_step = 0.1
trt.speed('fastest')
for step_num in range (1 , 721):
    trt.left(1)
    trt.forward((step_num / 360) * spiral_step)
