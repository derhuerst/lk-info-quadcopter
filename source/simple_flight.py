import time

def start(control, max_duration, *params):
    for i in xrange(max_duration/10):
        control.crazyflie.commander.send_setpoint(*params)
        time.sleep(0.01)
