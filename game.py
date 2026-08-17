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
    pygame.font.init()
    screen = pygame.display.set_mode(CANVAS_SIZE)
    background = pygame.image.load("background.png").convert()
    font = pygame.font.Font('Kubasta.ttf', 32)

    textbox = pygame.Rect(20, 340, 600, 120)

    running = True

    def draw_text(text: str, color: pygame.Color = pygame.Color("white"), antialias: bool = True):
        # we can have 29 characters and 3 lines
        count = 0
        lines = []
        currentline = ""

        for letter in text:
            #TODO handle newlines when \n detected
            currentline += letter
            count += 1
            if count == 29:
                lines.append(currentline)
                currentline = ""
                count = 0
        
        if currentline:
            lines.append(currentline)

        count = 0
        for line in lines:
            #TODO if lines > 3 then wait for user input before showing next line(s)
            text_obj = font.render(line, antialias, color)
            shadow_wizard_math = count * 20
            shadow_wizard_math += count * 9
            screen.blit(text_obj, (40, 340 + shadow_wizard_math))
            count += 1

    # main game loop
    while running:
        # fetch new events, like input
        events = pygame.event.get()

        # die
        if any(event.type == pygame.QUIT for event in events): # pylint: disable=no-member
            running = False

        # fill screen with background color, draw image & textbox
        screen.fill(BACKGROUND_COLOUR)
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, (33,33,33), textbox)

        # TODO: the game
        draw_text("1234567890123456789012345678912345678901234567890123456789123456789012345678901234567891234567890")

        # here is your frame sir
        pygame.display.flip()

        # wait till our next frame
        await asyncio.sleep(FRAME_DELAY)
