# void-stranger-ap
Archipelago integration for Void Stranger

## How to install this
For generation:
Drop the voidstranger.apworld file into your Archipelago\custom_worlds folder

For playing the game:
Find the data.win file for Void Stranger at {YourSteamLibrary}\steamapps\common\Void Stranger, and patch it using either

vsap.bdf (using https://www.romhacking.net/utilities/929/)

or

vsap.xdelta (using https://www.romhacking.net/utilities/598/)

and replace the existing data.win file with the patched one, still named data.win. It might also be wise to keep a copy 
of the original data.win file as a backup in case at any point you need to patch the game again (When I update the patch
files with new content or a fix)

Finally, be sure to add the gm-apclientpp.dll to the Void Stranger folder

## Connecting to a server

If the game was patched successfully, you can open the connection menu by pushing F10. Press tab to enter data and 
move to the next field. (you will have to hit tab a few extra times after the password field) The most recent event from
the AP server is always shown in the top left. 

## Known bugs

1. Locust count might get a little wonky with repeated connections after collecting a large amount of them. I think I 
fixed this already but let me know if anything strange happens with this

2. Mon unfortunately doesnt spawn if you fall short on the locust requirements, despite my best efforts. 

3. There is a bug with how UMT recompiles the game that can cause crashes when a textbox displays with different 
dialogue sounds. I fixed all the ones needed to complete a run, but I'm sure there are other instances of this across 
the game. If you run into this please provide the crash message so I can fix it.

4. if you plead guilty to hoarding locusts in court, chest locations get disabled

5. During the final RPG battle, the command menu text is squished together. This is purely visual thankfully.

## General options/game info
Game Spoilers ahead, read at your own risk

The apworld assumes you play as Gray, playing as Lillie will make certain locust chest locations uncheckable, and Cif 
cannot goal. The only thing randomized by default is the burdens, making for a very small world. There are options for 
randomizing normal chests, ability to use brands, certain statues existing, and the ability to use shortcuts. For now, 
the only goal is the DIS ending, goal is sent after completing the final gameplay section before the ending sequence.

## Future Plans

1. Erase the Known bugs section (except maybe #5, that one isn't that bad)

2. Support for characters other than Gray, more on that in #3

3. More Goals, I'm thinking normal ending for all three characters. Perhaps Bee's Stinky Hole would be a good short 
goal. Carcass ending seems like a pretty bad goal in my opinion, requires exactly one item and its annoying to reach 
unless you play as Cif.

4. MAYBE more locations, but many ideas I've seen (memento crystals mainly) have one big issue: there aren't any more 
items left to place in those locations. Perhaps I could let the player choose locust chests or memento crystals as 
locations, but not both. There are already way too many locust items in the pool as it is.

5. Removing the constant network event debug message? At first, it was just a debug measure but as I played it sort of 
grew on me? It provides a sort of reassurance that the communications are working properly. If enough people raise 
complaints about it I'll get rid of it I suppose.