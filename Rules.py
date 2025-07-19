from typing import Dict, List

from BaseClasses import CollectionState

from . import VoidStrangerWorld
from .Constants import ItemNames, LocationNames
from ..generic.Rules import set_rule, forbid_item, add_rule


def has_brand(world: VoidStrangerWorld, state: CollectionState, brand: str) -> bool:
    if world.options.brandsanity:
        if brand == "add":
            return state.has_any_count({ItemNames.brand_add: 1, ItemNames.brand_prog: 1}, world.player)
        elif brand == "eus":
            return state.has_any_count({ItemNames.brand_eus: 1, ItemNames.brand_prog: 2}, world.player)
        elif brand == "bee":
            return state.has_any_count({ItemNames.brand_bee: 1, ItemNames.brand_prog: 3}, world.player)
        elif brand == "mon":
            return state.has_any_count({ItemNames.brand_mon: 1, ItemNames.brand_prog: 4}, world.player)
        elif brand == "tan":
            return state.has_any_count({ItemNames.brand_tan: 1, ItemNames.brand_prog: 5}, world.player)
        elif brand == "gor":
            return state.has_any_count({ItemNames.brand_gor: 1, ItemNames.brand_prog: 6}, world.player)
        elif brand == "lev":
            return state.has_any_count({ItemNames.brand_lev: 1, ItemNames.brand_prog: 7}, world.player)
        elif brand == "cif":
            return state.has_any_count({ItemNames.brand_cif: 1, ItemNames.brand_prog: 8}, world.player)
        elif brand == "dis":
            return state.has_any_count({ItemNames.brand_dis: 1, ItemNames.brand_prog: 9}, world.player)
    else:
        return True

def has_idol(world: VoidStrangerWorld, state: CollectionState, statue: str) -> bool:
    if world.options.idolsanity:
        if statue == "lover":
            return state.has(ItemNames.enable_lover, world.player)
        elif statue == "smiler":
            return state.has(ItemNames.enable_smiler, world.player)
        elif statue == "killer":
            return state.has(ItemNames.enable_killer, world.player)
        elif statue == "watcher":
            return state.has(ItemNames.enable_watcher, world.player)

    else:
        return True
        
def has_locust_count(world: VoidStrangerWorld, state: CollectionState, required: int) -> bool:
    if world.options.locustsanity:
        return state.has("locusts", world.player, required)
    else:
        return True
        
def check_shortcut_cheating(world: VoidStrangerWorld, state: CollectionState, shortcut: int, required: int) -> bool:
    if world.options.shortcutcheating >= shortcut and state.has(ItemNames.interface_manip, world.player):
        return True
    else:
        return has_locust_count(world, state, required)
        
def set_rules(world: VoidStrangerWorld):
    # goal logic decision
    world.multiworld.completion_condition[world.player] = \
        lambda state: ((state.has_all({ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings, ItemNames.void_sword, ItemNames.endless_void_rod}, world.player) and
                        has_idol(world, state, "killer") and
                        has_idol(world, state, "lover") and
                        has_idol(world, state, "smiler") and
                        has_brand(world, state, "add") and
                        has_brand(world, state, "eus") and
                        has_brand(world, state, "bee") and
                        has_brand(world, state, "mon") and
                        has_brand(world, state, "tan") and
                        has_brand(world, state, "gor") and
                        has_brand(world, state, "lev") and
                        has_brand(world, state, "cif") and
                        has_brand(world, state, "dis")))

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

    #base Greed Zone rules
    if world.options.greedzone and world.options.locustsanity:
        add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))

    #base locations
    set_rule(world.multiworld.get_location(LocationNames.endless_void_rod_chest, world.player),
             lambda state: state.has(ItemNames.lust_seal, world.player) and
                           state.has(ItemNames.sloth_seal, world.player) and
                           state.has(ItemNames.interface_manip, world.player))

    add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
             lambda state: state.has(ItemNames.void_memory, world.player))

    add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
             lambda state: state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                           has_brand(world, state, "add"))

    add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
             lambda state: state.has(ItemNames.void_sword, world.player) and
                           has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_idol(world, state, "killer"))
             
             
    add_rule(world.multiworld.get_location(LocationNames.burden_chest1, world.player),
             lambda state: has_brand(world, state, "add"))
    
    add_rule(world.multiworld.get_location(LocationNames.burden_chest2, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee"))
    
    add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_idol(world, state, "killer"))
    
    add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

    #brandsanity locations
    if world.options.brandsanity:
        add_rule(world.multiworld.get_location(LocationNames.mural_eus, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.mural_bee, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.mural_mon, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee"))

        add_rule(world.multiworld.get_location(LocationNames.mural_tan, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon"))

        add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_brand(world, state, "lev") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_brand(world, state, "lev") and
                               has_brand(world, state, "cif") and
                               has_idol(world, state, "killer"))

    #idolsanity locations
    if world.options.idolsanity:
        add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and (
                                  state.has(ItemNames.void_wings, world.player) or
                                  state.has(ItemNames.endless_void_rod, world.player)) and
                               has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_idol(world, state, "lover"))

        add_rule(world.multiworld.get_location(LocationNames.statue_smiler, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and
                               has_idol(world, state, "smiler"))
    
        add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                 lambda state: state.has(ItemNames.void_memory, world.player) and
                               has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

    #shortcutsanity locations
    if world.options.shortcutsanity:
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut1, world.player),
                 lambda state: check_shortcut_cheating(world, state, 5, 3))
                 
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                 lambda state: has_brand(world, state, "add") and
                               check_shortcut_cheating(world, state, 4, 21))
        
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               check_shortcut_cheating(world, state, 3, 49))

        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer") and
                               check_shortcut_cheating(world, state, 2, 56))
    
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer") and
                               check_shortcut_cheating(world, state, 1, 77))
        
    #locustsanity locations
    if world.options.locustsanity:
        add_rule(world.multiworld.get_location(LocationNames.b032_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b033_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b034_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b035_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b036_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b037_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b040_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b041_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b043_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b048_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b050_chest, world.player),
                 lambda state: has_brand(world, state, "add"))

        add_rule(world.multiworld.get_location(LocationNames.b060_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b064_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b065_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b069_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b074_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b076_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b077_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b078_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b080_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b081_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus"))

        add_rule(world.multiworld.get_location(LocationNames.b088_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee"))

        add_rule(world.multiworld.get_location(LocationNames.b091_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee"))

        add_rule(world.multiworld.get_location(LocationNames.b094_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee"))

        add_rule(world.multiworld.get_location(LocationNames.b115_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon"))

        add_rule(world.multiworld.get_location(LocationNames.b116_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon"))

        add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_brand(world, state, "lev") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_brand(world, state, "lev") and
                               has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
                 lambda state: has_brand(world, state, "add") and
                               has_brand(world, state, "eus") and
                               has_brand(world, state, "bee") and
                               has_brand(world, state, "mon") and
                               has_brand(world, state, "tan") and
                               has_brand(world, state, "gor") and
                               has_brand(world, state, "lev") and
                               has_idol(world, state, "killer"))
                               
    #greed zone locations
    if world.options.greedzone:
        add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))

        add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
             lambda state: has_brand(world, state, "add") and
                           has_brand(world, state, "eus") and
                           has_brand(world, state, "bee") and
                           has_brand(world, state, "mon") and
                           has_brand(world, state, "tan") and
                           has_brand(world, state, "gor") and
                           has_idol(world, state, "killer"))