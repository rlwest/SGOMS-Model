from sgoms import *

mySgoms = Sgoms()

mySgoms.planning_units = {
  "pu1": ['ut1', 'ut2', 'ut3', 'ut4'],
  "pu2": ['ut2', 'ut3', 'ut4', 'ut3','ut4']
}

mySgoms.unit_tasks = {
  "ut1": ['m1', 'm2', 'm3'],
  "ut2": ['m2', 'm4', 'm4', 'm1'],
  "ut3": ['m3', 'm4', 'm1', 'm1'],
  "ut4": ['m4', 'm1', 'm2', 'm3']
}

mySgoms.run()
