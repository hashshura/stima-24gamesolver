"""
GUI Front-end Module
TUBES 1 STIMA - 24 Solver with Greedy Approach
"""

# import the pg module, so you can use it
import pygame as pg
import random
import backend

# define a main function
def main():

    # initialize the pg module
    pg.init()
    pg.font.init()

    # load and set the logo
    pg.display.set_caption("24 Solver - Greedy")

    # create a surface on screen that has the size of 240 x 180
    screen = pg.display.set_mode((720, 480))

    # load asset
    card = pg.transform.smoothscale(pg.image.load("ass/cards/blue_back.png"), (140, 210))
    # bgd_image = pg.image.load("ass/cards/back_cards-07.png")

    # blit image(s) to screen
    # screen.blit(bgd_image, (0, 0))  # first background
    # instead of blitting the background image you could fill it
    # (uncomment the next line to do so)
    screen.fill(pg.Color('gray25'))

    screen.blit(pg.transform.rotate(card, 90), (50, 300))

    # update the screen to make the changes visible (fullscreen update)
    pg.display.flip()

    # define a variable to control the main loop
    running = True

    # array of cards ID, div by 13 = 0 clubs; 1 diamond; 2 heart; 3 spades
    card_arr = [i+1 for i in range(52)]

    # shuffle card
    for i in range(52):
        ran = random.randint(0,51)
        card_arr[i], card_arr[ran] = card_arr[ran], card_arr[i]

    current_num = []

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pg.event.get():
            # only do something if the event if of type QUIT
            keyinput = pg.key.get_pressed()
            # exit on corner 'x' click or escape key press
            if keyinput[pg.K_ESCAPE]:
                raise SystemExit
            elif event.type == pg.QUIT:
                # change the value to False, to exit the main loop
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                card_pos = pg.Rect(50, 300, 140, 210)

                if card_pos.collidepoint(x, y):
                    if not card_arr:
                        running = False
                        break
                    
                    for i in range(4):
                        current_num.append(card_arr.pop())

                    myfont = pg.font.SysFont('Roboto', 30)
                    textsurface = myfont.render(backend.solve(current_num), False, pg.Color('grey40'))
                    screen.blit(textsurface, (0, 0))
                    
                    screen.blit(pg.transform.smoothscale(pg.image.load("ass/cards/" + str(current_num.pop(0)) + ".png"), (140, 210)), (50, 50))
                    screen.blit(pg.transform.smoothscale(pg.image.load("ass/cards/" + str(current_num.pop(0)) + ".png"), (140, 210)), (210, 50))
                    screen.blit(pg.transform.smoothscale(pg.image.load("ass/cards/" + str(current_num.pop(0)) + ".png"), (140, 210)), (370, 50))
                    screen.blit(pg.transform.smoothscale(pg.image.load("ass/cards/" + str(current_num.pop(0)) + ".png"), (140, 210)), (530, 50))
                    pg.display.flip()
            


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
