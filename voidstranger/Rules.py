from typing import Dict, List

from BaseClasses import CollectionState

from . import VoidStrangerWorld
from .Constants import ItemNames, LocationNames
from ..generic.Rules import set_rule, forbid_item, add_rule


def set_rules(world: VoidStrangerWorld):

    # goal logic decision
    if world.options.brandsanity and world.options.idolsanity:
        world.goal_logic_mapping = goal_full_dis_logic
    elif world.options.brandsanity and not world.options.idolsanity:
        world.goal_logic_mapping = goal_brand_dis_logic
    elif not world.options.brandsanity and world.options.idolsanity:
        world.goal_logic_mapping = goal_idol_dis_logic
    elif not world.options.brandsanity and not world.options.idolsanity:
        world.goal_logic_mapping = goal_min_dis_logic

    # Completion condition.
    world.multiworld.completion_condition[world.player] = lambda state: goal_rule(state, world)

    if world.options.brandsanity:
        forbid_item(world.multiworld.get_location(LocationNames.mural_add, world.player),
                    ItemNames.endless_void_rod,world.player)

    set_rule(world.multiworld.get_location(LocationNames.endless_void_rod_chest, world.player),
             lambda state: state.has(ItemNames.lust_seal, world.player) and
                           state.has(ItemNames.sloth_seal, world.player) and
                           state.has(ItemNames.interface_manip, world.player))

    add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
             lambda state: state.has(ItemNames.void_memory, world.player))

    add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
             lambda state: state.has(ItemNames.void_wings, world.player) and
                           state.has(ItemNames.void_sword, world.player))

    add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
             lambda state: state.has(ItemNames.void_sword, world.player))

    if world.options.brandsanity:
        add_rule(world.multiworld.get_location(LocationNames.burden_chest1, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player))

        add_rule(world.multiworld.get_location(LocationNames.burden_chest2, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player))

        add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player))

        add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player) and
                               state.has(ItemNames.brand_gor, world.player))

        add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player))

        add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_eus, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_bee, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_mon, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_tan, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player) and
                               state.has(ItemNames.brand_gor, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player) and
                               state.has(ItemNames.brand_gor, world.player) and
                               state.has(ItemNames.brand_lev, world.player) and
                               state.has(ItemNames.void_memory, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                 lambda state: state.has(ItemNames.brand_add, world.player) and
                               state.has(ItemNames.brand_eus, world.player) and
                               state.has(ItemNames.brand_bee, world.player) and
                               state.has(ItemNames.brand_mon, world.player) and
                               state.has(ItemNames.brand_tan, world.player) and
                               state.has(ItemNames.brand_gor, world.player) and
                               state.has(ItemNames.brand_lev, world.player) and
                               state.has(ItemNames.brand_cif, world.player))


        if world.options.idolsanity:

            add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))


        if world.options.shortcutsanity:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

        if world.options.locustsanity:
            add_rule(world.multiworld.get_location(LocationNames.b032_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b033_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b034_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b035_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b036_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b037_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b040_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b041_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b043_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b048_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b050_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b060_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b064_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b065_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b069_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b074_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b076_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b077_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b078_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b080_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b081_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b088_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b091_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b094_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b115_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b116_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) and
                                   state.has(ItemNames.brand_lev, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) and
                                   state.has(ItemNames.brand_lev, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) and
                                   state.has(ItemNames.brand_lev, world.player))

    if world.options.idolsanity:
        add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
                 lambda state: state.has(ItemNames.enable_killer, world.player))

        add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
                 lambda state: state.has(ItemNames.enable_killer, world.player))

        add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
                 lambda state: state.has(ItemNames.enable_killer, world.player))

        add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and
                           state.has(ItemNames.enable_lover, world.player) and
                               (state.has(ItemNames.void_wings, world.player) or
                                state.has(ItemNames.endless_void_rod, world.player)))

        add_rule(world.multiworld.get_location(LocationNames.statue_smiler, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and
                               state.has(ItemNames.enable_smiler, world.player))

        add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and
                               state.has(ItemNames.enable_smiler, world.player))

        if world.options.brandsanity:
            add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

        if world.options.shortcutsanity:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

        if world.options.locustsanity:
            add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

#goal rules

#brands + idols randomized
goal_full_dis_logic: List[List[str]] = [[ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings,
                                         ItemNames.void_sword, ItemNames.endless_void_rod, ItemNames.enable_lover,
                                         ItemNames.enable_smiler, ItemNames.enable_killer, ItemNames.brand_add,
                                         ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.brand_tan,
                                         ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.brand_cif, ItemNames.brand_dis]]

#only brands randomized
goal_brand_dis_logic: List[List[str]] = [[ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings,
                                         ItemNames.void_sword, ItemNames.endless_void_rod, ItemNames.brand_add,
                                         ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.brand_tan,
                                         ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.brand_cif, ItemNames.brand_dis]]

#only idols randomized
goal_idol_dis_logic: List[List[str]] = [[ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings,
                                         ItemNames.void_sword, ItemNames.endless_void_rod, ItemNames.enable_lover,
                                         ItemNames.enable_smiler, ItemNames.enable_killer]]

#no extra randomization
goal_min_dis_logic: List[List[str]] = [[ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings,
                                         ItemNames.void_sword, ItemNames.endless_void_rod]]

def goal_rule(state: CollectionState, world: VoidStrangerWorld) -> bool:

    for possible_access in world.goal_logic_mapping:
        if state.has_all(possible_access, world.player):
            return True

    return False