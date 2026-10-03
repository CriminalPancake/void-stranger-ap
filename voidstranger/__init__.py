import importlib, math
from typing import Dict, List
from collections import defaultdict, deque
from BaseClasses import Region, Item, MultiWorld, CollectionState, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World, LogicMixin

from .Items import VoidStrangerItem, burden_item_data_table, misc_item_data_table, brand_item_data_table, \
    statue_item_data_table, shortcut_item_data_table, item_data_table, item_table
from .Locations import VoidStrangerLocation, burden_location_data_table, misc_location_data_table,\
    mural_location_data_table, shortcut_location_data_table, chest_location_data_table, location_table, \
    greed_chest_location_data_table, beehole_chest_location_data_table, whitevoid_location_data_table, deadend_location_data_table
from .Options import VoidStrangerOptions
from .Constants import ItemNames, LocationNames
from .LocationGroups import vs_location_groups
from .ItemGroups import vs_item_groups

class VoidStrangerWebWorld(WebWorld):
    theme = "stone"


class VoidStrangerWorld(World):

    #Class Data
    game = "Void Stranger"
    web = VoidStrangerWebWorld()
    options_dataclass = VoidStrangerOptions
    options: VoidStrangerOptions
    location_name_to_id = location_table
    item_name_to_id = item_table
    location_name_groups = vs_location_groups
    item_name_groups = vs_item_groups

    #Instance Data
    goal_logic_mapping: Dict[str, List[List[str]]]
    greed_coin_count: int
    #locust_up_size: int
    #locust_up_amount: int
    #starting_max_locust: int
        
    # for shuffle floors, we make a list with all main floors allowed by settings (generate keys method or w/e)
    #   then pick a random subset of them to reach 256 floors after first including the required floors.
    # for every floor with a shortcut, we pick a side brane and update the shortcut destination to that new side brane, and add the side brane to a list.
    # then at the end, every side brane in that list gets assigned a possibly random exit floor, somewhere on the main brane_order.
    # lastly, brand floors get their table updated too, and are handled similarily to shortcut floors.
    
    # add exception for B143, where Gor gives you a free locust if you have none? Or just ignore that.
    
    # how dungeon lists work is it's the floor data, but with an extra tag for if it's a main or not, and all grouped under the {DungeonName} key.
    # If the dungeon is excluded by yaml option (either by name, or randomly via dungeon count), it checks the "Standalone" tag for if specific required floors can be added by themselves, without the entrance.
    # Standalone floors become optional for that floor type (main or side)
    # If the dungeon is included, all required dungeon floors are put into their respective required list.
    # we cannot/shouldn't shuffle dungeon entrances?
    # if floor shuffle, assume all dungeons that appear have checks
    # figure out what to do if too many dungeons disabled, becuase then too many side branes are disabled?
    
    
    def __init__(self, multiworld: MultiWorld, player: int):
        # initialize attributes
        self.vs_brane_order = []
        self.vs_brane_list = {}
        self.vs_dungeon_list = []
         
        # generate the list of floors
        # mostly setup for the future shuffle floors option
        
        # create floor generation variables
        pool_required_main = {}
        pool_required_side = {}
        pool_optional_main = {}
        pool_optional_side = {}
        pool_dungeons = {}
        goal_dungeons = ["DIS"]
        floor_pack_list = ["vanilla_floors"]
        # if goal settings
            # add dungeons to goal_dungeons
        #if add community floor packs
            #floor_pack_list.extend(self.options.EnabledFloors)
        
        # import all enabled floor packs and sort the floors within
        for enabled_floor_pack in floor_pack_list:
            floor_pack = importlib.import_module(f".Floors.{enabled_floor_pack}", package = __name__)
            pool_required_main.update({k: v.copy() for k, v in floor_pack.RequiredMainBranes.items()})
            pool_required_side.update({k: v.copy() for k, v in floor_pack.RequiredSideBranes.items()})
            pool_optional_main.update({k: v.copy() for k, v in floor_pack.OptionalMainBranes.items()})
            pool_optional_side.update({k: v.copy() for k, v in floor_pack.OptionalSideBranes.items()})
            pool_dungeons.update({k: v.copy() for k, v in floor_pack.Dungeons.items()})
        
        # when shuffle floors is off, excluded dungeons remain, but logic won't place anything there.
        # when shuffle floors is on, excluding a dungeon will remove it's entrance and all related floors entirely
        if False: #if shuffle floors
            print("dummy line")
            # if treasure hunter / ninnie (except always do this?)
                # add first and last floors of their sequence to required, as well as 5 other random floors from their sequence
                # then, put the rest of their sequence into optional
            # edit brand and shortcut connections as necessary
            # for dungeon not in goal_dungeons:
                # etc
            # for generation, include option for a floor to be "locked" behind the placement of another floor.
            # aka, if a floor is placed, it pulls it's corrosponding floor out of the locked pool
                #give the locked floor ths field: "locked": "(floors required to be placed first)"
            # also, allow for floors to be placed in any order, sometimes shortcuts taken first, sometimes not, etc
            
        # if shuffle floors is off, prepare vanilla floor order and floors
        else:
            self.vs_brane_order = Floors.vanilla_floors.VanillaBraneOrder
            self.vs_brane_list.update(pool_required_main)
            self.vs_brane_list.update(pool_required_side)
            self.vs_brane_list.update(pool_optional_main)
            self.vs_brane_list.update(pool_optional_side)
            self.vs_brane_list.update(pool_dungeons)
         
        # connect stairs in brane order
        for brane in self.vs_brane_order:
            floor = self.vs_brane_list[brane]
            if floor["Stairs"] != False:
                if floor["Stairs"][0] == "next":
                    brane_index = self.vs_brane_order.index(brane)
                    i = 1
                    while True:
                        if brane_index + i > 255:
                            floor["Stairs"] = ("whitevoid", floor["Stairs"][1])
                            break
                        next_floor = self.vs_brane_order[brane_index + i]
                        if "Skipped" in self.vs_brane_list[next_floor]:
                            i += 1
                            continue
                        floor["Stairs"] = (next_floor, floor["Stairs"][1]) # update stair connection by replacing the tuple
                        break
        super().__init__(multiworld, player)
    
    
    
    # main pathfinding function
    def calculate_accessibility(self, state) -> None:
        from .Rules import has_item_by_type, check_item_tuples
        
        state.vs_stale_pathfinding[self.player] = False
        for brane in self.vs_brane_list:
            state.vs_brane_accessibility[self.player].update({brane: {"Accessible": False, "Locust_Score": -1}})
        max_locust_score = min(99, (state.prog_items[self.player][ItemNames.locust_capacity_up] * 3))
        
        # main pathfinding loop
        queue = deque([("B001", 0)])
        while queue:
            current_brane, locust_score = queue.pop()
            brane_access = state.vs_brane_accessibility[self.player][current_brane]
            if brane_access["Accessible"] and brane_access["Locust_Score"] >= locust_score:
                continue
            brane_access["Accessible"] = True
            brane_access["Locust_Score"] = locust_score
            floor = self.vs_brane_list[current_brane]
            if current_brane in self.vs_brane_order:
                floor_index = self.vs_brane_order.index(current_brane)
            else:
                floor_index = -1
            
            locust_score += floor["Chest_Score"]
            if locust_score > max_locust_score:
                locust_score = max_locust_score
            
            if self.options.logiccomplexity and floor_index != -1 and "Interface" in floor:
                if check_item_tuples(self, state, floor["Interface"]):
                    floor_index_fixed = (floor_index // 100) * 100 # round down to hundreds
                    floor_index_changeable = floor_index % 100
                    locust_score = min(max(floor_index_changeable, locust_score), max_locust_score) # update locust score for other paths
                    i = locust_score
                    while i >= 0:
                        if floor_index_fixed + i > 255:
                            queue.append(("whitevoid", 99))
                            i = 55
                        else:
                            new_score = max(min(floor_index_changeable, max_locust_score), i) # This works because we previously bounded i to be no greater than max_locust_score
                            new_floor = floor_index_fixed + i
                            queue.append((self.vs_brane_order[new_floor], new_score))
                            #print(str(floor_index) + " " + str(floor_index_fixed) + " " + str(floor_index_changeable) + " " + str(max_locust_score) + " " + str(new_floor) + " " + str(new_score))
                        i -= 1
            
            if floor["Stairs"] != False:
                if check_item_tuples(self, state, floor["Stairs"][1]):
                    queue.append((floor["Stairs"][0], locust_score))
            
            if "Shortcut" in floor:
                for shortcut in floor["Shortcut"]:
                    if check_item_tuples(self, state, shortcut[1]):
                        queue.append((shortcut[0], locust_score))
            
            if "Brand_Room" in floor:
                for brand_carve in Floors.vanilla_floors.VanillaBrandCarving[current_brane]:
                    if check_item_tuples(self, state, brand_carve[1]):
                        queue.append((brand_carve[0], locust_score))
            
            if self.options.logiccomplexity and floor_index != -1 and "Smiler" in floor:
                if check_item_tuples(self, state, floor["Smiler"]):
                    i = locust_score
                    while i > 0:
                        if floor_index + i > 255:
                            queue.append(("whitevoid", 99))
                        else:
                            queue.append((self.vs_brane_order[floor_index + i], 0))
                        i -= 1
    
    
    
    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        state.vs_stale_pathfinding[self.player] = True
        return change

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().remove(state, item)
        state.vs_stale_pathfinding[self.player] = True
        return change

    def generate_early(self):
        return
        #if self.options.logiccomplexity == 0:
        #    raise OptionError("ERROR: Simple Logic is not compatible with OPTION")
    
    def create_item(self, name: str) -> VoidStrangerItem:
        return VoidStrangerItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: list[VoidStrangerItem] = []

        location_count: int = 18
        unfilled_locations: int = 0

        item_pool += [self.create_item(name)
                      for name in burden_item_data_table.keys()
                      if name not in self.options.start_inventory]
        item_pool += [self.create_item(name)
                      for name in misc_item_data_table.keys()
                      if name not in self.options.start_inventory]
        item_pool += [self.create_item(name)
                      for name in brand_item_data_table.keys()
                      if name not in self.options.start_inventory]

        location_count += 68
        #if lillith, location_count = 69
        unfilled_locations += 68
        
        #dungeons
        if self.options.deadend:
            location_count += 10
            unfilled_locations += 10
        if self.options.whitevoid != 0:
            location_count += 5
            unfilled_locations += 5
        if self.options.beehole:
            location_count += 4
            unfilled_locations += 4
        if self.options.greedzone:
            self.greed_coin_count: int = int(self.options.greedcoinamount.value)
            location_count += 15
            unfilled_locations = unfilled_locations + 15 - self.greed_coin_count
            item_pool += [self.create_item(ItemNames.greed_coin) for _ in range(self.greed_coin_count)]
        
        unfilled_locations -= 33
        item_pool += [self.create_item(ItemNames.locust_capacity_up) for _ in range(33)]
            
        if self.options.idolsanity:
            unfilled_locations-= 3
            item_pool += [self.create_item(name)
                          for name in statue_item_data_table.keys()
                          if name not in self.options.start_inventory]
        if self.options.shortcutsanity:
            location_count+= 5
            item_pool += [self.create_item(name)
                          for name in shortcut_item_data_table.keys()
                          if name not in self.options.start_inventory]
                          
        # fill remaining locations with filler
        item_pool += [self.create_item(ItemNames.bonus_locust) for _ in range(unfilled_locations)] # cap this with setting
        
        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        from .Regions import region_data_table

        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)

            region.add_locations({
                location_name: location_data.address for location_name, location_data in
                burden_location_data_table.items() if location_data.region == region_name
            }, VoidStrangerLocation)

            region.add_locations({
                location_name: location_data.address for location_name, location_data in
                misc_location_data_table.items() if location_data.region == region_name
            }, VoidStrangerLocation)
            
            region.add_locations({
                location_name: location_data.address for location_name, location_data in
                mural_location_data_table.items() if location_data.region == region_name
            }, VoidStrangerLocation)

            region.add_locations({
                location_name: location_data.address for location_name, location_data in
                chest_location_data_table.items() if location_data.region == region_name
            }, VoidStrangerLocation)
            
            if self.options.shortcutsanity:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    shortcut_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            if self.options.deadend:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    deadend_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)
            
            if self.options.whitevoid != 0:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    whitevoid_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)
            
            if self.options.beehole:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    beehole_chest_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)
            
            if self.options.greedzone:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    greed_chest_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            region.add_exits(region_data_table[region_name].connecting_regions)

    def set_rules(self) -> None:
        from .Rules import set_rules
        set_rules(self)

    def fill_slot_data(self):
        return {
            "idolsanity": self.options.idolsanity.value,
            "shortcutsanity": self.options.shortcutsanity.value,
            "deadend": self.options.deadend.value,
            "whitevoid": self.options.whitevoid.value,
            "beehole": self.options.beehole.value,
            "greedzone": self.options.greedzone.value,
            "disdungeon": self.options.disdungeon.value,
            "greedcoinamount": self.options.greedcoinamount.value,
            "skipcutscenes": self.options.skipcutscenes.value,
        }
    
class vsstate(LogicMixin):
    vs_stale_pathfinding: dict[int, bool]          
    vs_brane_accessibility: dict[int, dict]
    
    def init_mixin(self, _):
        self.vs_stale_pathfinding = defaultdict(lambda: True)
        self.vs_brane_accessibility = defaultdict(lambda: {})
        