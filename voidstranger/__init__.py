import importlib, math
from typing import Dict, List
from collections import defaultdict
from BaseClasses import Region, Item, MultiWorld, CollectionState, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World, LogicMixin

from .Constants.ItemNames import greed_coin
from .Items import VoidStrangerItem, burden_item_data_table, misc_item_data_table, brand_item_data_table, \
    statue_item_data_table, shortcut_item_data_table, locust_item_table, item_data_table, item_table, \
    prog_brand_item_data_table
from .Locations import VoidStrangerLocation, burden_location_data_table, misc_location_data_table,\
    mural_location_data_table, statue_location_data_table, shortcut_location_data_table, chest_location_data_table, \
    location_table, greed_chest_location_data_table
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
    locust_up_size: int
    locust_up_amount: int
    starting_max_locust: int
    
    #vs_brane_order: List         # ordered list of all 255 main branes in the seed
    #vs_brane_list: Dict          # dict of all branes in the seed, in the form {brane_id: {brane_data}}
    #vs_dungeon_list: List        # list of dungeons in the seed, in format (dungeon_name, accessible?)
    #vs_statue_floors: Dict       # dict of lists of floors that each statue type appears on
    
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
        self.vs_statue_floors = ({"lover":[],"smiler":[],"killer":[],"slower":[],"watcher":[]})
        
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
            # aka, if a floor is placed, it pulls it's corrosponding floor from the locked pool
            # also, allow for floors to be placed in any order, sometimes shortcuts taken first, sometimes not, etc
            
        # if shuffle floors is off, prepare vanilla floor order and floors
        else:
            self.vs_brane_order = Floors.vanilla_floors.VanillaBraneOrder
            self.vs_brane_list.update(pool_required_main)
            self.vs_brane_list.update(pool_required_side)
            self.vs_brane_list.update(pool_optional_main)
            self.vs_brane_list.update(pool_optional_side)
            self.vs_brane_list.update(Floors.vanilla_floors.VanillaDungeonEntrances)
        
        
        # Add required access rule tags to each active floor
        # Compile floor lists for each statue type
        for brane in self.vs_brane_list:
            for statue_type in self.vs_brane_list[brane]["Statues"]:
                self.vs_statue_floors[statue_type].append(brane)
            
        
        # parse stair connections with "next"
        # TODO check for Skipped Tag here
        for brane in self.vs_brane_order:
            if self.vs_brane_list[brane]["Stairs"] != False:
                if self.vs_brane_list[brane]["Stairs"][0] == "next":
                    if self.vs_brane_order.index(brane) == 255:
                        if False:   # if white void dungeon is enabled
                            self.vs_brane_list[brane]["Dungeon"] = ("white_void", self.vs_brane_list[brane]["Stairs"][1])
                        self.vs_brane_list[brane]["Stairs"] = False
                    else:
                        self.vs_brane_list[brane]["Stairs"] = (self.vs_brane_order[self.vs_brane_order.index(brane) + 1], self.vs_brane_list[brane]["Stairs"][1]) # messy line to replace a tuple
        super().__init__(multiworld, player)
    
    
    
    # primary function for checking floor accessibility
    # checks if the target floor has already been visited with a better locust score, and if not, whether the required items for the connection have been collected
    # connection tuple format: (destination, [[option A item_tuples],[option B item_tuples]], running_locust_score)
    def check_floor_connection(self, state, connection_tuple, current_brane, brane_index) -> tuple[bool, str, int|str]:
        from .Rules import check_item_tuples
        if state.vs_brane_accessibility[self.player][connection_tuple[0]]["Accessible"] == True and state.vs_brane_accessibility[self.player][connection_tuple[0]]["Locust_Score"] >= connection_tuple[2]:
            return False, current_brane, brane_index
        if check_item_tuples(self, state, connection_tuple[1]):
            if connection_tuple[0] in self.vs_brane_order:
                brane_index = self.vs_brane_order.index(connection_tuple[0])
            else:
                brane_index = "???"
            return True, connection_tuple[0], brane_index
        else:
            return False, current_brane, brane_index
    
    
    # main pathfinding function
    # iterates through every possible connection between floors to determine accessibility with the current set of collected items
    def calculate_accessibility(self, state) -> None:
        from .Rules import has_item_by_type, check_item_tuples
        state.vs_stale_pathfinding[self.player] = False
        
        for brane in self.vs_brane_list:
            state.vs_brane_accessibility[self.player].update({brane: {"Accessible": False, "Locust_Score": -1}})
        
        max_locust_score = max(99, (state.prog_items[self.player][ItemNames.locust_capacity_up] * self.locust_up_size) + self.starting_max_locust)
        
        # main pathfinding loop
        queue = [("B001", 0)]
        while queue:
            current_brane, locust_score = queue.pop(0)
            #for node in queue:
            #    if current_brane == node[0]:
            #        locust_score = max(locust_score, node[1])
            #        queue.remove(node)
                    
            brane_access = state.vs_brane_accessibility[self.player][current_brane]
            if brane_access["Accessible"] and brane_access["Locust_Score"] >= locust_score:
                continue
            
            brane_access["Accessible"] = True
            brane_access["Locust_Score"] = locust_score
            floor = self.vs_brane_list[current_brane]
            
            locust_score += floor["Chest_Score"]
            if locust_score > max_locust_score:
                locust_score = max_locust_score
            
            if floor["Stairs"] != False:
                if check_item_tuples(self, state, floor["Stairs"][1]):
                    queue.append((floor["Stairs"][0], locust_score))

            if floor["Shortcut"] != False:
                for shortcut in floor["Shortcut"]:
                    if check_item_tuples(self, state, shortcut[1]):
                        queue.append((shortcut[0], locust_score))

            if floor["Brand_Room"] != False:
                for brand_carve in Floors.vanilla_floors.VanillaBrandCarving[current_brane]:
                    if check_item_tuples(self, state, brand_carve[1]):
                        queue.append((brand_carve[0], locust_score))
                        
        #print(state.vs_brane_accessibility[self.player])
        
    
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
        if self.options.logiccomplexity == 1:
            raise OptionError("ERROR: Full Logic is not currently implemented")
    
    
    def create_item(self, name: str) -> VoidStrangerItem:
        return VoidStrangerItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: list[VoidStrangerItem] = []

        location_count: int = 7
        unfilled_locations: int = 0

        item_pool += [self.create_item(name)
                      for name in burden_item_data_table.keys()
                      if name not in self.options.start_inventory]

        item_pool += [self.create_item(name)
                      for name in misc_item_data_table.keys()
                      if name not in self.options.start_inventory]

        location_count += 68
        #if lillith, location_count = 69
        unfilled_locations += 68

        if self.options.greedzone:
            self.greed_coin_count: int = int(self.options.greedcoinamount.value)
            location_count += 15
            unfilled_locations = unfilled_locations + 15 - self.greed_coin_count
            item_pool += [self.create_item(ItemNames.greed_coin) for _ in range(self.greed_coin_count)]
        
        self.locust_up_size: int = int(self.options.locustcapacityup.value)
        self.locust_up_amount: int = min(unfilled_locations, math.ceil(99 / self.locust_up_size))
        self.starting_max_locust: int = math.ceil(99 / self.locust_up_size) - self.locust_up_amount
        unfilled_locations -= self.locust_up_amount
        item_pool += [self.create_item(ItemNames.locust_capacity_up) for _ in range(self.locust_up_amount)]
        print("LocUP " + str(self.locust_up_amount))
        #input()
            
        if self.options.brandsanity:
            location_count+= 9

            if self.options.progressivebrands:
                item_pool += [self.create_item(ItemNames.brand_prog) for _ in range(9)]
            else:
                item_pool += [self.create_item(name)
                              for name in brand_item_data_table.keys()
                              if name not in self.options.start_inventory]
        if self.options.idolsanity:
            location_count+= 3
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

            # Create locations.
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
                chest_location_data_table.items() if location_data.region == region_name
            }, VoidStrangerLocation)

            if self.options.greedzone:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    greed_chest_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            if self.options.brandsanity:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    mural_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            if self.options.idolsanity:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    statue_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            if self.options.shortcutsanity:
                region.add_locations({
                    location_name: location_data.address for location_name, location_data in
                    shortcut_location_data_table.items() if location_data.region == region_name
                }, VoidStrangerLocation)

            region.add_exits(region_data_table[region_name].connecting_regions)

    def set_rules(self) -> None:
        #self.generate_brane_list()
        from .Rules import set_rules
        set_rules(self)

    def fill_slot_data(self):
        return {
            "brandsanity": self.options.brandsanity.value,
            "locustcapacityup": self.options.locustcapacityup.value,
            #"locustcapacityamount": self.locust_up_amount,
            "startingmaxlocust": self.starting_max_locust,
            "progressivebrands": self.options.progressivebrands.value,
            "idolsanity": self.options.idolsanity.value,
            "shortcutsanity": self.options.shortcutsanity.value,
            "shortcutcheating": self.options.shortcutcheating.value,
            "greedzone": self.options.greedzone.value,
            "greedcoinamount": self.options.greedcoinamount.value,
            "skipcutscenes": self.options.skipcutscenes.value,
            "visibleinterface": self.options.visibleinterface.value
        }
    
class vsstate(LogicMixin):
    vs_stale_pathfinding: dict[int, bool]          
    vs_brane_accessibility: dict[int, dict]
    
    def init_mixin(self, _):
        self.vs_stale_pathfinding = defaultdict(lambda: True)
        self.vs_brane_accessibility = defaultdict(lambda: {})
        