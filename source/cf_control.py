import time, sys
from threading import Thread
sys.path.append("lib")
import cflib
from cflib.crazyflie import Crazyflie
from cflib.crazyflie import log

#import hover
import acc_printer

 
class control:
    def __init__(self, methodSetupFinished):
        self.methodSetupFinished = methodSetupFinished
        self.crazyflie = Crazyflie()
        cflib.crtp.init_drivers()
 
        # You may need to update this value if your Crazyradio uses a different frequency.
        self.crazyflie.open_link("radio://0/10/250K")
        time.sleep(0.2)
        # Set up the callback when connected
        self.crazyflie.connectSetupFinished.add_callback(self.connectSetupFinished)
 
    def setup(self):
        self.sensors = sensors(self.crazyflie, 10)
        while not self.sensors.ready():
            time.sleep(0.1)
        self.methodSetupFinished()

    def connectSetupFinished(self, linkURI):
        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        Thread(target=self.setup).start() # Thread(target=self.pulse_command).start()

    def command(self, string, duration):
        if string == 'hover':
            #hover.start(self.crazyflie, duration)
            pass
        elif string == 'acc_printer':
            acc_printer.start(self.crazyflie, duration)

    def close(self):
        self.crazyflie.commander.send_setpoint(0, 0, 0, 0)
        # Make sure that the last packet leaves before the link is closed
        # since the message queue is not flushed before closing
        time.sleep(0.1)
        self.crazyflie.close_link()
        print "Verbindung getrennt."




class sensors:
    # acc_x
    # acc_y
    # acc_z
    # acc_x_default
    # acc_y_default
    # acc_z_default
    # speed_x
    # speed_y
    # speed_z
    # stab_roll
    # stab_pitch
    # stab_yaw
    # stab_thrust

    
    def __init__(self, crazyflie, timer):
        self.MAIN_TIMER = timer
        self.acc_x_default = 0
        self.acc_y_default = 0
        self.acc_z_default = 0
        self.speed_x = 0
        self.speed_y = 0
        self.speed_z = 0
        
        #Acceleration
        self.logAcc = log.LogConfig("Acceleration", self.MAIN_TIMER)
        self.logAcc.add_variable("acc.x", "float")
        self.logAcc.add_variable("acc.y", "float")
        self.logAcc.add_variable("acc.z", "float")
        crazyflie.log.add_config(self.logAcc)
        if self.logAcc.valid:
            self.logAcc.data_received_cb.add_callback(self.acc_callback)
            self.logAcc.start()
        else:
            print "Could not setup log configuration for Acceleration after connection!"
        self.data_count = 100
        self.data_count_act = self.data_count
        self.acc_ready = False

        #Stablilizer
        self.logStab = log.LogConfig("Stabilizer", self.MAIN_TIMER)
        self.logStab.add_variable("stabilizer.roll", "float")
        self.logStab.add_variable("stabilizer.pitch", "float")
        self.logStab.add_variable("stabilizer.yaw", "float")
        self.logStab.add_variable("stabilizer.thrust", "float")
        crazyflie.log.add_config(self.logStab)
        if self.logStab.valid:
            self.logStab.data_received_cb.add_callback(self.stab_callback)
            self.logStab.start()
            print "logStab started"
        else:
            print "Could not setup log configuration for Stabilizer after connection!"

    def ready(self):
        return self.acc_ready

    def acc_callback(self, ident, data, logconfig):
        self.acc_x = data["acc.x"]
        self.acc_y = data["acc.y"]
        self.acc_z = data["acc.z"]
        
        if self.data_count_act == 0:
            self.acc_x_default = self.acc_x_default/self.data_count
            self.acc_y_default = self.acc_y_default/self.data_count
            self.acc_z_default = self.acc_z_default/self.data_count
            print "Kalibration abgeschlossen"
            self.data_count_act -= 1
            self.acc_ready = True
        elif self.data_count_act > 0:
            self.acc_x_default = self.acc_x_default+data["acc.x"]
            self.acc_y_default = self.acc_y_default+data["acc.y"]
            self.acc_z_default = self.acc_z_default+data["acc.z"]
            self.data_count_act -= 1
        else:
            self.speed_x = self.speed_x+(self.acc_x - self.acc_x_default)*self.MAIN_TIMER/1000
            self.speed_y = self.speed_y+(self.acc_y - self.acc_y_default)*self.MAIN_TIMER/1000
            self.speed_z = self.speed_z+(self.acc_z - self.acc_z_default)*self.MAIN_TIMER/1000
            #print (self.acc_x - self.acc_x_default)*self.MAIN_TIMER * 3.6
            #print (self.acc_y - self.acc_y_default)*self.MAIN_TIMER * 3.6
            #print (self.acc_z - self.acc_z_default)*self.MAIN_TIMER * 3.6
            print self.speed_z, (self.acc_z - self.acc_z_default)
            #print '#################'
        
    def stab_callback(self, ident, data, logconfig):
        self.stab_roll = data["stabilizer.roll"]
        self.stab_pitch = data["stabilizer.pitch"]
        self.stab_yaw = data["stabilizer.yaw"]
        self.stab_thrust = data["stabilizer.thrust"]
        
            
