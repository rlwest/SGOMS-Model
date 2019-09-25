# this file attempts to use a listener function

class Sgoms:

    def run(self):
      for pu in self.planning_units:
        print ('planning unit = ', end=' ')
        print (pu)
        for ut in self.planning_units[pu]:
          print ('   unit task = ', end=' ')
          print (ut)
          for m in self.unit_tasks[ut]:
            print ('      method = ', end=' ')
            print (m)

