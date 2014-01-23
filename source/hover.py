import time, math
from cflib.crazyflie import log


def start(crazyflie, duration):
   
    # Hover Mode
    global acc_x
    global acc_y
    global acc_z
    global acc_x_default
    global acc_y_default
    global acc_z_default
    
    global speed_x
    global speed_y
    global speed_z
    
    global values_to_set_data
    global values_to_set_data_act

    
    global MAIN_TIMER
    MAIN_TIMER = 0.01

    speed_x = 0
    speed_y = 0
    speed_z = 0
    acc_x = 0
    acc_y = 0
    acc_z = 0
    acc_x_default = 0
    acc_y_default = 0
    acc_z_default = 0
    
    values_to_set_data = 100
    values_to_set_data_act = values_to_set_data

       
     while values_to_set_data_act > 0:
        time.sleep(MAIN_TIMER*10)

    thrust = 35000
    roll = 0
    pitch = 0 

    for i in xrange(duration/MAIN_TIMER):
        thrust += speed_z*-2500
        if (speed_z > -0.1) and (speed_z < 0.1):
            #print "#"
            roll = (speed_x*50)
            pitch = (speed_y*50)
        #print pitch, acc_y
        #pitch = math.copysign(1, acc_y)
        #roll += acc_x *-1
        #crazyflie.commander.send_setpoint(roll, pitch, 0, thrust)
        time.sleep(MAIN_TIMER)
        
def acc_callback(ident, data, logconfig):
    global acc_x
    global acc_y
    global acc_z
    global acc_x_default
    global acc_y_default
    global acc_z_default
    global speed_x
    global speed_y
    global speed_z
    global values_to_set_data
    global values_to_set_data_act
    global MAIN_TIMER
    acc_x = data["acc.x"]
    acc_y = data["acc.y"]
    acc_z = data["acc.z"]
    
    if values_to_set_data_act == 0:
        acc_x_default = acc_x_default/values_to_set_data
        acc_y_default = acc_y_default/values_to_set_data
        acc_z_default = acc_z_default/values_to_set_data
        print "Kalibration abgeschlossen"
        print acc_z_default
        values_to_set_data_act -= 1
    elif values_to_set_data_act > 0:
        acc_x_default += data["acc.x"]
        acc_y_default += data["acc.y"]
        acc_z_default += data["acc.z"]
        values_to_set_data_act -= 1
    else:
        speed_x += (acc_x - acc_x_default)*MAIN_TIMER
        speed_y += (acc_y - acc_y_default)*MAIN_TIMER
        speed_z += (acc_z - acc_z_default)*MAIN_TIMER
        #print (acc_x - acc_x_default)*MAIN_TIMER * 3.6
        #print (acc_y - acc_y_default)*MAIN_TIMER * 3.6
        #print (acc_z - acc_z_default)*MAIN_TIMER * 3.6
        print speed_z, (acc_z - acc_z_default)
        
        #print '#################'

    #print math.copysign(acc_x, 1), math.copysign(acc_y, 1), math.copysign(acc_z, 1)
    
def stab_callback(ident, data, logconfig):
    #print "Roll:", data["stabilizer.roll"], "Pitch:", data["stabilizer.pitch"], "Yaw:", data["stabilizer.yaw"], "Thrust:", data["stabilizer.thrust"]
    pass
