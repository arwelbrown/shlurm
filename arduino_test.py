import platformio
import time
from pyfirmata import Arduino, util

board = Arduino("/dev/ttyACM0")

def arduino_loop(board):

    time.sleep(3)

    iterator = util.Iterator(board)
    iterator.start()

    v1 = board.get_pin("a:0:i")
    time.sleep(1.0)
    print(v1.read())

arduino_loop(board)

# It appears that the value 0.219 is popular, occasionally as I apply pressure I receive back a value around 25.0, this is intermittent - why?