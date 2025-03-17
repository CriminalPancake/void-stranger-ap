from typing import Dict, List

from BaseClasses import CollectionState

from . import VoidStrangerWorld
from .Constants import ItemNames, LocationNames
from ..generic.Rules import set_rule, forbid_item, add_rule


def set_rules(world: VoidStrangerWorld):
    # goal logic decision
    if world.options.brandsanity and world.options.idolsanity:
        if world.options.progressivebrands:
            world.multiworld.completion_condition[world.player] = \
                lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                                state.has(ItemNames.void_memory, world.player) and
                                state.has(ItemNames.void_wings, world.player) and
                                state.has(ItemNames.void_sword, world.player) and
                                state.has(ItemNames.endless_void_rod, world.player) and
                                state.has(ItemNames.enable_lover, world.player) and
                                state.has(ItemNames.enable_smiler, world.player) and
                                state.has(ItemNames.enable_killer, world.player) and
                                state.has(ItemNames.brand_prog, world.player, 9)))
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                                state.has(ItemNames.void_memory, world.player) and
                                state.has(ItemNames.void_wings, world.player) and
                                state.has(ItemNames.void_sword, world.player) and
                                state.has(ItemNames.endless_void_rod, world.player) and
                                state.has(ItemNames.enable_lover, world.player) and
                                state.has(ItemNames.enable_smiler, world.player) and
                                state.has(ItemNames.enable_killer, world.player) and
                                state.has(ItemNames.brand_add, world.player) and
                                state.has(ItemNames.brand_eus, world.player) and
                                state.has(ItemNames.brand_bee, world.player) and
                                state.has(ItemNames.brand_mon, world.player) and
                                state.has(ItemNames.brand_tan, world.player) and
                                state.has(ItemNames.brand_gor, world.player) and
                                state.has(ItemNames.brand_lev, world.player) and
                                state.has(ItemNames.brand_cif, world.player) and
                                state.has(ItemNames.brand_dis, world.player)))

    elif world.options.brandsanity and not world.options.idolsanity:
        if world.options.progressivebrands:
            world.multiworld.completion_condition[world.player] = \
                lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                                state.has(ItemNames.void_memory, world.player) and
                                state.has(ItemNames.void_wings, world.player) and
                                state.has(ItemNames.void_sword, world.player) and
                                state.has(ItemNames.endless_void_rod, world.player) and
                                state.has(ItemNames.brand_prog, world.player, 9)))
        else:
            world.multiworld.completion_condition[world.player] = \
                lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                                state.has(ItemNames.void_memory, world.player) and
                                state.has(ItemNames.void_wings, world.player) and
                                state.has(ItemNames.void_sword, world.player) and
                                state.has(ItemNames.endless_void_rod, world.player) and
                                state.has(ItemNames.brand_add, world.player) and
                                state.has(ItemNames.brand_eus, world.player) and
                                state.has(ItemNames.brand_bee, world.player) and
                                state.has(ItemNames.brand_mon, world.player) and
                                state.has(ItemNames.brand_tan, world.player) and
                                state.has(ItemNames.brand_gor, world.player) and
                                state.has(ItemNames.brand_lev, world.player) and
                                state.has(ItemNames.brand_cif, world.player) and
                                state.has(ItemNames.brand_dis, world.player)))

    elif not world.options.brandsanity and world.options.idolsanity:
        world.multiworld.completion_condition[world.player] = \
            lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                            state.has(ItemNames.void_memory, world.player) and
                            state.has(ItemNames.void_wings, world.player) and
                            state.has(ItemNames.void_sword, world.player) and
                            state.has(ItemNames.endless_void_rod, world.player) and
                            state.has(ItemNames.enable_lover, world.player) and
                            state.has(ItemNames.enable_smiler, world.player) and
                            state.has(ItemNames.enable_killer, world.player)))

    elif not world.options.brandsanity and not world.options.idolsanity:
        world.multiworld.completion_condition[world.player] = \
            lambda state: ((state.has(ItemNames.interface_manip, world.player) and
                            state.has(ItemNames.void_memory, world.player) and
                            state.has(ItemNames.void_wings, world.player) and
                            state.has(ItemNames.void_sword, world.player) and
                            state.has(ItemNames.endless_void_rod, world.player)))

    #Forbid item rules
    if world.options.brandsanity:
        forbid_item(world.multiworld.get_location(LocationNames.mural_add, world.player),
                    ItemNames.endless_void_rod,world.player)

    if world.options.locustsanity and world.options.greedzone:
        forbid_item(world.multiworld.get_location(LocationNames.m14_chest1, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m14_chest2, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m14_chest3, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest1, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest2, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest3, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest4, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest5, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest6, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest7, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest8, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest9, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest10, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest11, world.player), ItemNames.greed_coin,
                    world.player)
        forbid_item(world.multiworld.get_location(LocationNames.m15_chest12, world.player), ItemNames.greed_coin,
                    world.player)

    #base logic rules
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

    #base Greed Zone rules
    if world.options.greedzone and world.options.locustsanity:
        add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has(ItemNames.void_wings, world.player) and
                        state.has(ItemNames.void_sword, world.player))

    #brand rules, progressive or otherwise
    if world.options.brandsanity:

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest1, world.player),
                    lambda state: state.has(ItemNames.brand_prog, world.player, 1))
        else:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest1, world.player),
                    lambda state: state.has(ItemNames.brand_add, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest2, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 3))
        else:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest2, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 5))
        else:
            add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 6))
        else:
            add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 1))
        else:
            add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 4))
        else:
            add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_eus, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 1))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_eus, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_bee, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 2))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_bee, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_mon, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 3))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_mon, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_tan, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 4))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_tan, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 5))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 6))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) )

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 7) and
                                   state.has(ItemNames.void_memory, world.player))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) and
                                   state.has(ItemNames.brand_lev, world.player) and
                                   state.has(ItemNames.void_memory, world.player))

        if world.options.progressivebrands:
            add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                     lambda state: state.has(ItemNames.brand_prog, world.player, 8))
        else:
            add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                     lambda state: state.has(ItemNames.brand_add, world.player) and
                                   state.has(ItemNames.brand_eus, world.player) and
                                   state.has(ItemNames.brand_bee, world.player) and
                                   state.has(ItemNames.brand_mon, world.player) and
                                   state.has(ItemNames.brand_tan, world.player) and
                                   state.has(ItemNames.brand_gor, world.player) and
                                   state.has(ItemNames.brand_lev, world.player) and
                                   state.has(ItemNames.brand_cif, world.player))

        #brand rules for locations added by idolsanity
        if world.options.idolsanity:

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

        #brand rules for locations added by shortcutsanity
        if world.options.shortcutsanity:
            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 3))
            else:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))
        #brand rules for locations added by locustsanity
        if world.options.locustsanity:
            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b032_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b032_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b033_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b033_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b034_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b034_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b035_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b035_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b036_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b036_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b037_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b037_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b040_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b040_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b041_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b041_chest, world.player),
                        lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b043_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b043_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b048_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b048_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b050_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 1))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b050_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b060_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b060_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b064_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b064_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b065_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b065_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b069_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b069_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b074_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b074_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b076_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b076_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b077_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b077_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b078_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b078_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b080_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b080_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b081_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 2))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b081_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b088_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 3))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b088_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b091_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 3))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b091_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b094_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 3))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b094_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b115_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b115_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b116_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b116_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 4))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 5))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 6))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 7))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player) and
                                       state.has(ItemNames.brand_lev, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 7))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player) and
                                       state.has(ItemNames.brand_lev, world.player))

            if world.options.progressivebrands:
                add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
                         lambda state: state.has(ItemNames.brand_prog, world.player, 7))
            else:
                add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
                         lambda state: state.has(ItemNames.brand_add, world.player) and
                                       state.has(ItemNames.brand_eus, world.player) and
                                       state.has(ItemNames.brand_bee, world.player) and
                                       state.has(ItemNames.brand_mon, world.player) and
                                       state.has(ItemNames.brand_tan, world.player) and
                                       state.has(ItemNames.brand_gor, world.player) and
                                       state.has(ItemNames.brand_lev, world.player))
            #brand rules for locations added in the greed zone
            if world.options.greedzone:
                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))

                if world.options.progressivebrands:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                             lambda state: state.has(ItemNames.brand_prog, world.player, 6))
                else:
                    add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                             lambda state: state.has(ItemNames.brand_add, world.player) and
                                           state.has(ItemNames.brand_eus, world.player) and
                                           state.has(ItemNames.brand_bee, world.player) and
                                           state.has(ItemNames.brand_mon, world.player) and
                                           state.has(ItemNames.brand_tan, world.player) and
                                           state.has(ItemNames.brand_gor, world.player))
    #idol rules
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
        #idol rules for locations added by brandsanity
        if world.options.brandsanity:
            add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))
        #idol rules added by shortcutsanity
        if world.options.shortcutsanity:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                     lambda state: state.has(ItemNames.enable_killer, world.player))
        #idol rules for locations added by locustsanity
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
            #idol rules for locations added in the greedzone
            if world.options.greedzone:
                add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))

                add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                         lambda state: state.has(ItemNames.enable_killer, world.player))
    #shortcut rules, for locustsanity and cheating
    if world.options.shortcutsanity:

        if world.options.locustsanity:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut1, world.player),
                     lambda state: locust(state, world.player, 3))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                     lambda state: locust(state, world.player, 21))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                     lambda state: locust(state, world.player, 49))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                     lambda state: locust(state, world.player, 56))

            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                     lambda state: locust(state, world.player, 77))

        if world.options.shortcutcheating >= 4:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                     lambda state: state.has(ItemNames.interface_manip, world.player))

        if world.options.shortcutcheating >= 3:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                     lambda state: state.has(ItemNames.interface_manip, world.player))

        if world.options.shortcutcheating >= 2:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                     lambda state: state.has(ItemNames.interface_manip, world.player))

        if world.options.shortcutcheating >= 1:
            add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                     lambda state: state.has(ItemNames.interface_manip, world.player))

def locust(state: CollectionState, player: int, required: int) -> bool:
    return state.has("locusts", player, required)