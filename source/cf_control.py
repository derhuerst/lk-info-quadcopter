import time, sys, math
from threading import Thread
sys.path.append("lib")
import cflib
from cflib.crazyflie import Crazyflie
from cflib.crazyflie import log

import hover
import acc_printer, gyro_printer, stab_printer
import simple_flight

 
class control:
    """
    Represents a control. Execute commands and close it at the end.
    """
    def __init__(self, methodSetupFinished):
        """
        Constructor
        Connect to the crazyflie; runs the setup method in a new thread;
        finally calls a custom method (in the interface)

        @param methodSetupFinished method():void method called after setup finished
        """
        self.methodSetupFinished = methodSetupFinished
        self.crazyflie = Crazyflie()
        cflib.crtp.init_drivers()
 
        # You may need to update this value if your Crazyradio uses a different frequency.
        self.crazyflie.open_link("radio://0/10/250K")
        time.sleep(0.2)
        # Set up the callback when connected
        self.crazyflie.connectSetupFinished.add_callback(self._connectSetupFinished)
 
    def _setup(self):
        self.sensors = sensors(self.crazyflie, 10)
        while not self.sensors.ready():
            time.sleep(0.1)
        self.methodSetupFinished()

    def _connectSetupFinished(self, linkURI):
        # Start a separate thread to do the motor test.
        # Do not hijack the calling thread!
        Thread(target=self._setup).start() # Thread(target=self.pulse_command).start()

    def command(self, command, max_duration, *params):
        """
        Calls a command

        @param command string command as a string
        @param max_duration integer maximal duration of the command in millisecounds
        @param params tupel multiple additional arguments dependig on the command
        """
        print command
        if command == 'hover':
            hover.start(self, max_duration, *params)
        elif command == 'acc_printer':
            acc_printer.start(self, max_duration, *params)
        elif command == 'gyro_printer':
            gyro_printer.start(self, max_duration, *params)
        elif command == 'stab_printer':
            stab_printer.start(self, max_duration, *params)
        elif command == 'simple_flight':
            simple_flight.start(self, max_duration, *params)

    def close(self):
        """
        Close the connecton to the crazyflie
        """
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
    # newtrack = (x,y,z)
    # newtrack_geo = (x,y,z)
    # pos_geo = (x,y,z)
    # stab_roll
    # stab_pitch
    # stab_yaw
    # stab_thrust
    # gyro_per_secound_x
    # gyro_per_secound_y
    # gyro_per_secound_z
    # gyro_x
    # gyro_y
    # gyro_z

    
    def __init__(self, crazyflie, timer):
        self.MAIN_TIMER = timer
        self.acc_x_default = 0
        self.acc_y_default = 0
        self.acc_z_default = 0
        self.speed_x = 0
        self.speed_y = 0
        self.speed_z = 0
        self.newtrack_geo = (0,0,0)
        self.pos_geo = (0,0,0)
        self.gyro_x = 0
        self.gyro_y = 0
        self.gyro_z = 0
        self.path_file = open('path.csv', 'w')
        
        # Acceleration
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
        self.data_count_act = 0
        self.acc_ready = False

        # Stablilizer
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

        # Gyro
        self.logGyro = log.LogConfig("Gyro", self.MAIN_TIMER)
        self.logGyro.add_variable("gyro.x", "float")
        self.logGyro.add_variable("gyro.y", "float")
        self.logGyro.add_variable("gyro.z", "float")
        crazyflie.log.add_config(self.logGyro)
        if self.logGyro.valid:
            self.logGyro.data_received_cb.add_callback(self.gyro_callback)
            self.logGyro.start()
            print "logGyro started"
        else:
            print "Could not setup log configuration for Gyro after connection!"

    def __del__(self):
        self.path_file.close()

    def ready(self):
        return self.acc_ready

    def acc_callback(self, ident, data, logconfig):
        self.acc_x = data["acc.x"]
        self.acc_y = data["acc.y"]
        self.acc_z = data["acc.z"]
        
        if self.data_count_act == self.data_count:
            self.acc_x_default = self.acc_x_default/self.data_count
            self.acc_y_default = self.acc_y_default/self.data_count
            self.acc_z_default = self.acc_z_default/self.data_count
            print "Kalibration abgeschlossen"
            self.acc_ready = True
        elif self.data_count_act < self.data_count:
            self.acc_x_default = self.acc_x_default+data["acc.x"]
            self.acc_y_default = self.acc_y_default+data["acc.y"]
            self.acc_z_default = self.acc_z_default+data["acc.z"]
        else:
            self.speed_x = self.speed_x+(self.acc_x - self.acc_x_default)*self.MAIN_TIMER/1000
            self.speed_y = self.speed_y+(self.acc_y - self.acc_y_default)*self.MAIN_TIMER/1000
            self.speed_z = self.speed_z+(self.acc_z - self.acc_z_default)*self.MAIN_TIMER/1000
            self.newtrack = (self.speed_x*self.MAIN_TIMER/1000,
                             self.speed_y*self.MAIN_TIMER/1000,
                             self.speed_z*self.MAIN_TIMER/1000)
            self.newtrack_geo = self.drone_to_geodetic(self.newtrack)
            self.pos_geo = (self.pos_geo[0]+self.newtrack_geo[0], self.pos_geo[1]+self.newtrack_geo[1], self.pos_geo[2]+self.newtrack_geo[2])
            self.path_file.write(str(self.pos_geo[0]*1000)+';'+str(self.pos_geo[1]*1000)+';'+str(self.pos_geo[2]*1000)+'\n')
        self.data_count_act += 1
        
    def stab_callback(self, ident, data, logconfig):
        self.stab_roll = data["stabilizer.roll"]
        self.stab_pitch = data["stabilizer.pitch"]
        self.stab_yaw = data["stabilizer.yaw"]
        self.stab_thrust = data["stabilizer.thrust"]

    def gyro_callback(self, ident, data, logconfig):
        self.gyro_per_secound_x = data["gyro.x"]
        self.gyro_per_secound_y = data["gyro.y"]
        self.gyro_per_secound_z = data["gyro.z"]
        
        self.gyro_x = self.gyro_x+self.gyro_per_secound_x*self.MAIN_TIMER/1000
        self.gyro_y = self.gyro_y+self.gyro_per_secound_y*self.MAIN_TIMER/1000
        self.gyro_z = self.gyro_z+self.gyro_per_secound_z*self.MAIN_TIMER/1000


    def drone_to_geodetic(self, vector):
        # phi
        r = self.stab_roll/180.0*math.pi
        # theta
        p = self.stab_pitch/180.0*math.pi
        # psi
        y = self.stab_yaw/180.0*math.pi
        sin_r = math.sin(r)
        sin_p = math.sin(p)
        sin_y = math.sin(y)
        cos_r = math.cos(r)
        cos_p = math.cos(p)
        cos_y = math.cos(y)
        x = vector[0]
        y = vector[1]
        z = vector[2]
        return (cos_p*cos_y*x+(sin_r*sin_p*cos_y-cos_r*sin_y)*y+(cos_r*sin_p*cos_y-sin_r*sin_y)*z,
                cos_p*sin_y*x+(sin_r*sin_p*sin_y-cos_r*sin_y)*y+(cos_r*sin_p*sin_y-sin_r*cos_y)*z,
                -sin_p*x+sin_r*cos_p*y+cos_r*cos_p*z)


    def geodetic_to_drone(self, vector):
        # phi
        r = self.stab_roll/180.0*math.pi
        # theta
        p = self.stab_pitch/180.0*math.pi
        # psi
        y = self.stab_yaw/180.0*math.pi
        sin_r = math.sin(r)
        sin_p = math.sin(p)
        sin_y = math.sin(y)
        cos_r = math.cos(r)
        cos_p = math.cos(p)
        cos_y = math.cos(y)
        x = vector[0]
        y = vector[1]
        z = vector[2]
        return (cos_p*cos_y*x+cos_p*sin_y*y+-sin_p*z,
                (sin_r*sin_p*cos_y-cos_r*sin_y)*x+(sin_r*sin_p*sin_y-cos_r*sin_y)*y+sin_r*cos_p*z,
                (cos_r*sin_p*cos_y-sin_r*sin_y)*x+(cos_r*sin_p*sin_y-sin_r*cos_y)*y+cos_r*cos_p*z)
            
