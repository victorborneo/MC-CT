Minecraft's Crafting Table
==========================

![An example crafting flint and steel](/icons/example1.gif)

**TO SPAWN ITEMS:** With the program opened, press LALT+C to ask for input on the terminal, then use the 'give' command to spawn the item, which follows the following syntax: give \<item\> \<amount\>.
The default for "amount" is 1. "item" should be the name of one of the PNG files inside the "block" or "item" folder, but without the ".png" at the end.

This is a small-scaled replica of Minecraft's crafting table system, which uses pattern recognition, so I thought it would be interest to try to replicate.

If you want to try it yourself, but the item you want to craft haven't been implemented by me, you can add it pretty easily by following the pattern of the "crafting.json" file.

Also, Microsoft has some documentation on how the crafting table system works, which I did follow to replicate it.

Just be mindful of shapeless and shaped items, that is, items that don't have a specific shape to be crafted need to go to the "shapeless" list of the JSON, whilst the others need to go to the "shaped" list.
Also, keep in mind that the syntax for shapeless and shaped items are different. It shouldn't be hard to figure them out just by taking a look at the JSON.

Another important thing to mention is that some items don't work properly because they don't have specific textures for them.
For example, buttons don't have button texture, they are simply smaller cubes that reutiize the texture of the material you used to craft it.

Since I wasn't feeling link implementing 3D stuff and was just more interested on the crafting system itself, I didn't bother implementing those specific items.

There's a workaround, tho, which I used for crafting chests. 
Simply look up the inventory icon for the item in question online, save its png into the "block" or "item" folder, inside "ïmages". Just make sure to give the proper type (block or item) in the JSON file.

![An example crafting planks and stick](/icons/example2.gif)
![An example crafting doors and signs](/icons/example3.gif)