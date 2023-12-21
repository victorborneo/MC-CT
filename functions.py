import os

import pygame as pg
from pygame.locals import *

from instances import *
from consts import BLOCKSIZE
from classes.item import Item


def quit_handler(_):
    pg.quit()
    quit()


def motion_handler(evt):
    global last_hovered

    if not selected.is_empty():
        selected.x, selected.y = evt.pos
        selected.x -= BLOCKSIZE / 2
        selected.y -= BLOCKSIZE / 2

    if last_hovered is not None:
        last_hovered.hover_out()
        last_hovered = None

    slot = crafting_table.is_hovered(evt.pos)    

    if slot:
        last_hovered = slot
        slot.hover_in()
        return

    slot = inventory.is_hovered(evt.pos)

    if slot:
        last_hovered = slot
        slot.hover_in()
        return


def click_handler(evt):
    if last_hovered is None or evt.button not in (1, 3):
        return

    if not selected.is_empty():
        if last_hovered.item is not None:
            if last_hovered.item.name != selected.name:
                if last_hovered.special_slot:
                    return
                aux_selected = Item(
                    selected.name,
                    selected.item_type,
                    selected.amount,
                    selected.x,
                    selected.y
                )
                selected.__init__(
                    last_hovered.item.name,
                    last_hovered.item.item_type,
                    last_hovered.item.amount,
                    evt.pos[0] - BLOCKSIZE / 2,
                    evt.pos[1] - BLOCKSIZE / 2
                )
                last_hovered.item = aux_selected
            else:
                if last_hovered.special_slot:
                    if selected.amount + last_hovered.item.amount <= 64:
                        selected.sum_amount(last_hovered.item.amount)
                        crafting_table.crafted()
                else:
                    if last_hovered.item.amount < 64:
                        if evt.button == 1:
                            amount = min(64 - last_hovered.item.amount, selected.amount)
                            last_hovered.item.sum_amount(amount)
                            selected.sum_amount(-amount)
                        else:
                            selected.sum_amount(-1)
                            last_hovered.item.sum_amount(1)
        else:
            if last_hovered.special_slot:
                return
            if evt.button == 1:
                last_hovered.item = Item(
                    selected.name,
                    selected.item_type,
                    selected.amount,
                    selected.x,
                    selected.y
                )
                selected.clear()
            else:
                last_hovered.item = Item(
                    selected.name,
                    selected.item_type,
                    1,
                    selected.x,
                    selected.y
                )
                selected.sum_amount(-1)
        last_hovered.place_item()
    else:
        if last_hovered.item is not None:
            if evt.button == 1:
                selected.__init__(
                    last_hovered.item.name,
                    last_hovered.item.item_type,
                    last_hovered.item.amount,
                    evt.pos[0] - BLOCKSIZE / 2,
                    evt.pos[1] - BLOCKSIZE / 2
                )
                last_hovered.item = None
                if last_hovered.special_slot:
                    crafting_table.crafted()
            else:
                if last_hovered.special_slot:
                    return
                selected.__init__(
                    last_hovered.item.name,
                    last_hovered.item.item_type,
                    last_hovered.item.amount // 2,
                    evt.pos[0] - BLOCKSIZE / 2,
                    evt.pos[1] - BLOCKSIZE / 2
                )

                if last_hovered.item.amount % 2 != 0:
                    last_hovered.item.set_amount((last_hovered.item.amount + 1) // 2)
                else:
                    last_hovered.item.set_amount(last_hovered.item.amount // 2)
    crafting_table.craft()


def keyboard_handler(evt):
    if pg.key.get_mods() & KMOD_LALT and evt.key == K_c:
        command = input().strip().split(maxsplit=1)

        if len(command) > 1:
            command, args = command
        else:
            command = command[0]

        func = command_linker.get(command)
        if func is not None:
            func(*args.split())
        else:
            print("Unknown command")


def give_item(*args):
    if len(args) == 1:
        item = args[0]
        amount = "1"
    elif len(args) == 2:
        item, amount = args
    else:
        print("'give' command syntax: give <item> <amount=1>")
        return
    
    if not amount.isdigit():
        print("'amount' argument must be an integer.")
        return
    
    item = item.lower()
    amount = int(amount)

    if os.path.isfile(f"./images/item/{item}.png"): 
        inventory.add_item(item, "item", amount)
        return
    if os.path.isfile(f"./images/block/{item}.png"):
        inventory.add_item(item, "block", amount)
        return

    print("Invalid item.")


linker = {
    QUIT: quit_handler,
    MOUSEMOTION: motion_handler,
    MOUSEBUTTONDOWN: click_handler,
    KEYDOWN: keyboard_handler
}

command_linker = {
    "give": give_item
}
