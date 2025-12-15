from typing import Dict, List
from BaseClasses import Region, Item, CollectionState, ItemClassification
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

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

    #Instance Data
    locusts: ItemClassification.progression
    goal_logic_mapping: Dict[str, List[List[str]]]
    greed_coin_count: int

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change and item.name == ItemNames.locust_idol:
            state.prog_items[item.player]["locusts"] += 1
        elif change and item.name == ItemNames.tripled_locust:
            state.prog_items[item.player]["locusts"] += 3
        return change

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().remove(state, item)
        if change and item.name == ItemNames.locust_idol:
            state.prog_items[item.player]["locusts"] -= 1
        elif change and item.name == ItemNames.tripled_locust:
            state.prog_items[item.player]["locusts"] -= 3
        return change

    def create_item(self, name: str) -> VoidStrangerItem:
        return VoidStrangerItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: list[VoidStrangerItem] = []

        location_count: int = 7

        item_pool += [self.create_item(name)
                      for name in burden_item_data_table.keys()
                      if name not in self.options.start_inventory]

        item_pool += [self.create_item(name)
                      for name in misc_item_data_table.keys()
                      if name not in self.options.start_inventory]

        if self.options.greedzone and not self.options.locustsanity:
            raise OptionError(
                f"Void Stranger player {self.player_name} failed. "
                + "Locustsanity must be enabled for greedzone to be enabled."
            )

        if self.options.locustsanity:
            location_count += 68
            gray_locusts: int = 42
            gray_triple_locusts: int = 26
            #for later
            lillith_locusts: int = 40
            lillith_triple_locusts: int = 29

            if self.options.greedzone:
                location_count += 15
                self.greed_coin_count: int = int(self.options.greedcoinamount.value)
                if self.greed_coin_count > 15:
                    gray_locusts -= self.greed_coin_count - 15 #removing locusts to make room for more greed coins if needed
                    if gray_locusts < 0: #if there are more greed coins than locusts, start removing triple locusts
                        gray_triple_locusts += gray_locusts
                item_pool += [self.create_item(ItemNames.greed_coin) for _ in range(self.greed_coin_count)]

            item_pool += [self.create_item(ItemNames.tripled_locust) for _ in range(gray_triple_locusts)]
            item_pool += [self.create_item(ItemNames.locust_idol) for _ in range(gray_locusts)]
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

            if self.options.locustsanity:
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
        from .Rules import set_rules
        set_rules(self)

    def fill_slot_data(self):
        return {
            "locustsanity": self.options.locustsanity.value,
            "brandsanity": self.options.brandsanity.value,
            "progressivebrands": self.options.progressivebrands.value,
            "idolsanity": self.options.idolsanity.value,
            "shortcutsanity": self.options.shortcutsanity.value,
            "shortcutcheating": self.options.shortcutcheating.value,
            "greedzone": self.options.greedzone.value,
            "greedcoinamount": self.options.greedcoinamount.value,
            "skipcutscenes": self.options.skipcutscenes.value,
            "visibleinterface": self.options.visibleinterface.value
        }
