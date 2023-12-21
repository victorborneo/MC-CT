from consts import WIDTH
from consts import HEIGHT
from consts import MARGIN
from consts import PADDING
from consts import BLOCKSIZE
from classes.slot import Slot
from classes.item import Item


class Inventory:
    def __init__(self):
        self.x_offset = WIDTH / 2 - (9 / 2 * BLOCKSIZE + 9 // 2 * PADDING)
        self.y_offset = HEIGHT - (4 * BLOCKSIZE + 2 * PADDING + 10 * PADDING + MARGIN)

        self.inv = self.build_inventory()
        self.hand = self.build_hand()

    def build_inventory(self):
        inv = [[None for _ in range(9)] for _ in range(3)]

        for i, line in enumerate(inv):
            for j, _ in enumerate(line):
                x = self.x_offset + j * BLOCKSIZE + PADDING * j
                y = self.y_offset + i * BLOCKSIZE + PADDING * i
                inv[i][j] = Slot(x, y)

        return inv

    def build_hand(self):
        hand = [None for _ in range(9)]

        y = self.y_offset + 3 * BLOCKSIZE + PADDING * 2 + PADDING * 10
        for i, _ in enumerate(hand):
            x = self.x_offset + i * BLOCKSIZE + 2 * i
            hand[i] = Slot(x, y)

        return hand

    def draw(self, ctx):
        for i, line in enumerate(self.inv):
            for j, _ in enumerate(line):
                self.inv[i][j].draw(ctx)

        for i, _ in enumerate(self.hand):
            self.hand[i].draw(ctx)

    def is_hovered(self, pos):
        for line in self.inv + [self.hand]:
            for slot in line:
                if slot.is_hovered(pos):
                    return slot

        return False

    def add_item(self, item_name, item_type, amount):
        for line in self.inv + [self.hand]:
            for slot in line:
                if slot.item is None:
                    pack_amount = min(64, amount)
                    amount -= pack_amount
                    slot.item = Item(item_name, item_type, pack_amount, slot.x, slot.y)

                    if amount == 0:
                        return
