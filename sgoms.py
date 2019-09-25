# this file attempts to use a listener function


from pynput import keyboard


class Sgoms:
    
    def on_release(self,key):
        try:        
            if key.char == 'd':
                return False # Stop listener (- or listener.stop)
            if key.char == 'w':
                print(5555555555555555555)
                self.step()
            else:
                print('that key has no function')
        except AttributeError:
            print('{0} has no function'.format(key))

    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join() # run the listener thread until stopped
        print('program terminated')

    def step(self):
        print('step')
        for pu in self.planning_units:
            print ('planning unit = ', end=' ')
            print (pu)
