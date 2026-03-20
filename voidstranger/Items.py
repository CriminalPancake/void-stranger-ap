from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Constants import ItemNames
from .Constants.ItemNames import greed_coin
from .Locations import VoidStrangerLocationData

void_stranger_base_id: int = 12345000

class VoidStrangerItem(Item):
    game = "Void Stranger"

class VoidStrangerItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler

burden_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.void_memory: VoidStrangerItemData(void_stranger_base_id + 0, ItemClassification.progression),
    ItemNames.void_wings: VoidStrangerItemData(void_stranger_base_id + 1, ItemClassification.progression),
    ItemNames.void_sword: VoidStrangerItemData(void_stranger_base_id + 2, ItemClassification.progression)
}

misc_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.endless_void_rod: VoidStrangerItemData(void_stranger_base_id + 3, ItemClassification.progression),
    ItemNames.interface_manip: VoidStrangerItemData(void_stranger_base_id + 4, ItemClassification.progression),
    ItemNames.lust_seal: VoidStrangerItemData(void_stranger_base_id + 27, ItemClassification.progression),
    ItemNames.sloth_seal: VoidStrangerItemData(void_stranger_base_id + 28, ItemClassification.progression)
}

brand_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.brand_add: VoidStrangerItemData(void_stranger_base_id + 5, ItemClassification.progression),
    ItemNames.brand_eus: VoidStrangerItemData(void_stranger_base_id + 6, ItemClassification.progression),
    ItemNames.brand_bee: VoidStrangerItemData(void_stranger_base_id + 7, ItemClassification.progression),
    ItemNames.brand_mon: VoidStrangerItemData(void_stranger_base_id + 8, ItemClassification.progression),
    ItemNames.brand_tan: VoidStrangerItemData(void_stranger_base_id + 9, ItemClassification.progression),
    ItemNames.brand_gor: VoidStrangerItemData(void_stranger_base_id + 10, ItemClassification.progression),
    ItemNames.brand_lev: VoidStrangerItemData(void_stranger_base_id + 11, ItemClassification.progression),
    ItemNames.brand_cif: VoidStrangerItemData(void_stranger_base_id + 12, ItemClassification.progression),
    ItemNames.brand_dis: VoidStrangerItemData(void_stranger_base_id + 13, ItemClassification.progression)
}

prog_brand_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.brand_prog: VoidStrangerItemData(void_stranger_base_id + 29, ItemClassification.progression)
}

statue_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.enable_lover: VoidStrangerItemData(void_stranger_base_id + 14, ItemClassification.progression),
    ItemNames.enable_smiler: VoidStrangerItemData(void_stranger_base_id + 15, ItemClassification.progression),
    ItemNames.enable_killer: VoidStrangerItemData(void_stranger_base_id + 16, ItemClassification.progression)
    # ItemNames.disable_greeder: VoidStrangerItemData(void_stranger_base_id + 17, ItemClassification.progression),
    # ItemNames.disable_slower: VoidStrangerItemData(void_stranger_base_id + 18, ItemClassification.useful),
    # ItemNames.disable_watcher: VoidStrangerItemData(void_stranger_base_id + 19, ItemClassification.useful),
}

shortcut_item_data_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.shortcut1: VoidStrangerItemData(void_stranger_base_id + 20, ItemClassification.progression),
    ItemNames.shortcut2: VoidStrangerItemData(void_stranger_base_id + 21, ItemClassification.progression),
    ItemNames.shortcut3: VoidStrangerItemData(void_stranger_base_id + 22, ItemClassification.progression),
    ItemNames.shortcut4: VoidStrangerItemData(void_stranger_base_id + 23, ItemClassification.progression),
    ItemNames.shortcut5: VoidStrangerItemData(void_stranger_base_id + 24, ItemClassification.progression)
}

locust_item_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.bonus_locust: VoidStrangerItemData(void_stranger_base_id + 25, ItemClassification.filler),
    ItemNames.locust_capacity_up: VoidStrangerItemData(void_stranger_base_id + 26, ItemClassification.progression)
}

greed_coin_item_table: Dict[str, VoidStrangerItemData] = {
    ItemNames.greed_coin: VoidStrangerItemData(void_stranger_base_id + 30, ItemClassification.progression)
}

item_data_table: Dict[str, VoidStrangerItemData] = {
    **burden_item_data_table,
    **misc_item_data_table,
    **brand_item_data_table,
    **prog_brand_item_data_table,
    **statue_item_data_table,
    **shortcut_item_data_table,
    **locust_item_table,
    **greed_coin_item_table
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}