import pygame

class Event_handler():
    def __init__(self):
        pass

    # Handle keyboard events
    def manage(self):
        for event in pygame.event.get():
            # window close button
            if event.type == pygame.QUIT:
                pygame.quit()

            # on key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
