from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class Locustsanity(Toggle):
    """
    When enabled, Locust Idols are shuffled into the item pool and their chests are checks. Each chest capable of
    tripling its contents adds an item worth 3 locusts to the pool.
    """
    display_name = "Locustsanity"

class Brandsanity(Toggle):
    """
    When enabled, the ability to carve each lord's brand into rooms are shuffled into the item pool and
    the inspecting each mural depicting them gives a check.
    """
    display_name = "Brandsanity"

class ProgressiveBrands(Toggle):
    """
    When enabled, 9 progressive brands are added to the pool instead of specific ones for each domain. Each domain needs
    an additional brand to enter. No effect when brandsanity is disabled.
    """
    display_name = "Progressive Brands"

class Idolsanity(Toggle):
    """
    When enabled, the Lover, Smiler, and Killer Idols are eggs until their respective items are received, and
    once restored, talking to them with the void memory gives checks.
    """
    display_name = "Idolsanity"

class Shortcutsanity(Toggle):
    """
    When enabled, the ability to use each of Mon's shortcuts are shuffled into the item pool, and talking to them is a
    check.
    """
    display_name = "Shortcutsanity"

class ShortcutCheating(Range):
    """
    Determines how many of the shortcut hint locations from Mon will require the "Unlock Cheats" item in logic to reach.
    This starts from the final shortcut, so a value of 2 will make the final 2 shortcut hint locations require cheating
    for example. Since the first shortcut only needs 3 there is no need to cheat on this one.
    For reference the requirements are as follows: 3, 21, 49, 56, and 77. Has no effect if Shortcutsanity is disabled.
    """
    display_name = "Shortcut Cheating"
    range_start = 0
    range_end = 4
    default = 3

class GreedZone(Toggle):
    """
    When enabled, adds 15 items and locations, for the 15 chests at the end of a certain optional area accessible from
    B193. Entry is locked until all Greed Coins are collected. Only works if Locustsanity is enabled.
    """
    display_name = "Greed Zone"

class GreedCoinAmount(Range):
    """
    Sets the amount of Greed Coins in the pool. The minimum and default value is 15, the maximum is 83. Using values
    higher than 15 will remove normal locust idols from the pool to make room. Only works if the Greed Zone is enabled.
    """
    display_name = "Greed Coin Amount"
    range_start = 15
    range_end = 35
    default = 15

class SkipCutscenes(Toggle):
    """
    When enabled, the final cutscene at the end of the game is skipped, stepping onto the elevator brings you
    instantly to controlling Lily in the final room.
    """
    display_name = "Skip Cutscenes"

@dataclass
class VoidStrangerOptions(PerGameCommonOptions):
    locustsanity: Locustsanity
    brandsanity: Brandsanity
    progressivebrands: ProgressiveBrands
    idolsanity: Idolsanity
    shortcutsanity: Shortcutsanity
    shortcutcheating: ShortcutCheating
    greedzone: GreedZone
    greedcoinamount: GreedCoinAmount
    skipcutscenes: SkipCutscenes