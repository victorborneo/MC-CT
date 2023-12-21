from classes.inventory import Inventory
from classes.crafting_table import CraftingTable
from classes.item import Item

inventory = Inventory()
crafting_table = CraftingTable()
selected = Item()
last_hovered = None

objs = [inventory, crafting_table, selected]
