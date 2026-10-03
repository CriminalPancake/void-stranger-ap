# void-stranger-ap v0.11.X
Archipelago integration for Void Stranger.  
This document and repository contains major spoilers for the game.
Thus, it is not recommended to read this until you have absolutely cleared the game for sure.

## How to install this
For generation:
Drop the voidstranger.apworld file into your Archipelago\custom_worlds folder

For playing the game:

Navigate to the betas tab under properties for the game on steam and select the 'old_version_1.1.1' beta to go back to 
the previous version of the game.


Find the data.win file for Void Stranger at {YourSteamLibrary}\steamapps\common\Void Stranger, and patch it using either:

---
### Windows
vsap.bdf (using https://www.romhacking.net/utilities/929/)

or

vsap.xdelta (using https://www.romhacking.net/utilities/598/)

### Linux
install `xdelta3` via your package manager (or distro specific tools) and use the command:

```sh
xdelta3 -d -s data.win vsap.xdelta data_patched.win
```

inside your game directory

or

install `bsdiff` via your package manager (or distro specific tools) and use the command:

```sh
bspatch data.win data_patched.win patch.bdfs
```

inside your game directory

---
and replace the existing data.win file with the patched one, still named data.win. It might also be wise to keep a copy 
of the original data.win file as a backup in case at any point you need to patch the game again (When the patch is 
updated with new content or a fix)

Finally, be sure to add gm-apclientpp.dll and ap_room_names.csv to the Void Stranger folder

## General options/game info

**Game Spoilers ahead, read at your own risk**  

The apworld assumes you play as Gray with the DIS ending as the only goal.
In the future, content from Lillie and Cif's routes will be added into Gray's route.

Items are not received if the player does not carry the void rod (however they can still be sent).
An error message will display: "Awaiting VR Connection" until it is picked up.
It is safe to send items while not connected to Archipelago; they will be saved and sent the next time you connect.

The Pause menu contains 2 new options replacing the close game option: Atone and End Run. The first acts as a portable 
atoner, letting you go back to B001 at any time. The second is used to go back to brand entry, mostly so players can 
quickly exit their current run. Going back to brand entry in the middle of an AP run is not recommended as you will lose
your items.

By default, the following items are randomized:

- All three Burdens
- Seals of Lust, Greed, and Sloth (Seal of Greed does nothing currently)
- Endless Void Rod
- Interface access
- The Void Fruit (makes you VOID in a certain area)
- Each Void Lord's Brand

Void Lord Brands are required to progress to take the stairs in their corrosponding mural room.  
Additionally, each brand must be acquired to access that Void Lord's secret room.

Further options exist to include some of the Void Lord's Statues as items, and to include Mon's Shortcuts.
Without a particular statue, all instances of it will become mostly useless eggs.  
Currently, only three statues are implemented.

By default, the following locations are checks:

- Locust Chests in numbered branes
- Secret Chests in secret rooms
- The Endless Void Rod chest
- All Murals (Speak to the rock in front of Cif's Mural while having the Void Memory to send Cif's Mural)
- Slaying Tail, Tan, and Gor
- Speaking to the rock in Gor's secret room (Obsolete location, will be removed in 0.12.0)

Further options exist to include various dungeons as locations, such as the Whitevoid area or Mon's Funhouse

The location and Item names are intentionally vague to minimize spoilers for other players in the multiworld.  
You can view a list of the Item and Location names here:
 - https://github.com/Cavin856/void-stranger-ap/blob/main/voidstranger/Constants/ItemNames.py
 - https://github.com/Cavin856/void-stranger-ap/blob/main/voidstranger/Constants/LocationNames.py

### AP Menu

If the game was patched successfully, you can open the AP menu by pushing F10 or binding a controller button to it.
The AP menu consists of multiple sub-menus, which can be navigated with left and right.

- Connection Menu

  This is the default menu until you connect to Archipelago. Here, you input the connectiong details and connect.  
  Press Enter to select a field, Tab to move to the next field, and Delete to clear the current field.  
  Your most recent connection will be saved.

- Mon Bank

  This menu allows you to view and manage the state and quantity of your locusts.  
  Bonus locusts you receive from AP are sent here. You can withdraw them from the bank or throw out locusts on hand.  
  Throwing out locusts does not deposit them back into the bank; they are removed entirely.  
  You cannot withdraw more than your maximum carrying capacity.  
  Atoning will not restore bonus locusts previously withdrawn.

- Tracker

  This menu keeps track of all the items you've received.  
  Top row is brands, middle row is statues (only three are implemented), bottom row in order is:  
  Void Memory, Seal of Lust, Void Wings, Mon Badge (Unimplemented), Void Sword, Seal of Sloth, Void Rod, Interface Manip  
  Shortcuts will show up on the right hand side with the shortcut number and an image depicting it.  
  The DIS Brand appears as a large DIS Badge between the three rows and the shortcuts, if you have it.  
  Also, the Void Fruit will appear if you have it, and your Greed Coins are tracker here.  
  This page is scheduled to be reformatted in v0.13.0

- Waypoints

  This menu allows you to set up to three simultanious waypoints and warp back to them at will.  
  Waypoints restore your locust count to what it was when the waypoint was made.  
  Waypoints can only be set on numbered branes.

- Extra

  This menu was added as a result of having too many menus. Less frequently used menu can be opened here.  
  Currently, this contains the Connection, Debug, and Palette menus.

- Debug

  This menu shows several internal variables used for debugging.  
  If something goes wrong with your game, please include a screenshot of this menu along with your bug report.  
  You can report bugs in the Void Stranger thread of the Archipelago discord.

- Palette

  This menu lets you preview and select a custom palette from the palettes.txt file.  
  Place the palettes.txt file (a sample file is included) in the save directory, which is NOT the same as the game directory.  
  Typically found in appdata/local/void_stranger  
  Custom palettes must follow the following format, where each color is a valid hex color, preceeded by 0x  

  *PaletteName1*  
  0x*Color1*  
  0x*Color2*  
  0x*Color3*  
  0x*Color4*  
  *PaletteName2*  
  0x*Color1*  
  etc.

### Known major issues

1. Opening a chest containing a locust capacity up will not grant additional locusts.
2. It is theoretically possible that logic will require you to loop Cif's Domain (or some other subset of floors)
    more times than reasonable in order to grind up locusts. No solution has been found yet.


## Future Plans

This is not an exhaustive list of all future updates, nor a comprehensive list of everything said updates will contain.
Many more features are planned, but not currently in development.

0.11.1      Music Menu, many QoL fixes
0.12.0      Traps, More Statues, More Dungeon Checks
0.13.0      Location Tracker, New Item Tracker, [*REDACTED*]

## Contributors

This implementation is the result of an entire community, and many people have had a hand in it.  
However, I would like to especially thank the following people, without whom this implementation never would have existed.

- [@Cavin856](https://github.com/Cavin856) -  For handling the current development
- [@CriminalPancake](https://github.com/CriminalPancake) -  For handling the initial development
- [@Eijebong](https://github.com/Eijebong) - For rewriting the entire the pathfinding algorithm and creating the AP generation fuzzer
- [@LeonarthCG](https://github.com/LeonarthCG) - For creating the entire gamemaker net code, the backbone of how we connect to AP

Additionally, I'd like to thank the following people for other contributions to the implementation:

- @Abelism
- [@Rayze421](https://github.com/Rayze421)
- [@Mysteryem](https://github.com/Mysteryem)
- @RoobyRoo
- @ThatOneGuy27
- [@Virulence](https://github.com/VirulenceDev)