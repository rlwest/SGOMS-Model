# this file attempts to use a listener function

##class Sgoms:
##
##    def run(self):
##      for pu in self.planning_units:
##        print ('planning unit = ', end=' ')
##        print (pu)
##        for ut in self.planning_units[pu]:
##          print ('   unit task = ', end=' ')
##          print (ut)
##          for m in self.unit_tasks[ut]:
##            print ('      method = ', end=' ')
##            print (m)

from pynput import keyboard


class Sgoms:
    
    def on_release(self,key):
        try:        
            if key.char == 'd':
                return False # Stop listener - or listener.stop??
            if key.char == 'w':
                print(5555555555555555555)
                self.step()
        except AttributeError:
            print('{0} has no function'.format(key))


    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join() # run the listener thread
        print('stopped')


    def _init_(self):
        self.planning_unit=None
        self.unit_task=None
        self.method=None

    def step(self):
        print('step')
