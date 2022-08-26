import sys
sys.path.insert(0, './ecosystem')

import ecosystem

eco = ecosystem.Ecosystem(number_organisms=10, food_amount=10, step_size=0.01)

eco.run()