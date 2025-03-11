# void-stranger-ap
Archipelago integration for Void Stranger. By being here I assume you know everything about the game, if you haven't 
finished the game, then scram!

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

## AP Menu

If the game was patched successfully, you can open the AP menu by pushing F10 or binding a controller button to it.
The AP menu has three pages, which can be navigated with left and right.

- Connection page
  This is the default page. Here you can input the connection details to connect to the AP server.
  Press Tab to move to the next field, Delete to clear the current field, and Enter to connect to AP.
  Your most recent connection will be saved.

- Mon Bank page
  Any locusts you receive from AP are sent here (if Locust-Sanity is turned on). Up/Down to navigate the options.
  You can withdraw and throw out locusts at will. Throwing out locusts DOES NOT deposit them back into the bank.
  Upon Atoning, your locust count resets as well as the amount withdrawn, but not the amount received.
  For rando balance reasons, you cannot withdraw if that would cause you to hold more than you've recieved.

- Tracker page
  This page keeps track of all the items you've received.
  Top row is brands, middle row is statues (only three are implemented), bottom row in order is:
    Void Memory, Seal of Lust, Void Wings, Mon Badge (Unimplemented), Void Sword, Seal of Sloth, Void Rod, Interface Manip
  Shortcuts will show up on the righthand side with the shortcut number and an image depicting it.
  The DIS Brand appears as a large DIS Badge between the three rows and the shortcuts, if you have it.

## Known bugs

1. GAME BREAKING ASYNC BUG!!!: If the Endless Void Rod is sent to you while the game is not connected to the AP Server,
then you won't get the rod upgrade, and you will need to have it cheated in.

2. If a Burden is received while one of the AP menus is open (connection menu, locust menu or item tracker), it will not
be properly unlocked in game. Closing and reopening the game should fix this.

3. There is a bug with how the game is recompiled by UMT that can cause crashes when a textbox displays with different 
dialogue sounds. I fixed all the ones needed to complete a run, but I'm sure there are other instances of this across 
the game. If you run into this please provide the crash message, so I can fix it.

## General options/game info
Game Spoilers ahead, read at your own risk

The apworld assumes you play as Gray with the DIS ending as the only goal. Playing as Lillie will make certain locust 
chest locations uncheckable, and Cif cannot goal. 

Items are not received if the player does not carry the void rod. 
An error message will display: "Waiting for VR Connection" until it is picked up. Then the game sends a sync message to 
the AP server and all items are received. 

The Pause menu contains 2 new options replacing the close game option: Atone and End Run. The first acts as a portable 
atoner, letting you go back to B001 at any time. The second is used to go back to brand entry, mostly so players can 
quickly exit their current run. Going back to brand entry in the middle of an AP run is not recommended as you will lose
your items.

By default, the following are randomized: 

- Burdens
- Seals on the Endless Void Rod, with killing the traitors as locations
- The Endless Void Rod
- The ability to access the interface, with a location on the Egg in Gor's chamber since it hints about the interface. 
Make sure to have the Void Memory for that check.

The location and Item names are intentionally vague to minimize spoiling the game for other players, if you need 
to see what all the names mean you can check the 
item names here: https://github.com/CriminalPancake/void-stranger-ap/blob/main/voidstranger/Constants/ItemNames.py

and the location 
names here: https://github.com/CriminalPancake/void-stranger-ap/blob/main/voidstranger/Constants/LocationNames.py

There are options for the following:

- Randomizing normal chests. Adds locust idols to the pool and they are managed by the Mon Bank. See "AP Menu" above.
- Adding the ability to use brands to the item pool, with the murals having locations. Without a Void Lord's Brand,
  you cannot progress beyond their domain. No shortcuts of any kind are considered
  in the logic with this enabled at the moment
- Disabling Smilers, Lovers and Killers until finding their respective items. Adds locations for talking to them with 
the void memory. Note that getting all of these items is required for go mode, and you may get stuck without them
in the final area
- Adding ability to use shortcuts to the item pool, talking to Mon in each location gives checks
- Skipping the long sequence of cutscenes before the final section of gameplay.

For now, the only goal is the DIS ending, goal is sent after completing the final gameplay section before the ending 
sequence.

## Future Plans

1. Support for characters other than Gray, more on that in #2

2. More Goals, I'm thinking the normal ending for all three characters. Perhaps Bee's Stinky Hole would be a good short 
goal. Additionally, a MacGuffin oriented goal seems fitting. Carcass ending seems like a pretty bad goal in my opinion, 
requires exactly one item and its annoying to reach unless you play as Cif.

3. Add an option for all kinds of shortcuts being accounted for in logic with brandsanity

4. MAYBE more locations, but many ideas I've seen (memento crystals mainly) have one big issue: there aren't any more 
items left to place in those locations. Perhaps I could let the player choose locust chests or memento crystals as 
locations, but not both. There are already way too many locust items in the pool as it is.

5. Possibly shuffling in new player dungeons and floors to remix things up?


## Special Thanks

ThatOneGuy - For making the Manual Void Stranger AP Implementation

Rayze - For sticking around and bouncing ideas around with me from the start

Leonarth - For helping a massive amount with the gamemaker net code side of things (and of course working on that library
in the first place!)

Cavin856 - For help with bugfixes and adding several improvements and features to the mod