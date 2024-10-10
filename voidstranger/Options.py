from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class Locustsanity(Toggle):
    """
    When enabled, Locust Idols are shuffled into the item pool and their chests award checks. Each chest capable of
    tripling its contents adds an item worth 3 locusts to the pool. Using an atoner no longer sets your count to 0 but instead to
    the number received
    """
    display_name = "Locustsanity"

class Brandsanity(Toggle):
    """
    When enabled, the ability to carve each lord's brand into rooms are shuffled into the item pool and
    the inspecting the murals depicting them awards a check
    """
    display_name = "Brandsanity"

class Idolsanity(Toggle):
    """
    When enabled, the Lover, Smiler, and Killer Idols are eggs until their respective items are received, and
    once restored, talking to them with the void memory awards a check
    """
    display_name = "Idolsanity"

class Shortcutsanity(Toggle):
    """
    When enabled, the ability to use each of Mon's shortcuts are shuffled into the item pool. The locust requirements
    for Mon to appear are removed, and talking to them awards a check
    """
    display_name = "Shortcutsanity"

@dataclass
class VoidStrangerOptions(PerGameCommonOptions):
    locustsanity: Locustsanity
    brandsanity: Brandsanity
    idolsanity: Idolsanity
    shortcutsanity: Shortcutsanity