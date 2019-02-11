"""
GUI Front-end Module
TUBES 1 STIMA - 24 Solver with Greedy Approach
"""

import pygame

def main():

    # initialize the pygame module
    pygame.init()

    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((720, 480))

    running = True

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
            


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
