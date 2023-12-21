from typing import Any
import pygame as pg

from consts import PADDING
from consts import BLOCKSIZE
from consts import WHITE
from consts import BLACK


class Item:
    def __init__(self, name=None, item_type=None, amount=None, x=None, y=None, tag=None):
        if not amount:
            self.clear()
            return

        self.x = x
        self.y = y
        self.name = name
        self.alt_name = self.name.replace("_", " ").capitalize()
        self.tag = self.get_tag()

        self.item_type = item_type
        self.amount = amount
        self.image = pg.image.load(f"./images/{self.item_type}/{self.name}.png")
        self.image = pg.transform.scale(self.image, (BLOCKSIZE, BLOCKSIZE))

        self.font = pg.font.Font("./fonts/Minecraft.ttf", round(BLOCKSIZE / 2))
        self.font_surf = self.font.render(str(self.amount), True, WHITE)
        self.back_font_surf = self.font.render(str(self.amount), True, BLACK)
        self.font_size_width, _ = self.font.size(str(self.amount))

    def set_font(self):
        self.font_surf = self.font.render(str(self.amount), True, WHITE)
        self.back_font_surf = self.font.render(str(self.amount), True, BLACK)
        self.font_size_width, _ = self.font.size(str(self.amount))

    def set_amount(self, amount):
        self.amount = amount
        self.set_font()
        if self.amount <= 0:
            self.clear()

    def sum_amount(self, amount):
        self.amount += amount
        self.set_font()
        if self.amount <= 0:
            self.clear()

    def clear(self):
        self.x = None
        self.y = None
        self.name = None
        self.alt_name = None
        self.item_type = None
        self.amount = None
        self.image = None
        self.font = None
        self.font_surf = None 
        self.back_font_surf = None 
        self.font_size_width = None
        self.tag = None

    def is_empty(self):
        return self.amount is None

    def draw(self, ctx):
        if self.image is None:
            return

        ctx.blit(self.image, (self.x, self.y))
        ctx.blit(
            self.back_font_surf, (
                self.x + BLOCKSIZE - self.font_size_width,
                self.y + BLOCKSIZE - BLOCKSIZE / 2.5
            )
        )
        ctx.blit(
            self.font_surf, (
                self.x + BLOCKSIZE - self.font_size_width - PADDING * 1.5,
                self.y + BLOCKSIZE - BLOCKSIZE / 2.5 - PADDING * 1.5
            )
        )

    def get_tag(self):
        if "log" in self.name:
            return "log"
        if "planks" in self.name:
            return "planks"
    
        return None
