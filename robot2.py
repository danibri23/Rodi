
import rodi
import time

robot = rodi.RoDI()  # crear el objeto RoDI

""" def vuelta_cuadrada ():
    for vuelta in range (4):
        robot.move_forward()
        time.sleep(3)
        robot.move_left()
        time.sleep(0.4)
    robot.move_stop()
vuelta_cuadrada()"""


""" color = int (input ("Elija una opción: 1 para rojo, 2 para verde y 3 para azul."))

if color == 1:
    robot.pixel (250,0,0)
    time.sleep (5)
    robot.pixel(0,0,0)

elif color == 2:
        robot.pixel (0,250,0)
        time.sleep (5)
        robot.pixel(0,0,0)

elif color == 3:
        robot.pixel(0,0,255)
        time.sleep(5)
        robot.pixel(0,0,0)

elif color >= 4:
    print ("no tenemos esa opcion!")
    robot.pixel(0,0,0) 
 """

""" 
while True:
    color = int (input ("Elija una opción: 1 para ROJO, 2 para VERDE y 3 para AZUL."))

    if color == 1:
        robot.pixel (250,0,0)
        time.sleep (5)
        robot.pixel(0,0,0)

    elif color == 2:
        robot.pixel (0,250,0)
        time.sleep (5)
        robot.pixel(0,0,0)
        
    elif color == 3:
        robot.pixel(0,0,255)
        time.sleep(5)
        robot.pixel(0,0,0)

    elif color >= 4:
        print ("no tenemos esa opcion!")
        robot.pixel(0,0,0)
        break """
"""""

while True:
    distancia = robot.see() 
    time.sleep (0.01)

    if distancia < 20:
        robot.move_forward()
          
    else:
        robot.move_left()
        time.sleep(0.5)

"""


""""
while True:
    distancia = robot.see() 
    time.sleep (0.1)

    if distancia > 25:
        robot.move_forward()
          
    else:
        robot.move_left()
        time.sleep(0.5)
        robot.move_forward()
        time.sleep(3)

"""
""""
while True:
    linea = robot.sense()
    print (linea [0]),
    print (linea [1])
    time.sleep(0.5)

    if linea < 50:
        robot.move_left()
        time.sleep(1)
          
    elif linea > 50:
        robot.move_forward()
        
"""

while True:
    linea = robot.sense()
    sensor_izq = linea[0]
    sensor_der = linea[1]
    print (linea[0]),
    print (linea[1])
    time.sleep(0.5)
    if sensor_der <100 and sensor_izq <100:
        robot.move_right()
    distancia = robot.see()
    print(robot.see())
    time.sleep(0.1)
    if distancia >10:
        robot.move_forward()
    elif distancia <10:
        robot.move_left
        time.sleep(0.1)
    else:
        robot.move_stop()
 