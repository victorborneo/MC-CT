import pygame as pg

from consts import FPS
from consts import WIDTH
from consts import HEIGHT
from consts import BACKGROUNDCOLOR
from functions import linker
from instances import *


def redraw(ctx, objs):
    ctx.fill(BACKGROUNDCOLOR)

    for obj in objs:
        obj.draw(ctx)

    pg.display.flip()


def main():    
    pg.init()
    clock = pg.time.Clock()
    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Minecraft crafting table")
    pg.display.set_icon(pg.image.load("./icons/crafting_table.ico"))

    while True:
        dt = clock.tick(FPS) / 1000

        for event in pg.event.get():
            func = linker.get(event.type)
            if func is not None:
                func(event)
        
        redraw(window, objs)
        

if __name__ == "__main__":
    main()
