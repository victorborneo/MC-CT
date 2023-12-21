import json

from consts import WIDTH
from consts import MARGIN
from consts import PADDING
from consts import BLOCKSIZE
from classes.slot import Slot
from classes.item import Item


class CraftingTable:
    def __init__(self):
        with open("./craftings.json", "r") as f:
            self.craftings = json.load(f)
        self.x_offset = WIDTH / 2 - (5 / 2 * BLOCKSIZE + 2 * PADDING)
        self.y_offset = MARGIN

        self.slots = self.build_slots()
        self.result = Slot(
            self.x_offset + 4 * BLOCKSIZE + PADDING * 4,
            self.y_offset + BLOCKSIZE + PADDING,
            special_slot=True
        )

    def build_slots(self):
        slots = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                x = self.x_offset + j * BLOCKSIZE + PADDING * j
                y = self.y_offset + i * BLOCKSIZE + PADDING * i
                slots[i][j] = Slot(x, y)

        return slots

    def draw(self, ctx):
        for i, line in enumerate(self.slots):
            for j, _ in enumerate(line):
                self.slots[i][j].draw(ctx)

        self.result.draw(ctx)

    def is_hovered(self, pos):
        for line in self.slots + [[self.result]]:
            for slot in line:
                if slot.is_hovered(pos):
                    return slot

        return False

    def crafted(self):
        for i, line in enumerate(self.slots):
            for j, slot in enumerate(line):
                if slot.item is not None:
                    slot.item.sum_amount(-1)
                    if slot.item.amount is None:
                        self.slots[i][j].item = None

    def craft(self):
        has_item = False    
        pattern = []
        ingredients = []
        tag = None
        name_if_has_tag = None
        has_item_on_first_column = False
        has_item_on_first_line = False

        for i, line in enumerate(self.slots):
            line_pattern = []
            for j, slot in enumerate(line):
                if slot.item is not None:
                    if j == 0:
                        has_item_on_first_column = True
                    if slot.item.tag is not None:
                        ingredients.append({"tag": slot.item.tag})
                        line_pattern.append(slot.item.tag)
                        name_if_has_tag = slot.item.name
                        tag = slot.item.tag
                    else:
                        ingredients.append({"item": slot.item.name})
                        line_pattern.append(slot.item.name)
                    has_item = True
                else:
                    line_pattern.append(" ")
            if i == 0 and "".join(line_pattern).strip() != "":
                has_item_on_first_line = True
            pattern.append(line_pattern)

        if not has_item:
            self.result.item = None
            return

        for j in range(2, -1, -1):
            if j == 1 and (len(pattern[0]) == 3 and has_item_on_first_column):
                continue
            if f"{pattern[0][j]}{pattern[1][j]}{pattern[2][j]}".strip() == "":
                for c in range(len(pattern)):
                    del pattern[c][j]
        for i in range(2, -1, -1):
            for j in range(len(pattern[i])):
                if i == 1 and (len(pattern) == 3 and has_item_on_first_line):
                    break
                if pattern[i][j] != ' ':
                    break
            else:
                del pattern[i]

        output = None
        for recipe in self.craftings["shapeless"]:
            if len(recipe["ingredients"]) == len(ingredients):
                a = set(frozenset(d.items()) for d in recipe["ingredients"])
                b = set(frozenset(d.items()) for d in ingredients)
                if a == b:
                    output = recipe["result"]
                    break
        else:
            for recipe in self.craftings["shaped"]:
                if len(pattern) != len(recipe["pattern"]) or len(pattern[0]) != len(recipe["pattern"][0]):
                    continue
                item_pattern = recipe["pattern"].copy()

                for i, line in enumerate(item_pattern):
                    item_pattern[i] = [j for j in line]
                    for j, val in enumerate(item_pattern[i]):
                        if val != ' ':
                            if recipe['key'][val].get("tag") is not None:
                                item_pattern[i][j] = recipe['key'][val]["tag"]
                            else:
                                item_pattern[i][j] = recipe['key'][val]["item"]

                flag = False
                for i, line in enumerate(item_pattern):
                    for j, el in enumerate(line):
                        if el == pattern[i][j]:
                            continue
                        flag = True
                        break
                    if flag:
                        break
                else:
                    output = recipe['result']
                    break

        if output is None:
            self.result.item = None
            return
        
        if output.get('tag') is not None:
            name = name_if_has_tag[:name_if_has_tag.index(tag)]
            name += output['tag']
        else:
            name = output['item']

        self.result.item = Item(
            name=name,
            item_type=output['type'],
            amount=output['amount'],
            x=self.result.x,
            y=self.result.y
        )

