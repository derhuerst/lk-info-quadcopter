import time

def start(control, max_duration, *params):
    for i in xrange(max_duration/10):
        print control.sensors.gyro_x, control.sensors.gyro_y, control.sensors.gyro_z
        time.sleep(0.01)
