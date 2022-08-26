import sys
sys.path.insert(0, './ecosystem')

import ecosystem
import rendering

def main():
    eco = ecosystem.Ecosystem(number_organisms=10, food_amount=10, step_size=0.5)
    screen = rendering.setup()
    running = True

    while running:
        eco.step()
        rendering.update(screen, eco)
        running = rendering.process_events()
    
    rendering.stop()

main()