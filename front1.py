"""
GUI Front-end Module
TUBES 1 STIMA - 24 Solver with Greedy Approach
"""

# import the pygame module, so you can use it
import pygame
import backend

# define a main function


def main():

    # initialize the pygame module
    pygame.init()

    # load and set the logo
    pygame.display.set_caption("24 Solver - Greedy")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((720, 480))

    # load image (it is in same directory)
    image = pygame.image.load("ass/cards/gray_back.png")
    bgd_image = pygame.image.load("ass/cards/back_cards-07.png")

    # blit image(s) to screen
    # screen.blit(bgd_image, (0, 0))  # first background
    # instead of blitting the background image you could fill it
    # (uncomment the next line to do so)
    screen.fill((255,0,0))

    #screen.blit(image, (50, 50))

    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()

    # define a variable to control the main loop
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
