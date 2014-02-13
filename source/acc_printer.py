import time

def start(control, max_duration, *params):
    for i in xrange(max_duration/10):
        print control.sensors.acc_x, control.sensors.acc_y, control.sensors.acc_z
        time.sleep(0.01)
