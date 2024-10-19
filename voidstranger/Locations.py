from typing import Dict, NamedTuple, Optional

from BaseClasses import Location
from .Constants import LocationNames


void_stranger_base_id: int = 12345000


class VoidStrangerLocation(Location):
    game = "Void Stranger"


class VoidStrangerLocationData(NamedTuple):
    region: str
    address: Optional[int] = None

burden_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.burden_chest1: VoidStrangerLocationData("Void", void_stranger_base_id + 0),
    LocationNames.burden_chest2: VoidStrangerLocationData("Void", void_stranger_base_id + 1),
    LocationNames.burden_chest3: VoidStrangerLocationData("Void", void_stranger_base_id + 93)
}

misc_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.endless_void_rod_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 2),
    LocationNames.interface_manip_hint: VoidStrangerLocationData("Void", void_stranger_base_id + 3),
    LocationNames.lust_slain: VoidStrangerLocationData("Void", void_stranger_base_id + 94),
    LocationNames.sloth_slain: VoidStrangerLocationData("Void", void_stranger_base_id + 95)
}

mural_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.mural_add: VoidStrangerLocationData("Void", void_stranger_base_id + 4),
    LocationNames.mural_eus: VoidStrangerLocationData("Void", void_stranger_base_id + 5),
    LocationNames.mural_bee: VoidStrangerLocationData("Void", void_stranger_base_id + 6),
    LocationNames.mural_mon: VoidStrangerLocationData("Void", void_stranger_base_id + 7),
    LocationNames.mural_tan: VoidStrangerLocationData("Void", void_stranger_base_id + 8),
    LocationNames.mural_gor: VoidStrangerLocationData("Void", void_stranger_base_id + 9),
    LocationNames.mural_lev: VoidStrangerLocationData("Void", void_stranger_base_id + 10),
    LocationNames.mural_cif: VoidStrangerLocationData("Void", void_stranger_base_id + 11),
    LocationNames.mural_dis: VoidStrangerLocationData("Void", void_stranger_base_id + 12)
}

statue_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.statue_lover: VoidStrangerLocationData("Void", void_stranger_base_id + 13),
    LocationNames.statue_smiler: VoidStrangerLocationData("Void", void_stranger_base_id + 14),
    LocationNames.statue_killer: VoidStrangerLocationData("Void", void_stranger_base_id + 15)
    # LocationNames.statue_greeder: VoidStrangerLocationData("Void", void_stranger_base_id + 16),
    # LocationNames.statue_slower: VoidStrangerLocationData("Void", void_stranger_base_id + 17),
    # LocationNames.statue_watcher: VoidStrangerLocationData("Void", void_stranger_base_id + 18),
}

shortcut_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.buy_shortcut1: VoidStrangerLocationData("Void", void_stranger_base_id + 19),
    LocationNames.buy_shortcut2: VoidStrangerLocationData("Void", void_stranger_base_id + 20),
    LocationNames.buy_shortcut3: VoidStrangerLocationData("Void", void_stranger_base_id + 21),
    LocationNames.buy_shortcut4: VoidStrangerLocationData("Void", void_stranger_base_id + 22),
    LocationNames.buy_shortcut5: VoidStrangerLocationData("Void", void_stranger_base_id + 23)
}

chest_location_data_table: Dict[str, VoidStrangerLocationData] = {
    LocationNames.b003_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 24),
    LocationNames.b004_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 25),
    LocationNames.b005_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 26),
    LocationNames.b006_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 27),
    LocationNames.b009_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 28),
    LocationNames.b010_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 29),
    LocationNames.b012_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 30),
    LocationNames.b014_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 31),
    LocationNames.b018_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 32),
    LocationNames.b024_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 34),
    LocationNames.b025_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 35),
    LocationNames.b026_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 36),
    LocationNames.b032_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 37),
    LocationNames.b033_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 38),
    LocationNames.b034_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 39),
    LocationNames.b035_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 40),
    LocationNames.b036_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 41),
    LocationNames.b037_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 42),
    LocationNames.b040_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 43),
    LocationNames.b041_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 44),
    LocationNames.b043_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 45),
    LocationNames.b048_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 46),
    LocationNames.b050_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 47),
    LocationNames.b060_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 48),
    LocationNames.b064_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 49),
    LocationNames.b065_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 50),
    LocationNames.b069_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 51),
    LocationNames.b074_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 52),
    LocationNames.b076_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 53),
    LocationNames.b077_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 54),
    LocationNames.b078_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 55),
    LocationNames.b080_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 56),
    LocationNames.b081_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 57),
    LocationNames.b088_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 58),
    LocationNames.b091_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 59),
    LocationNames.b094_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 60),
    LocationNames.b115_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 61),
    LocationNames.b116_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 62),
    LocationNames.b118_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 63),
    LocationNames.b122_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 64),
    LocationNames.b123_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 65),
    LocationNames.b127_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 66),
    LocationNames.b133_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 67),
    LocationNames.b135_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 68),
    LocationNames.b144_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 69),
    LocationNames.b145_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 70),
    LocationNames.b151_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 71),
    LocationNames.b159_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 72),
    LocationNames.b160_chest1: VoidStrangerLocationData("Void", void_stranger_base_id + 73),
    LocationNames.b160_chest2: VoidStrangerLocationData("Void", void_stranger_base_id + 74),
    LocationNames.b166_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 75),
    LocationNames.b171_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 76),
    LocationNames.b173_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 77),
    LocationNames.b176_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 78),
    LocationNames.b177_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 79),
    LocationNames.b178_chest1: VoidStrangerLocationData("Void", void_stranger_base_id + 80),
    LocationNames.b178_chest2: VoidStrangerLocationData("Void", void_stranger_base_id + 81),
    LocationNames.b179_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 82),
    LocationNames.b180_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 83),
    LocationNames.b189_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 84),
    LocationNames.b191_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 85),
    LocationNames.b195_chest1: VoidStrangerLocationData("Void", void_stranger_base_id + 86),
    LocationNames.b195_chest2: VoidStrangerLocationData("Void", void_stranger_base_id + 87),
    LocationNames.b195_chest3: VoidStrangerLocationData("Void", void_stranger_base_id + 88),
    LocationNames.b195_chest4: VoidStrangerLocationData("Void", void_stranger_base_id + 89),
    LocationNames.b200_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 90),
    LocationNames.b209_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 91),
    LocationNames.b210_chest: VoidStrangerLocationData("Void", void_stranger_base_id + 92)
}

location_data_table: Dict[str, VoidStrangerLocationData] = {
    **burden_location_data_table,
    **misc_location_data_table,
    **mural_location_data_table,
    **statue_location_data_table,
    **shortcut_location_data_table,
    **chest_location_data_table
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}