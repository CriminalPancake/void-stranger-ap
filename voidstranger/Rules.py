from typing import Dict, List

from BaseClasses import CollectionState

from . import VoidStrangerWorld
from .Constants import ItemNames, LocationNames
from ..generic.Rules import set_rule, forbid_item


def set_rules(world: VoidStrangerWorld):
    #location rule logic
    #Praying for the day Rayze cleans this garbage up for me
    if world.options.brandsanity and world.options.idolsanity and world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_full_dis_logic
    elif world.options.brandsanity and world.options.idolsanity and not world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_no_locust_dis_logic
    elif world.options.brandsanity and not world.options.idolsanity and world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_no_idol_dis_logic
    elif world.options.brandsanity and not world.options.idolsanity and not world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_brand_shortcut_dis_logic
    elif not world.options.brandsanity and world.options.idolsanity and world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_no_brand_dis_logic
    elif world.options.brandsanity and world.options.idolsanity and world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_no_shortcut_dis_logic
    elif world.options.brandsanity and world.options.idolsanity and not world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_brand_idol_dis_logic
    elif world.options.brandsanity and not world.options.idolsanity and world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_brand_locust_dis_logic
    elif not world.options.brandsanity and world.options.idolsanity and not world.options.locustsanity and world.options.shortcutsanity:
        world.active_logic_mapping = location_idol_shortcut_dis_logic
    elif not world.options.brandsanity and world.options.idolsanity and world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_idol_locust_dis_logic
    elif world.options.brandsanity and not world.options.idolsanity and not world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_brand_dis_logic
    elif not world.options.brandsanity and world.options.idolsanity and not world.options.locustsanity and not world.options.shortcutsanity:
        world.active_logic_mapping = location_idol_dis_logic
    elif not world.options.brandsanity and not world.options.idolsanity:
        world.active_logic_mapping = location_min_dis_logic

    #greed zone logic
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

        if world.options.brandsanity:
            if world.options.idolsanity:
                #both rules
                set_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1, ItemNames.brand_add: 1,
                                                             ItemNames.brand_eus: 1, ItemNames.brand_bee: 1,
                                                             ItemNames.brand_mon: 1, ItemNames.brand_tan: 1,
                                                             ItemNames.brand_gor: 1}, world.player))

            #brand rules
            set_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))
            set_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                     lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                         ItemNames.brand_add: 1, ItemNames.brand_eus: 1, 
                                                         ItemNames.brand_bee: 1, ItemNames.brand_mon: 1,
                                                         ItemNames.brand_tan: 1, ItemNames.brand_gor: 1}, world.player))

        else:
            if world.options.idolsanity:
                #idol rules
                set_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
                set_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                         lambda state: state.has_all_counts({ItemNames.greed_coin: world.greed_coin_count,
                                                             ItemNames.enable_killer: 1}, world.player))
        #just coins rules
        set_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))
        set_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count))

    if world.options.brandsanity:
        forbid_item(world.multiworld.get_location(LocationNames.mural_add, world.player), ItemNames.endless_void_rod,
                world.player)

    for location in world.multiworld.get_locations(world.player):
        set_rule(location, lambda state, location=location: location_rule(state, world, location.name))

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

#location rule Dicts

#brands, idols, shortcuts, and locusts randomized
location_full_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.enable_killer, ItemNames.void_memory]],
    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.enable_killer]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer,
                               ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.enable_killer]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.brand_add,
                                  ItemNames.brand_eus, ItemNames.enable_lover, ItemNames.void_wings],
                                 [ItemNames.void_memory, ItemNames.brand_add,
                                  ItemNames.brand_eus, ItemNames.enable_lover, ItemNames.endless_void_rod]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.buy_shortcut2: [[ItemNames.brand_add]],
    LocationNames.buy_shortcut3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.buy_shortcut4: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.enable_killer]],
    LocationNames.buy_shortcut5: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer]],

    LocationNames.b032_chest: [[ItemNames.brand_add]],
    LocationNames.b033_chest: [[ItemNames.brand_add]],
    LocationNames.b034_chest: [[ItemNames.brand_add]],
    LocationNames.b035_chest: [[ItemNames.brand_add]],
    LocationNames.b036_chest: [[ItemNames.brand_add]],
    LocationNames.b037_chest: [[ItemNames.brand_add]],
    LocationNames.b040_chest: [[ItemNames.brand_add]],
    LocationNames.b041_chest: [[ItemNames.brand_add]],
    LocationNames.b043_chest: [[ItemNames.brand_add]],
    LocationNames.b048_chest: [[ItemNames.brand_add]],
    LocationNames.b050_chest: [[ItemNames.brand_add]],
    LocationNames.b060_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b064_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b065_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b069_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b074_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b076_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b077_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b078_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b080_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b081_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b088_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b091_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b094_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b115_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b116_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b118_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b122_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b123_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b127_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b133_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b135_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b144_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b145_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b151_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b159_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b160_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b160_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b166_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b171_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b173_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b176_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b177_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b179_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b180_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b189_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b191_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest3: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest4: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b200_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b209_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b210_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]]
}

#3 enabled
#brands, idols, and shortcuts randomized
location_no_locust_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.enable_killer]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer,
                               ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.enable_killer]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.brand_add,
                                  ItemNames.brand_eus, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.buy_shortcut2: [[ItemNames.brand_add]],
    LocationNames.buy_shortcut3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.buy_shortcut4: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.enable_killer]],
    LocationNames.buy_shortcut5: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer]]
}

#brands, locusts, and shortcuts randomized
location_no_idol_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                 ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],

    LocationNames.buy_shortcut2: [[ItemNames.brand_add]],
    LocationNames.buy_shortcut3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.buy_shortcut4: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.buy_shortcut5: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.brand_gor]],

    LocationNames.b032_chest: [[ItemNames.brand_add]],
    LocationNames.b033_chest: [[ItemNames.brand_add]],
    LocationNames.b034_chest: [[ItemNames.brand_add]],
    LocationNames.b035_chest: [[ItemNames.brand_add]],
    LocationNames.b036_chest: [[ItemNames.brand_add]],
    LocationNames.b037_chest: [[ItemNames.brand_add]],
    LocationNames.b040_chest: [[ItemNames.brand_add]],
    LocationNames.b041_chest: [[ItemNames.brand_add]],
    LocationNames.b043_chest: [[ItemNames.brand_add]],
    LocationNames.b048_chest: [[ItemNames.brand_add]],
    LocationNames.b050_chest: [[ItemNames.brand_add]],
    LocationNames.b060_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b064_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b065_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b069_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b074_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b076_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b077_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b078_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b080_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b081_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b088_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b091_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b094_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b115_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b116_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b118_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b122_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b123_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b127_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b133_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b135_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b144_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b145_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b151_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b159_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b160_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b160_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b166_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan]],
    LocationNames.b171_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b173_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b176_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b177_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b179_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b180_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b189_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b191_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest3: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest4: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b200_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b209_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b210_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, 
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]]
}

#idols, locusts, and shortcuts randomized
location_no_brand_dis_logic: Dict[str, List[List[str]]] = {

    LocationNames.burden_chest3: [[ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.enable_killer, ItemNames.void_memory]],

LocationNames.lust_slain: [[ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.buy_shortcut4: [[ItemNames.enable_killer]],
    LocationNames.buy_shortcut5: [[ItemNames.enable_killer]],

    LocationNames.b118_chest: [[ItemNames.enable_killer]],
    LocationNames.b122_chest: [[ItemNames.enable_killer]],
    LocationNames.b123_chest: [[ItemNames.enable_killer]],
    LocationNames.b127_chest: [[ItemNames.enable_killer]],
    LocationNames.b133_chest: [[ItemNames.enable_killer]],
    LocationNames.b135_chest: [[ItemNames.enable_killer]],
    LocationNames.b144_chest: [[ItemNames.enable_killer]],
    LocationNames.b145_chest: [[ItemNames.enable_killer]],
    LocationNames.b151_chest: [[ItemNames.enable_killer]],
    LocationNames.b159_chest: [[ItemNames.enable_killer]],
    LocationNames.b160_chest1: [[ItemNames.enable_killer]],
    LocationNames.b160_chest2: [[ItemNames.enable_killer]],
    LocationNames.b166_chest: [[ItemNames.enable_killer]],
    LocationNames.b171_chest: [[ItemNames.enable_killer]],
    LocationNames.b173_chest: [[ItemNames.enable_killer]],
    LocationNames.b176_chest: [[ItemNames.enable_killer]],
    LocationNames.b177_chest: [[ItemNames.enable_killer]],
    LocationNames.b178_chest1: [[ItemNames.enable_killer]],
    LocationNames.b178_chest2: [[ItemNames.enable_killer]],
    LocationNames.b179_chest: [[ItemNames.enable_killer]],
    LocationNames.b180_chest: [[ItemNames.enable_killer]],
    LocationNames.b189_chest: [[ItemNames.enable_killer]],
    LocationNames.b191_chest: [[ItemNames.enable_killer]],
    LocationNames.b195_chest1: [[ItemNames.enable_killer]],
    LocationNames.b195_chest2: [[ItemNames.enable_killer]],
    LocationNames.b195_chest3: [[ItemNames.enable_killer]],
    LocationNames.b195_chest4: [[ItemNames.enable_killer]],
    LocationNames.b200_chest: [[ItemNames.enable_killer]],
    LocationNames.b209_chest: [[ItemNames.enable_killer]],
    LocationNames.b210_chest: [[ItemNames.enable_killer]]
}

#brands, idols, and locusts randomized
location_no_shortcut_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.enable_killer]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer,
                               ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.enable_killer]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.brand_add,
                                  ItemNames.brand_eus, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.b032_chest: [[ItemNames.brand_add]],
    LocationNames.b033_chest: [[ItemNames.brand_add]],
    LocationNames.b034_chest: [[ItemNames.brand_add]],
    LocationNames.b035_chest: [[ItemNames.brand_add]],
    LocationNames.b036_chest: [[ItemNames.brand_add]],
    LocationNames.b037_chest: [[ItemNames.brand_add]],
    LocationNames.b040_chest: [[ItemNames.brand_add]],
    LocationNames.b041_chest: [[ItemNames.brand_add]],
    LocationNames.b043_chest: [[ItemNames.brand_add]],
    LocationNames.b048_chest: [[ItemNames.brand_add]],
    LocationNames.b050_chest: [[ItemNames.brand_add]],
    LocationNames.b060_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b064_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b065_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b069_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b074_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b076_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b077_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b078_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b080_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b081_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b088_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b091_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b094_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b115_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b116_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b118_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b122_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b123_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b127_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b133_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b135_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer]],
    LocationNames.b144_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b145_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b151_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b159_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b160_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b160_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b166_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan]],
    LocationNames.b171_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b173_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b176_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b177_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b179_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b180_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b189_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b191_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest3: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest4: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b200_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b209_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b210_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon, ItemNames.enable_killer,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]]
}

#2 enabled
#brands + shortcuts randomized
location_brand_shortcut_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],

    LocationNames.buy_shortcut2: [[ItemNames.brand_add]],
    LocationNames.buy_shortcut3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.buy_shortcut4: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.buy_shortcut5: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.brand_gor]]
}

#brands + idols randomized
location_brand_idol_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.enable_killer]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.enable_killer]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.enable_killer,
                               ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.enable_killer]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.brand_add,
                                  ItemNames.brand_eus, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan, ItemNames.enable_killer, ItemNames.void_memory]]
}

#brands + locusts randomized
location_brand_locust_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                                   ItemNames.brand_tan]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                          ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.void_sword]],

    LocationNames.mural_bee: [[ItemNames.brand_add]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],

    LocationNames.b032_chest: [[ItemNames.brand_add]],
    LocationNames.b033_chest: [[ItemNames.brand_add]],
    LocationNames.b034_chest: [[ItemNames.brand_add]],
    LocationNames.b035_chest: [[ItemNames.brand_add]],
    LocationNames.b036_chest: [[ItemNames.brand_add]],
    LocationNames.b037_chest: [[ItemNames.brand_add]],
    LocationNames.b040_chest: [[ItemNames.brand_add]],
    LocationNames.b041_chest: [[ItemNames.brand_add]],
    LocationNames.b043_chest: [[ItemNames.brand_add]],
    LocationNames.b048_chest: [[ItemNames.brand_add]],
    LocationNames.b050_chest: [[ItemNames.brand_add]],
    LocationNames.b060_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b064_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b065_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b069_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b074_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b076_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b077_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b078_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b080_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b081_chest: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.b088_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b091_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b094_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.b115_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b116_chest: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b118_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b122_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b123_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b127_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b133_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b135_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.b144_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b145_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b151_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b159_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b160_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b160_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b166_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan]],
    LocationNames.b171_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b173_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b176_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b177_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b178_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b179_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b180_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b189_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b191_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest1: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest2: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest3: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b195_chest4: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.b200_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b209_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]],
    LocationNames.b210_chest: [
        [ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
         ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev]]
}

#idols + shortcuts randomized
location_idol_shortcut_dis_logic: Dict[str, List[List[str]]] = {

    LocationNames.burden_chest3: [[ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.buy_shortcut4: [[ItemNames.enable_killer]],
    LocationNames.buy_shortcut5: [[ItemNames.enable_killer]]
}

#idols + locusts randomized
location_idol_locust_dis_logic: Dict[str, List[List[str]]] = {

    LocationNames.burden_chest3: [[ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.b118_chest: [[ItemNames.enable_killer]],
    LocationNames.b122_chest: [[ItemNames.enable_killer]],
    LocationNames.b123_chest: [[ItemNames.enable_killer]],
    LocationNames.b127_chest: [[ItemNames.enable_killer]],
    LocationNames.b133_chest: [[ItemNames.enable_killer]],
    LocationNames.b135_chest: [[ItemNames.enable_killer]],
    LocationNames.b144_chest: [[ItemNames.enable_killer]],
    LocationNames.b145_chest: [[ItemNames.enable_killer]],
    LocationNames.b151_chest: [[ItemNames.enable_killer]],
    LocationNames.b159_chest: [[ItemNames.enable_killer]],
    LocationNames.b160_chest1: [[ItemNames.enable_killer]],
    LocationNames.b160_chest2: [[ItemNames.enable_killer]],
    LocationNames.b166_chest: [[ItemNames.enable_killer]],
    LocationNames.b171_chest: [[ItemNames.enable_killer]],
    LocationNames.b173_chest: [[ItemNames.enable_killer]],
    LocationNames.b176_chest: [[ItemNames.enable_killer]],
    LocationNames.b177_chest: [[ItemNames.enable_killer]],
    LocationNames.b178_chest1: [[ItemNames.enable_killer]],
    LocationNames.b178_chest2: [[ItemNames.enable_killer]],
    LocationNames.b179_chest: [[ItemNames.enable_killer]],
    LocationNames.b180_chest: [[ItemNames.enable_killer]],
    LocationNames.b189_chest: [[ItemNames.enable_killer]],
    LocationNames.b191_chest: [[ItemNames.enable_killer]],
    LocationNames.b195_chest1: [[ItemNames.enable_killer]],
    LocationNames.b195_chest2: [[ItemNames.enable_killer]],
    LocationNames.b195_chest3: [[ItemNames.enable_killer]],
    LocationNames.b195_chest4: [[ItemNames.enable_killer]],
    LocationNames.b200_chest: [[ItemNames.enable_killer]],
    LocationNames.b209_chest: [[ItemNames.enable_killer]],
    LocationNames.b210_chest: [[ItemNames.enable_killer]]
}

#1 enabled
location_brand_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.burden_chest1: [[ItemNames.brand_add]],
    LocationNames.burden_chest2: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.burden_chest3: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_tan]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee,
                                          ItemNames.brand_mon, ItemNames.brand_tan, ItemNames.brand_gor,
                                           ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.brand_add, ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.void_sword]],

    LocationNames.mural_eus: [[ItemNames.brand_add]],
    LocationNames.mural_bee: [[ItemNames.brand_add, ItemNames.brand_eus]],
    LocationNames.mural_mon: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee]],
    LocationNames.mural_tan: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon]],
    LocationNames.mural_gor: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan]],
    LocationNames.mural_lev: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor]],
    LocationNames.mural_cif: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev,
                               ItemNames.void_memory]],
    LocationNames.mural_dis: [[ItemNames.brand_add, ItemNames.brand_eus, ItemNames.brand_bee, ItemNames.brand_mon,
                               ItemNames.brand_tan, ItemNames.brand_gor, ItemNames.brand_lev, ItemNames.brand_cif]]
}

location_idol_dis_logic: Dict[str, List[List[str]]] = {

    LocationNames.burden_chest3: [[ItemNames.enable_killer]],

    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.enable_killer, ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.enable_killer, ItemNames.void_sword]],

    LocationNames.statue_lover: [[ItemNames.void_memory, ItemNames.enable_lover]],
    LocationNames.statue_smiler: [[ItemNames.void_memory, ItemNames.enable_smiler]],
    LocationNames.statue_killer: [[ItemNames.enable_killer, ItemNames.void_memory]]
}

#0 enabled
#no extra randomization, or just locusts and/or shortcuts randomized
location_min_dis_logic: Dict[str, List[List[str]]] = {
    LocationNames.endless_void_rod_chest: [[ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip]],
    LocationNames.interface_manip_hint: [[ItemNames.void_memory]],

    LocationNames.lust_slain: [[ItemNames.void_wings, ItemNames.void_sword]],
    LocationNames.sloth_slain: [[ItemNames.void_sword]],
}

def location_rule(state: CollectionState, world: VoidStrangerWorld, loc: str) -> bool:
    if loc not in world.active_logic_mapping:
        return True

    for possible_access in world.active_logic_mapping[loc]:
        if state.has_all(possible_access, world.player):
            return True

    return False

def goal_rule(state: CollectionState, world: VoidStrangerWorld) -> bool:

    for possible_access in world.goal_logic_mapping:
        if state.has_all(possible_access, world.player):
            return True

    return False