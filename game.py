"""the game:tm:"""

import asyncio

import pygame

# constants
BACKGROUND_COLOUR: pygame.Color = pygame.Color("black")
CANVAS_SIZE: tuple[int, int] = (640, 480)
FRAME_DELAY: float = 1.0 / 60.0

# game data - should be in a seperate file but boohoo :speaking_head: :fire:
enemies = {
    "zombie": {
        "minhealth": 15,
        "maxhealth": 30,
        "attacks": [
            {
                "name": "bite",
                "actions": [
                    {
                        "damage": 5
                    }
                ]
            }
        ]
    }
}

async def main() -> None:
    """main game entry point"""
    # set up pygame with the canvas size
    pygame.init() # pylint: disable=no-member
    screen = pygame.display.set_mode(CANVAS_SIZE)
    background = pygame.image.load("background.png").convert()

    textbox = pygame.Rect(20, 340, 600, 120)

    running = True

    # main game loop
    while running:
        # fetch new events, like input
        events = pygame.event.get()

        # krill yourself <3
        if any(event.type == pygame.QUIT for event in events): # pylint: disable=no-member
            running = False

        # fill screen with background color, draw image & textbox
        screen.fill(BACKGROUND_COLOUR)
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (33,33,33), textbox)

        # TODO: the game

        # here is your frame sir
        pygame.display.flip()

        # wait till our next frame
        await asyncio.sleep(FRAME_DELAY)
