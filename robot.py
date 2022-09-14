import rodi
import time

robot = rodi.RoDI () #instancia/crear el objeto RoDi

for vuelta in range (4):
    robot.move_forward()
    time.sleep(3)
    robot.move_left()
    time.sleep(0.4)   

robot.move_stop()


