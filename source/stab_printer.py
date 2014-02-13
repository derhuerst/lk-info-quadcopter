import time

def start(control, max_duration, *params):
    for i in xrange(max_duration/10):
        print control.sensors.stab_roll, control.sensors.stab_pitch, control.sensors.stab_yaw, control.sensors.stab_thrust
        time.sleep(0.01)
