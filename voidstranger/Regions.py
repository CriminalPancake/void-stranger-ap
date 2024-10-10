from typing import Dict, List, NamedTuple

class VoidStrangerRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, VoidStrangerRegionData] = {
    "Menu": VoidStrangerRegionData(["Void"]),
    "Void": VoidStrangerRegionData(),
}