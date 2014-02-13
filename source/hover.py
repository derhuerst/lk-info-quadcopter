import time, math

def start(control, max_duration, *params):
    # Hover Mode

    thrust = 36000
    roll = 0
    pitch = 0

    for i in xrange(max_duration / 10):
        against_speed = get_against_speed(control, (control.sensors.speed_x, control.sensors.speed_y, control.sensors.speed_z), params)
        thrust += math.copysign(against_speed[2]**10 * 150000000000, against_speed[2])
        thrust = min(59999, max(10001, thrust))
        print thrust, against_speed[2]
        #roll += against_speed[0]*-50
        #pitch += against_speed[1]*-50
        control.crazyflie.commander.send_setpoint(roll, pitch, 0, thrust)
        time.sleep(0.01)

def get_against_speed(control, curr_speed, aim_speed_geo):
    """
    Calculates the speed to countersteer

    @param control control_object Crazyflie control object
    @param curr_speed 3-tupel speed vector of current speed in drone constant coordinate system
    @param aim_speed_geo 3-tupel speed vector of aim speed in geodetic coordinate system
    @return 3-tupel speed vector of speed to countersteer in drone constant coordinate system
    """
    curr_speed_geo = control.sensors.drone_to_geodetic(curr_speed)
    against_speed_geo = (aim_speed_geo[0] - curr_speed_geo[0],
                         aim_speed_geo[1] - curr_speed_geo[1],
                         aim_speed_geo[2] - curr_speed_geo[2])
    return control.sensors.geodetic_to_drone(against_speed_geo)
