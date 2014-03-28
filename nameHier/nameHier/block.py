'''
    Module for the block-system of the nameHier.
    This block-system is the core of our lib. Every module should inherit from Block.
    This system works like LEGO, but you have different blocks. There are blocks that can have blocks under them and blocks that can't.
    If it has children you have to inherit from Block1 or BlockN. Because of this system there is sort of a tree-structure.
    That means that every step the whole tree gets traversed. Every block without a child return what it wants the drone to do.
    The father of the returning block uses the data to calcute its data and return it to his father.
    When all this data come to Drone, which is an instance of Block1, the real drone will execute what his direct child returned to Drone.
    Every new block for nameHier should use this system, but new returning types are possible as long as Drone gets RPYT.

    Author: Lukas Radke; Sebastian Seedorf
    Date: 2014-03-25
    
'''

class Block(object):
'''
    Baseclass that every class in the lib should inherit from.
    You can give it zero children.
'''
    _sensor = None  # Pointer to the instance of Sensor

    def __init__(self, sensor):
    '''
        Constructor of the class Block.
        It needs as a parameter a pointer to an instance of Sensor.
        If this parameter is None Sensor can't be used or it will lead to an error.
    '''
        _sensor = sensor
        
    def tick(self):
    '''
        This function calls compute without params.
        It needs no params.
        @return fitting interface
    '''
        return self._compute()

    def _compute(self):
    '''
        virtual:
        Function that computes values with giving data.
        @return fitting interface
    '''
        pass


class Block1(Block):
'''
    Baseclass every class with exactly one child should inherit from.
    You can give an instance inheriting from this class a child with a fitting interface, but only one at a time.
'''
    _child = None
    
    def connect(self, newChild):
    '''
        virtual:
        This function adds the child newChild, if newChild returns the fitting data.
        If Block1 already has a child the old one is removed, when the new one fits, not fitting child means no change for this class.
        @return true if successful
    '''
        pass

    def tick(self):
    '''
        This function calls tick for child and _compute for self.
        @return fitting interface
    '''
        return self._compute(self._child.tick())

    def _compute(self, data):
    '''
        virtual:
        Function that calculates a value with data.
        @return fiiting interface
    '''
        pass
    
class BlockN(object):
'''
    Baseclass every class with more than one child should inherit from.
    You can give it multiple children.
'''
    _children = []
    
    def connect(self, newChild):    
    '''
        virtual:
        This function appends the child newChild to _children, if newChild returns the fitting data.
        @return true if successful
    '''
        pass

    def remove(self, child):
    '''
        Function that removes the child from children by using the address.
        If there is more than one time the first child with this address will be removed.
    '''
        if child in _children:
            _children.remove(child)

    def remove_all(self, child):    
    '''
        Function that removes the child from children by using the address.
        If there is more than one time the same child, all children with this address will be removed.
        It uses remove_first to remove the children.
    '''
        for i in xrange(_children.count(child)):
            self.remove_first(self, child)

    def tick(self):
    '''
        This function calls compute for children of BlockN. After this it calls compute with the returned data from all children
        @return fitting interface
    '''
        return self._compute([c.tick() for c in self._children]) # calls compute for all children

    def _compute(self, data_list):
    '''
        virtual:
        Function that calculates a value with data_list.
        @return fiiting interface
    '''
        pass
