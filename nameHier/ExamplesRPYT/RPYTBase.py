from nameHier import block    # blocksystem is used
from nameHier import parentRPYT     # parentsystem is used

class ThrustRPYT(Block, ParentRPYT):
'''
    Class that gets a thrust when it is created and returns every tick this thrust.
'''
    _thrust = 0      # variable that stores the thrust it should return. It's an absolute value.
    
    def __init__(self, sensor, thrust):
    '''
        Constructor of this class. It needs the address to the sensor instance as the first param and the thrust as a second param.
    '''
        _thrust = thrust
        super(ThrustRPYT, self).__init__(self, sensor)

    def _compute(self):
    '''
        T = _thrust
        @return RPYT
    '''
        return (0, 0, 0, _thrust)



class YawRPYT(Block, ParentRPYT):
'''
    Class that gets a degree when it is created and returns every tick this degree multiplied with 1/2 so that it can be send to the drone directly.
'''
    
    _yaw = 0     # variable that stores the yaw for the drone in degree/2. It's an absolute value.

    def _init__(self, sensor, degree):
    '''
        Constructor of this class. It needs the address to the sensor instance as the first param and the number of degrees as a second param.
    '''
        _yaw = degree*2
        super(YawRPYT, self).__init__(self, sensor)

    def _compute(self):
    '''
        Y = _yaw
        @return RPYT
    '''
        return (0, 0, _yaw, 0)



class PitchRPYT(Block, ParentRPYT):
'''
    Class that gets a pitch when it is created and returns every tick this pitch.
'''
    _pitch = 0      # variable that stores the pitch it should return. It's an absolute value.
    
    def __init__(self, sensor, pitch):
    '''
        Constructor of this class. It needs the address to the sensor instance as the first param and the pitch as a second param.
    '''
        _pitch = pitch
        super(PitchRPYT, self).__init__(self, sensor)

    def _compute(self):
    '''
        P = _pitch
        @return RPYT
    '''
        return (0, _pitch, 0, 0)



class RollRPYT(Block, ParentRPYT):
'''
    Class that gets a roll when it is created and returns every tick this roll.
'''
    _roll = 0      # variable that stores the roll it should return. It's an absolute value.
    
    def __init__(self, sensor, roll):
    '''
        Constructor of this class. It needs the address to the sensor instance as the first param and the roll as a second param.
    '''
        _roll = roll
        super(RollRPYT, self).__init__(self, sensor)

    def _compute(self):
    '''
        R = _roll
        @return RPYT
    '''
        return (_roll, 0, 0, 0)



class RPYTArithmeticCombiner(BlockN, ParentRPYT):
'''
    Class that combines many blocks that return a RPYT-tuple. It calculates the arithmetic mean of the returned values.
    It can only have children that inherit from ParentRPYT.
'''

    def connect(self, newChild):
        if isinstance(newChild, ParentRPYT):
            _children.append(newChild)
            return true
        else:
            return false

    def _compute(self, data_list):
        _arithmetic_mean = 0
        for i in data_list:
            _arithmetic_mean = tuple(sum(x) for x in data_list)
        return _arithmetic_mean/__len__(data_list)
