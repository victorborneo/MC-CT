import pygame as pg

from consts import SLOTHOVERCOLOR
from consts import SLOTCOLOR
from consts import BLOCKSIZE
from consts import BLACK
from consts import WHITE


class Slot:
    def __init__(self, x, y, item=None, special_slot=False):
        self.x = x
        self.y = y
        self.item = item
        self.color = SLOTCOLOR
        self.special_slot = special_slot

    def draw(self, ctx):
        pg.draw.rect(
            surface=ctx,
            color=self.color,
            rect=(
                self.x, self.y,
                BLOCKSIZE, BLOCKSIZE
            )
        )

        pg.draw.line(
            surface=ctx,
            color=WHITE,
            start_pos=(self.x + BLOCKSIZE, self.y),
            end_pos=(self.x + BLOCKSIZE, self.y + BLOCKSIZE),
            width=max(1, int(BLOCKSIZE * 0.03))
        )

        pg.draw.line(
            surface=ctx,
            color=WHITE,
            start_pos=(self.x, self.y + BLOCKSIZE),
            end_pos=(self.x + BLOCKSIZE, self.y + BLOCKSIZE),
            width=max(1, int(BLOCKSIZE * 0.03))
        )

        pg.draw.line(
            surface=ctx,
            color=BLACK,
            start_pos=(self.x, self.y),
            end_pos=(self.x + BLOCKSIZE, self.y),
            width=max(1, int(BLOCKSIZE * 0.03))
        )

        pg.draw.line(
            surface=ctx,
            color=BLACK,
            start_pos=(self.x, self.y),
            end_pos=(self.x, self.y + BLOCKSIZE),
            width=max(1, int(BLOCKSIZE * 0.03))
        )

        if self.item is not None:
            self.item.draw(ctx)

    def is_hovered(self, pos):
        mouse_x, mouse_y = pos
        is_in_x = self.x <= mouse_x <= self.x + BLOCKSIZE
        is_in_y = self.y <= mouse_y <= self.y + BLOCKSIZE
        return is_in_x and is_in_y

    def hover_in(self):
        self.color = SLOTHOVERCOLOR

    def hover_out(self):
        self.color = SLOTCOLOR

    def place_item(self):
        self.item.x = self.x
        self.item.y = self.y
