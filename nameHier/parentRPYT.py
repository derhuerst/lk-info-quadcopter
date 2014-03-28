'''
interface for RPYT
RPYT = roll pitch yaw thrust
placeholder class to check if child has correct interface
every block that inherits from this class has the RPYT interface
RPYT blocks pass data as tuple (R, P, Y, T)
'''
class ParentRPYT(object):
	pass
