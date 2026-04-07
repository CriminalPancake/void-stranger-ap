from typing import Dict, List

from BaseClasses import CollectionState

from . import VoidStrangerWorld
from .Constants import ItemNames, LocationNames
from ..generic.Rules import set_rule, forbid_item, add_rule

# checks if a floor exists
# currently unused
def floor_exists(world: VoidStrangerWorld, floor) -> bool:
    if floor in world.vs_brane_list:
        return True
    else:
        return False

# high-level: runs the pathfinder if it's stale
# checks if a floor was tagged as accessible
def can_access_floor(world: VoidStrangerWorld, state: CollectionState, floor: str) -> bool:
    if state.vs_stale_pathfinding[world.player]:
        world.calculate_accessibility(state)
    return state.vs_brane_accessibility[world.player][floor]["Accessible"]

# high-level: runs the pathfinder if it's stale
# checks if a floor was tagged as accessible and also has a certain locust score or better
def can_access_floor_with_locusts(world: VoidStrangerWorld, state: CollectionState, floor: str, locust_count: int) -> bool:
    if can_access_floor(world, state, floor):
        if state.vs_brane_accessibility[world.player][floor]["Locust_Score"] >= locust_count:
            return True
    else:
        return False

# high-level: runs the pathfinder if it's stale
# checks if any floors are accessible on a pre-generated list of floors that contain the specified statue and if that statue is reachable
def can_access_idol(world: VoidStrangerWorld, state: CollectionState, statue: str) -> bool:
    if state.vs_stale_pathfinding[world.player]:
        world.calculate_accessibility(state)
    if state.has(ItemNames.void_memory, world.player) and has_idol(world, state, statue): #remove this check if we change how idol locations work
        for floor in world.vs_statue_floors[statue]:
            if can_access_floor(world, state, floor) and check_item_tuples(world, state, world.vs_brane_list[floor]["Statues"][statue]):
                return True
    return False

# checks lists of item combinations and returns true if any of the combinations is collected
# item tuple format: [[(item_category,item),(other item tuple)],[other valid item combination]]
def check_item_tuples(world: VoidStrangerWorld, state: CollectionState, item_groups) -> bool:
    for item_list in item_groups:
        result = True
        for item_tuple in item_list:
            result &= has_item_by_type(world, state, item_tuple[0], item_tuple[1])
        if result:
            return True
    return False
        
# generic item checking function
# allows for item tuples with different types of "item" fields
# add "access" type which checks CanAccessFloor?
def has_item_by_type(world: VoidStrangerWorld, state: CollectionState, type: str, item: str) -> bool:
    if type == "brand":
        return has_brand(world, state, item)
    elif type == "idol":
        return has_idol(world, state, item)
    elif type == "shortcut":
        return has_shortcut(world, state, item)
    elif type == "item":
        return state.has(item, world.player)

# checks if brandsanity is on, and if so, whether the specified brand is collected
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

# checks if idolsanity is on, and if so, whether the specified statue is collected
def has_idol(world: VoidStrangerWorld, state: CollectionState, statue: str) -> bool:
    if world.options.idolsanity:
        if statue == "lover":
            return state.has(ItemNames.enable_lover, world.player)
        elif statue == "smiler":
            return state.has(ItemNames.enable_smiler, world.player)
        elif statue == "greeder":
            #unimplemented
            #return state.has(ItemNames.enable_greeder, world.player)
            return True
        elif statue == "killer":
            return state.has(ItemNames.enable_killer, world.player)
        elif statue == "slower":
            #unimplemented
            #return state.has(ItemNames.enable_slower, world.player)
            return True
        elif statue == "watcher":
            #unimplemented
            #return state.has(ItemNames.enable_watcher, world.player)
            return True
    else:
        return True

# checks if shortcutsanity is on, and if so, whether the specified shortcut is collected
def has_shortcut(world: VoidStrangerWorld, state: CollectionState, shortcut: str) -> bool:
    if world.options.shortcutsanity:
        if shortcut == "mon1":
            return state.has(ItemNames.shortcut1, world.player)
        elif shortcut == "mon2":
            return state.has(ItemNames.shortcut2, world.player)
        elif shortcut == "mon3":
            return state.has(ItemNames.shortcut3, world.player)
        elif shortcut == "mon4":
            return state.has(ItemNames.shortcut4, world.player)
        elif shortcut == "mon5":
            return state.has(ItemNames.shortcut5, world.player)
    else:
        return True

# processes shortcutcheating option
def check_shortcut_cheating(world: VoidStrangerWorld, state: CollectionState, shortcut: int) -> bool:
    if world.options.shortcutcheating >= shortcut and not state.has(ItemNames.interface_manip, world.player):
        return False
    else:
        return True
        
def set_rules(world: VoidStrangerWorld):
    # goal logic decision
    world.multiworld.completion_condition[world.player] = \
        lambda state: ((state.has_all({ItemNames.interface_manip, ItemNames.void_memory, ItemNames.void_wings, ItemNames.void_sword, ItemNames.endless_void_rod}, world.player) and
                        can_access_floor(world, state, "dis_entrance") and
                        has_idol(world, state, "lover") and has_idol(world, state, "smiler") and has_idol(world, state, "greeder") and has_idol(world, state, "killer") and has_idol(world, state, "watcher")))

    #Forbid item rules
    if world.options.brandsanity:
        forbid_item(world.multiworld.get_location(LocationNames.mural_add, world.player),
                    ItemNames.endless_void_rod,world.player)

    if world.options.greedzone:
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

    #base locations
    set_rule(world.multiworld.get_location(LocationNames.endless_void_rod_chest, world.player),
             lambda state: can_access_floor(world, state, "B028") and # change floor to B000 after UI manip added
                           state.has_all({ItemNames.lust_seal, ItemNames.sloth_seal, ItemNames.interface_manip}, world.player))

    add_rule(world.multiworld.get_location(LocationNames.lust_slain, world.player),
             lambda state: can_access_floor(world, state, "B030") and state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player))

    add_rule(world.multiworld.get_location(LocationNames.sloth_slain, world.player),
             lambda state: can_access_floor(world, state, "B143") and state.has(ItemNames.void_sword, world.player))
             
    add_rule(world.multiworld.get_location(LocationNames.burden_chest1, world.player),
             lambda state: can_access_floor(world, state, "room_add"))
    
    add_rule(world.multiworld.get_location(LocationNames.burden_chest2, world.player),
             lambda state: can_access_floor(world, state, "room_bee"))
    
    add_rule(world.multiworld.get_location(LocationNames.burden_chest3, world.player),
             lambda state: can_access_floor(world, state, "room_tan") and state.has(ItemNames.void_sword, world.player))
    
    add_rule(world.multiworld.get_location(LocationNames.interface_manip_hint, world.player),
             lambda state: can_access_floor(world, state, "room_gor") and state.has(ItemNames.void_memory, world.player))

    #brandsanity locations
    if world.options.brandsanity:
        add_rule(world.multiworld.get_location(LocationNames.mural_add, world.player),
                 lambda state: can_access_floor(world, state, "B001"))
                 
        add_rule(world.multiworld.get_location(LocationNames.mural_eus, world.player),
                 lambda state: can_access_floor(world, state, "B029"))

        add_rule(world.multiworld.get_location(LocationNames.mural_bee, world.player),
                 lambda state: can_access_floor(world, state, "B057"))

        add_rule(world.multiworld.get_location(LocationNames.mural_mon, world.player),
                 lambda state: can_access_floor(world, state, "B085"))

        add_rule(world.multiworld.get_location(LocationNames.mural_tan, world.player),
                 lambda state: can_access_floor(world, state, "B113"))

        add_rule(world.multiworld.get_location(LocationNames.mural_gor, world.player),
                 lambda state: can_access_floor(world, state, "B141"))

        add_rule(world.multiworld.get_location(LocationNames.mural_lev, world.player),
                 lambda state: can_access_floor(world, state, "B169"))

        add_rule(world.multiworld.get_location(LocationNames.mural_cif, world.player),
                 lambda state: can_access_floor(world, state, "B197") and state.has(ItemNames.void_memory, world.player))

        add_rule(world.multiworld.get_location(LocationNames.mural_dis, world.player),
                 lambda state: can_access_floor(world, state, "B225"))

    #idolsanity locations
    if world.options.idolsanity:
        add_rule(world.multiworld.get_location(LocationNames.statue_lover, world.player),
                 lambda state: can_access_idol(world, state, "lover"))

        add_rule(world.multiworld.get_location(LocationNames.statue_smiler, world.player),
                 lambda state: can_access_idol(world, state, "smiler"))
    
        add_rule(world.multiworld.get_location(LocationNames.statue_killer, world.player),
                 lambda state: can_access_idol(world, state, "killer"))

    #shortcutsanity locations
    if world.options.shortcutsanity:
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut1, world.player),
                 lambda state: can_access_floor_with_locusts(world, state, "B004", 3) and check_shortcut_cheating(world, state, 5))
                 
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut2, world.player),
                 lambda state: can_access_floor_with_locusts(world, state, "B044", 21) and check_shortcut_cheating(world, state, 4))
        
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut3, world.player),
                 lambda state: can_access_floor_with_locusts(world, state, "B086", 49) and check_shortcut_cheating(world, state, 3))

        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut4, world.player),
                 lambda state: can_access_floor_with_locusts(world, state, "B124", 56) and check_shortcut_cheating(world, state, 2))
    
        add_rule(world.multiworld.get_location(LocationNames.buy_shortcut5, world.player),
                 lambda state: can_access_floor_with_locusts(world, state, "B196", 77) and check_shortcut_cheating(world, state, 1))
        
    #locust chest locations
    add_rule(world.multiworld.get_location(LocationNames.b032_chest, world.player),
             lambda state: can_access_floor(world, state, "B032"))

    add_rule(world.multiworld.get_location(LocationNames.b033_chest, world.player),
             lambda state: can_access_floor(world, state, "B033"))

    add_rule(world.multiworld.get_location(LocationNames.b034_chest, world.player),
             lambda state: can_access_floor(world, state, "B034"))

    add_rule(world.multiworld.get_location(LocationNames.b035_chest, world.player),
             lambda state: can_access_floor(world, state, "B035"))

    add_rule(world.multiworld.get_location(LocationNames.b036_chest, world.player),
             lambda state: can_access_floor(world, state, "B036"))

    add_rule(world.multiworld.get_location(LocationNames.b037_chest, world.player),
             lambda state: can_access_floor(world, state, "B037"))

    add_rule(world.multiworld.get_location(LocationNames.b040_chest, world.player),
             lambda state: can_access_floor(world, state, "B040"))

    add_rule(world.multiworld.get_location(LocationNames.b041_chest, world.player),
             lambda state: can_access_floor(world, state, "B041"))

    add_rule(world.multiworld.get_location(LocationNames.b043_chest, world.player),
             lambda state: can_access_floor(world, state, "B043"))

    add_rule(world.multiworld.get_location(LocationNames.b048_chest, world.player),
             lambda state: can_access_floor(world, state, "B048"))
             
    add_rule(world.multiworld.get_location(LocationNames.b050_chest, world.player),
             lambda state: can_access_floor(world, state, "B050"))
             
    add_rule(world.multiworld.get_location(LocationNames.b060_chest, world.player),
             lambda state: can_access_floor(world, state, "B060"))

    add_rule(world.multiworld.get_location(LocationNames.b064_chest, world.player),
             lambda state: can_access_floor(world, state, "B064"))

    add_rule(world.multiworld.get_location(LocationNames.b065_chest, world.player),
             lambda state: can_access_floor(world, state, "B065"))

    add_rule(world.multiworld.get_location(LocationNames.b069_chest, world.player),
             lambda state: can_access_floor(world, state, "B069"))

    add_rule(world.multiworld.get_location(LocationNames.b074_chest, world.player),
             lambda state: can_access_floor(world, state, "B074"))

    add_rule(world.multiworld.get_location(LocationNames.b076_chest, world.player),
             lambda state: can_access_floor(world, state, "B076"))

    add_rule(world.multiworld.get_location(LocationNames.b077_chest, world.player),
             lambda state: can_access_floor(world, state, "B077"))

    add_rule(world.multiworld.get_location(LocationNames.b078_chest, world.player),
             lambda state: can_access_floor(world, state, "B078"))

    add_rule(world.multiworld.get_location(LocationNames.b080_chest, world.player),
             lambda state: can_access_floor(world, state, "B080"))

    add_rule(world.multiworld.get_location(LocationNames.b081_chest, world.player),
             lambda state: can_access_floor(world, state, "B081"))

    add_rule(world.multiworld.get_location(LocationNames.b088_chest, world.player),
             lambda state: can_access_floor(world, state, "B088"))

    add_rule(world.multiworld.get_location(LocationNames.b091_chest, world.player),
             lambda state: can_access_floor(world, state, "B091"))

    add_rule(world.multiworld.get_location(LocationNames.b094_chest, world.player),
             lambda state: can_access_floor(world, state, "B094"))

    add_rule(world.multiworld.get_location(LocationNames.b115_chest, world.player),
             lambda state: can_access_floor(world, state, "B115"))

    add_rule(world.multiworld.get_location(LocationNames.b116_chest, world.player),
             lambda state: can_access_floor(world, state, "B116"))

    add_rule(world.multiworld.get_location(LocationNames.b118_chest, world.player),
             lambda state: can_access_floor(world, state, "B118") and has_idol(world, state, "killer"))

    add_rule(world.multiworld.get_location(LocationNames.b122_chest, world.player),
             lambda state: can_access_floor(world, state, "B122") and has_idol(world, state, "killer"))

    add_rule(world.multiworld.get_location(LocationNames.b123_chest, world.player),
             lambda state: can_access_floor(world, state, "B123"))

    add_rule(world.multiworld.get_location(LocationNames.b127_chest, world.player),
             lambda state: can_access_floor(world, state, "B127") and (has_idol(world, state, "killer") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b133_chest, world.player),
             lambda state: can_access_floor(world, state, "B133"))

    add_rule(world.multiworld.get_location(LocationNames.b135_chest, world.player),
             lambda state: can_access_floor(world, state, "B135"))

    add_rule(world.multiworld.get_location(LocationNames.b144_chest, world.player),
             lambda state: can_access_floor(world, state, "B144"))

    add_rule(world.multiworld.get_location(LocationNames.b145_chest, world.player),
             lambda state: can_access_floor(world, state, "B145"))

    add_rule(world.multiworld.get_location(LocationNames.b151_chest, world.player),
             lambda state: can_access_floor(world, state, "B151"))

    add_rule(world.multiworld.get_location(LocationNames.b159_chest, world.player),
             lambda state: can_access_floor(world, state, "B159"))

    add_rule(world.multiworld.get_location(LocationNames.b160_chest1, world.player),
             lambda state: can_access_floor(world, state, "B160"))

    add_rule(world.multiworld.get_location(LocationNames.b160_chest2, world.player),
             lambda state: can_access_floor(world, state, "B160"))

    add_rule(world.multiworld.get_location(LocationNames.b166_chest, world.player),
             lambda state: can_access_floor(world, state, "B166"))

    add_rule(world.multiworld.get_location(LocationNames.b171_chest, world.player),
             lambda state: can_access_floor(world, state, "B171"))

    add_rule(world.multiworld.get_location(LocationNames.b173_chest, world.player),
             lambda state: can_access_floor(world, state, "B173"))

    add_rule(world.multiworld.get_location(LocationNames.b176_chest, world.player),
             lambda state: can_access_floor(world, state, "B176"))

    add_rule(world.multiworld.get_location(LocationNames.b177_chest, world.player),
             lambda state: can_access_floor(world, state, "B177"))

    add_rule(world.multiworld.get_location(LocationNames.b178_chest1, world.player),
             lambda state: can_access_floor(world, state, "B178") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b178_chest2, world.player),
             lambda state: can_access_floor(world, state, "B178") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b179_chest, world.player),
             lambda state: can_access_floor(world, state, "B179"))

    add_rule(world.multiworld.get_location(LocationNames.b180_chest, world.player),
             lambda state: can_access_floor(world, state, "B180"))

    add_rule(world.multiworld.get_location(LocationNames.b189_chest, world.player),
             lambda state: can_access_floor(world, state, "B189"))

    add_rule(world.multiworld.get_location(LocationNames.b191_chest, world.player),
             lambda state: can_access_floor(world, state, "B191"))

    add_rule(world.multiworld.get_location(LocationNames.b195_chest1, world.player),
             lambda state: can_access_floor(world, state, "B195") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b195_chest2, world.player),
             lambda state: can_access_floor(world, state, "B195") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b195_chest3, world.player),
             lambda state: can_access_floor(world, state, "B195") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b195_chest4, world.player),
             lambda state: can_access_floor(world, state, "B195") and (has_idol(world, state, "watcher") or state.has(ItemNames.void_wings, world.player)))

    add_rule(world.multiworld.get_location(LocationNames.b200_chest, world.player),
             lambda state: can_access_floor(world, state, "B200"))

    add_rule(world.multiworld.get_location(LocationNames.b209_chest, world.player),
             lambda state: can_access_floor(world, state, "B209") and has_idol(world, state, "killer"))

    add_rule(world.multiworld.get_location(LocationNames.b210_chest, world.player),
             lambda state: can_access_floor(world, state, "B210"))
                               
    #greed zone locations
    # will rewrite these rules once we migrate to the Dungeon system
    if world.options.greedzone:
        add_rule(world.multiworld.get_location(LocationNames.m14_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m14_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest1, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest2, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest3, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest4, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest5, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest6, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest7, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest8, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest9, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest10, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest11, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))
        add_rule(world.multiworld.get_location(LocationNames.m15_chest12, world.player),
                 lambda state: state.has(ItemNames.greed_coin, world.player, world.greed_coin_count) and
                        state.has_all({ItemNames.void_wings, ItemNames.void_sword}, world.player) and
                        has_idol(world, state, "killer") and can_access_floor(world, state, "B193"))