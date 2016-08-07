#! /usr/env/python3



class debugMode():
    '''Provides a simple print out of a variable with in a program
        throuth the debug method. The mode attribute is set(0 is reseved for no printing), then any
         debug method used sending the same value as the mode attribute
        is printed when the program runs.  The mode attribute may be set any where
        in the program such that it is available to the calling debug method. Setting mode
        as a global variable works for the whole program. Use:
        Dbg = debugMode(), Dbg.mode=1, debug=Dbg.debug, x = 5, debug(x,1) see debug method doc.'''
    def __init__(self, mode=(0,)):
        '''Instatiated with default mode = 0 (reserved for no print)
        Mode is the only argument that may be sent'''        
        self.mode = mode
        self.Dict = {}

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, val):
        '''This allows a single integer to be sent to the attribute which is type tuple'''
        if type(val) is  int:
            val = (val,)
            self.__mode = val
        else: self.__mode = val

    def debug(self, var, mode, prt=None):
        '''Placed in code it prints out the varibles, at the point in the code, sent if the
            mode value sent is the same mode value set on then
            instance,(not 0). It also prints with default identifier, which can be set also
            (var, mode,prt)'''
        if mode == 0:
            print(var, ' "0"is reserved for debug off')
            return 
        if prt == None: prt = "debug " + str(mode) + " = "
        if (var,mode) in self.Dict.items() and self.mode in mode: 
            print(prt, var)
        else: 
            self.Dict.update({var:mode})
            # Second test allows you to set up a debug spot for a different mode, to be used later.
            # and then you won't be worried that Debug.mode = is set wrong.
            if self.mode != 0 and (mode in self.mode):
                print(prt, var)

