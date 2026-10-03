from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionSet, PerGameCommonOptions

class LogicComplexity(Choice):
    """
    Simple: Smiler warps (Bee statues) will not be factored into logical progression.
            Interface manipulation will also not be factored into logic with the following exceptions:
                Traversing DIS
                Reaching B000
                Reaching Cif's brand room
            Simple Logic is not compatible with the following options:
                (Nothing yet)
    
    Full:   Smiler warps and interface manipulation are factored into logic.
                (Using the HP value is still not logically required)
            All settings are compatible.
    
    """
    display_name = "Logic Complexity"
    option_simple = 0
    option_full = 1
    default = 1

class Shortcutsanity(Toggle):
    """
    Access to each of Mon's five shortcuts are now items.
    Speaking to Mon at his five hint locations will each send a check.
    Only shortcuts 3, 4, and 5 have logical implications currently.
    """
    display_name = "Shortcutsanity"
    default = 1

class Idolsanity(Toggle):
    """
    When enabled, the Lover, Smiler, and Killer statues are eggs until their respective items are received.
    While eggs, the statues will not perform any of their functions.
    """
    display_name = "Idolsanity"

#class DungeonSet(OptionSet)
#    """
#    Which dungeons to include in logic. For specifics, see the Readme.
#    Excluding DIS has no effect as DIS is currently the only goal.
#    """
#    display_name = "Include Dungeons"
#    default = {"dead_end", "white_void", "beehole", "greedzone", "dis"}
#    valid_keys = ["dead_end", "white_void", "beehole", "greedzone", "dis"]

class DeadEnd(Toggle):
    """
    Adds all nine accessible empty chests from the voided ending sequence as checks.
    Also adds the "It's your brand" mural as a check.
    You can now reach this area from B225 without being VOID.
    """
    display_name = "Include Dead End"

class WhiteVoid(Choice):
    """
    When enabled, spawns five chests at the end of the White Void area after interacting with the statue.
    Regardless of this option, the statue no longer deletes your save file.
    Short: Limit the dungeon to a random 12 screens before the final room.
    Full: All 28 rooms are required to traverse before the final room.
    """
    display_name = "Include White Void"
    option_off = 0
    option_short = 1
    option_full = 2
    default = 0

class Beehole(Toggle):
    """
    When enabled, moves the "Slay the Lord of Sloth" check to the end of the Beehole dungeon.
    To access, you must first show Gor the Void Rod, and then find the entrance room (Normally past the secret exit on B144).
    Also includes the two chests in the entrance room, and adds two additional chests to the end of the area.
    """
    display_name = "Include Beehole"

class Greedzone(Toggle):
    """
    When enabled, includes the 15 chests at the end of Mon's Funhouse as checks.
    A set amount of Greed Coins are added as items and are required to access the dungeon.
    This will be revamped in v0.12.0
    """
    display_name = "Include Greedzone"

class Disdungeon(Choice):
    """
    How long the final dungeon, DIS, should be.
    Short chooses a random 12 rooms
    Full is the normal vanilla length.
    """
    display_name = "DIS Length"
    option_full = 0
    option_short = 1
    default = 0

class GreedCoinAmount(Range):
    """
    Sets the amount of Greed Coins in the pool.
    Only works if the Greed Zone is enabled. Valid range is 1-30.
    """
    display_name = "Greed Coin Amount"
    range_start = 1
    range_end = 30
    default = 15

class SkipCutscenes(Toggle):
    """
    When enabled, the final cutscene at the end of the game is skipped, stepping onto the elevator brings you
     instantly to controlling Lily in the final room.
    """
    display_name = "Skip Cutscenes"
    default = 1

@dataclass
class VoidStrangerOptions(PerGameCommonOptions):
    logiccomplexity: LogicComplexity
    idolsanity: Idolsanity
    shortcutsanity: Shortcutsanity
    deadend: DeadEnd
    whitevoid: WhiteVoid
    beehole: Beehole
    greedzone: Greedzone
    disdungeon: Disdungeon
    greedcoinamount: GreedCoinAmount
    skipcutscenes: SkipCutscenes