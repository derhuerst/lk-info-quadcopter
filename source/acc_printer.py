import time
from cflib.crazyflie import log


def start(crazyflie):
   
   
    logAcc = log.LogConfig("Acceleration", 200)

    logAcc.add_variable("acc.x", "float")
    logAcc.add_variable("acc.y", "float")
    logAcc.add_variable("acc.z", "float")
    crazyflie.log.add_config(logAcc)
    if logAcc.valid:
        logAcc.data_received_cb.add_callback(acc_callback)
        logAcc.start()
        print "logACC started"
    else:
        print "Could not setup log configuration for stabilizer after connection!"
    
    
    for i in xrange (1000):
        crazyflie.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        time.sleep(0.01)
    time.sleep(0.1)
    crazyflie.close_link()
    
def acc_callback(ident, data, logconfig):
    #print "Id={0}, Stabilizer: Roll={1:.2f}, Pitch={2:.2f}, Yaw={3:.2f}, Thrust={4:.2f}".format(ident, data["stabilizer.roll"], data["stabilizer.pitch"], data["stabilizer.yaw"], data["stabilizer.thrust"])

    #print 'wurst'
    global acc_x
    global acc_y
    global acc_z
    global acc_z_default
    acc_x = data["acc.x"]
    acc_y = data["acc.y"]
    acc_z = data["acc.z"]
    
    print acc_x , acc_y , acc_z



