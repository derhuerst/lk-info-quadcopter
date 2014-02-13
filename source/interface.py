import cf_control
import time

def testMethod():
    crazy.command('simple_flight', 750, 0, 0, 0, 41000)
    crazy.command('hover', 3000, 0, 0, 0)
    crazy.close()

crazy = cf_control.control(testMethod)
