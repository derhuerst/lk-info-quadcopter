from vector import Vector
import math

class CoordinateTransform:
    def __init__(self, roll, pitch, yaw):
        self.set_angles(roll, pitch, yaw)

    def set_angles(self, roll, pitch, yaw):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
    
    def geodetic_to_drone(self, vector):
        # phi
        r = self.roll/180.0*math.pi
        # theta
        p = self.pitch/180.0*math.pi
        # psi
        y = self.yaw/180.0*math.pi
        sin_r = math.sin(r)
        sin_p = math.sin(p)
        sin_y = math.sin(y)
        cos_r = math.cos(r)
        cos_p = math.cos(p)
        cos_y = math.cos(y)
        x = vector[0]
        y = vector[1]
        z = vector[2]
        return Vector(cos_p*cos_y*x+
                      cos_p*sin_y*y+
                      -sin_p*z,
                      (sin_r*sin_p*cos_y-cos_r*sin_y)*x+
                      (sin_r*sin_p*sin_y+cos_r*cos_y)*y+
                      sin_r*cos_p*z,
                      (cos_r*sin_p*cos_y+sin_r*sin_y)*x+
                      (cos_r*sin_p*sin_y-sin_r*cos_y)*y+
                      cos_r*cos_p*z
                     )
    
    def drone_to_geodetic(self, vector):
        # phi
        r = self.roll/180.0*math.pi
        # theta
        p = self.pitch/180.0*math.pi
        # psi
        y = self.yaw/180.0*math.pi
        sin_r = math.sin(r)
        sin_p = math.sin(p)
        sin_y = math.sin(y)
        cos_r = math.cos(r)
        cos_p = math.cos(p)
        cos_y = math.cos(y)
        x = vector[0]
        y = vector[1]
        z = vector[2]
        return Vector(cos_p*cos_y*x+
                (sin_r*sin_p*cos_y-cos_r*sin_y)*y+
                (cos_r*sin_p*cos_y+sin_r*sin_y)*z,
                cos_p*sin_y*x+
                (sin_r*sin_p*sin_y+cos_r*cos_y)*y+
                (cos_r*sin_p*sin_y-sin_r*cos_y)*z,
                -sin_p*x+
                sin_r*cos_p*y+
                cos_r*cos_p*z
               )

class Coordinates:
    def __init__(self, pos_geo_vector, *angles):
        self.pos_geo_vector = pos_geo_vector
        self.transform = CoordinateTransform(*angles)
        self.file = None

    def set_angles(self, *angles):
        self.transform.set_angles(*angles)

    def set_file_append(self, file_path):
        if self.file != None:
            self.file.close()
            self.file == None
        if file_path != None:
            self.file = open(file_path, "a")
            _write_to_file()

    def _write_to_file(self):
        if self.file != None:
            self.file.write(str(self.pos_geo_vector)+'\n')

    def set_newtrack(self, are_drone_coords, newtrack_vector):
        if are_drone_coords:
            newtrack_vector = self.transform.drone_to_geodetic(newtrack_vector)
        self.pos_geo_vector += newtrack_vector
        _write_to_file()
            
    def set_velocity(self, are_drone_coords, velocity_vector, time):
        self.set_newtrack(self, are_drone_coords, velocity_vector*time)
        
    def set_acceleration(self, are_drone_coords, acceleration_vector, time):
        self.set_newtrack(self, are_drone_coords, acceleration_vector*time*time)
