# Window 
FPS = 30
WIDTH = 1000
HEIGHT = 800
WIDTH *= (4 / 3) / (WIDTH / HEIGHT)  # Makes sure the window is 4/3

# UI
UISCALE = 1
UISCALE = max(0.1, min(UISCALE, 0.8))  # Values higher than 0.8 are too big and the UI gets messy, less than 0.01 are too small
BLOCKSIZE = WIDTH / 9 * UISCALE
MARGIN = BLOCKSIZE // 3
PADDING = WIDTH * (1 / 400)

# Colors
BACKGROUNDCOLOR = (198, 198, 198)
SLOTCOLOR = (138, 138, 138)
SLOTHOVERCOLOR = BACKGROUNDCOLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
