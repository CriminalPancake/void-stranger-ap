from ..Constants import ItemNames


# Connection Types: Stairs, Shortcut, Dungeon

# floor_order: has ordered list of floors, each with {"Floors": region, "Connections": [], "Last_Smiler": "", "Last_Interface": "", "Chest_Score": 0, "Access_Cost": 0, "Accessible": False}

# RequiredBranes = all brand rooms, all mural rooms, tail's room, gor's room, room 0, etc

# reorganize to be modular, with each room pack it's own modular file
# maybe each floor pack has a type? Like, some might be entire domains unshuffled, and it just swaps the domain in for another domain?
# others might be party collections of various floor types
# keep it at 8 brand carves per seed, but maybe allow more than 8 rooms?

# RequiredMainBranes
# FillerMainBranes
# RequiredSideBranes
# FillerSideBranes
# Brand Rooms
# ImportantBranes? (include all or none)

VanillaBraneOrder = [
        "B000","B001","B002","B003","B004","B005","B006","B007","B008","B009","B010","B011","B012","B013","B014","B015","B016","B017","B018","B019",
        "B020","B021","B022","B023","B024","B025","B026","B027","B028","B029","B030","B031","B032","B033","B034","B035","B036","B037","B038","B039",
        "B040","B041","B042","B043","B044","B045","B046","B047","B048","B049","B050","B051","B052","B053","B054","B055","B056","B057","B058","B059",
        "B060","B061","B062","B063","B064","B065","B066","B067","B068","B069","B070","B071","B072","B073","B074","B075","B076","B077","B078","B079",
        "B080","B081","B082","B083","B084","B085","B086","B087","B088","B089","B090","B091","B092","B093","B094","B095","B096","B097","B098","B099",
        "B100","B101","B102","B103","B104","B105","B106","B107","B108","B109","B110","B111","B112","B113","B114","B115","B116","B117","B118","B119",
        "B120","B121","B122","B123","B124","B125","B126","B127","B128","B129","B130","B131","B132","B133","B134","B135","B136","B137","B138","B139",
        "B140","B141","B142","B143","B144","B145","B146","B147","B148","B149","B150","B151","B152","B153","B154","B155","B156","B157","B158","B159",
        "B160","B161","B162","B163","B164","B165","B166","B167","B168","B169","B170","B171","B172","B173","B174","B175","B176","B177","B178","B179",
        "B180","B181","B182","B183","B184","B185","B186","B187","B188","B189","B190","B191","B192","B193","B194","B195","B196","B197","B198","B199",
        "B200","B201","B202","B203","B204","B205","B206","B207","B208","B209","B210","B211","B212","B213","B214","B215","B216","B217","B218","B219",
        "B220","B221","B222","B223","B224","B225","B226","B227","B228","B229","B230","B231","B232","B233","B234","B235","B236","B237","B238","B239",
        "B240","B241","B242","B243","B244","B245","B246","B247","B248","B249","B250","B251","B252","B253","B254","B255"]


# Two shuffle settings. One for which floors: Side, All, etc. The other setting for If Side: Shortcut, Include Brands, Include Dungeons
# copy first N entries to shuffle list, shuffle it, then append the remaining ones in order at the endswith
# then go through mains and if side index, reassign with corrosponding shuffled side
# need to re-order dungeons to end for easier grouping

# use a different system entirely for pools and true random sides, since there will be more sides to choose from and all are random
# no need to combine methods because there is no compeltely random + some vanilla

# for full random sides (and mains) make a list, include all required, then randomly add optional until a certain total is reached
# side exits are a different matter entirely and will be handled in a separate phase as needed
# may need to make sides link to further sides if there are too many
# basically each side entrance slot will have an ordered list of all sides it goes through before the exit
# will need to make list of all slots

# all side slot arrays contain the final destination as the final entry. So Slot 1 Entry 1 points to Slot 1 Entry 2 which may be another side, or if not, is the main brane exit
# Replace shortcuts with tuple ("index", #, Vanilla_Exit_Brane)


VanillaSideMap = [
        "mon_shortcut_1",
        "mon_shortcut_2",
        "mon_shortcut_3",
        "mon_shortcut_4",
        "mon_shortcut_5",
        "beehole_entrance",
        "greedzone_entrance",
        "room_add",
        "room_eus",
        "room_bee",
        "room_mon",
        "room_tan",
        "room_gor",
        "room_lev",
        "room_cif",
        "room_dis"]

# for adding new brand rooms and carvings:
# if key exists in brand_dictionary, append the new carve (from a table of all carves of this new brand) to it's list of possible carves

# can dev and trailer brands be carved in eus' room?
# also add elysum carving, etc

#VanillaBrandConnections = {
#        "add": "room_add",
#        "eus": "room_eus",
#        "bee": "room_bee",
#        "mon": "room_mon",
#        "tan": "room_tan",
#        "gor": "room_gor",
#        "lev": "room_lev",
#        "cif": "room_cif",
#        "dis": "room_dis"}

VanillaBrandCarving = {
        "B023": [("room_add",[[("brand","add"),]]),
                 ("room_gor",[[("brand","gor"),("item", ItemNames.endless_void_rod)]]),
                 ("room_lev",[[("brand","lev"),("item", ItemNames.endless_void_rod)]]),
                 ("room_cif",[[("brand","cif"),("item", ItemNames.endless_void_rod)]])],
        "B053": [("room_add",[[("brand","add"),("item", ItemNames.void_wings)]]),
                 ("room_eus",[[("brand","eus"),]]),
                 ("room_bee",[[("brand","bee"),("item", ItemNames.void_wings)]]),
                 ("room_tan",[[("brand","tan"),("item", ItemNames.void_wings)]]),
                 ("room_lev",[[("brand","lev"),]]),
                 ("room_cif",[[("brand","cif"),("item", ItemNames.void_wings)]])],
        "B067": [("room_add",[[("brand","add"),("item", ItemNames.endless_void_rod)]]),
                 ("room_bee",[[("brand","bee"),]]),
                 ("room_gor",[[("brand","gor"),("item", ItemNames.endless_void_rod)]]),
                 ("room_lev",[[("brand","lev"),("item", ItemNames.endless_void_rod)]]),
                 ("room_cif",[[("brand","cif"),("item", ItemNames.endless_void_rod)]])],
        "B089": [("room_add",[[("brand","add"),("item", ItemNames.endless_void_rod)]]),
                 ("room_eus",[[("brand","eus"),]]),
                 ("room_bee",[[("brand","bee"),("item", ItemNames.endless_void_rod)]]),
                 ("room_mon",[[("brand","mon"),]]),
                 ("room_tan",[[("brand","tan"),]]),
                 ("room_lev",[[("brand","lev"),("item", ItemNames.endless_void_rod)],]),
                 ("room_cif",[[("brand","cif"),("item", ItemNames.endless_void_rod)]])],
        "B137": [("room_add",[[("brand","add"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","add"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]]),
                 ("room_eus",[[("brand","eus"),("item", ItemNames.void_sword)]]),
                 ("room_bee",[[("brand","bee"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","bee"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]]),
                 ("room_mon",[[("brand","mon"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","mon"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]]),
                 ("room_tan",[[("brand","tan"),("idol","killer")],[("brand","tan"),("item",ItemNames.void_sword)]]),
                 ("room_gor",[[("brand","gor"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","gor"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]]),
                 ("room_lev",[[("brand","lev"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","lev"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]]),
                 ("room_cif",[[("brand","cif"),("item", ItemNames.endless_void_rod),("idol","killer")],[("brand","cif"),("item", ItemNames.endless_void_rod),("item",ItemNames.void_sword)]])],
        "B157": [("room_add",[[("brand","add"),]]),
                 ("room_eus",[[("brand","eus"),]]),
                 ("room_bee",[[("brand","bee"),]]),
                 ("room_mon",[[("brand","mon"),]]),
                 ("room_tan",[[("brand","tan"),]]),
                 ("room_gor",[[("brand","gor"),]]),
                 ("room_lev",[[("brand","lev"),]]),
                 ("room_cif",[[("brand","cif"),]])],
        "B179": [("room_lev",[[("brand","lev"),("idol","watcher")]])],
        "B223": [("room_cif",[[("brand","cif"),]])],
        "B227": [("room_add",[[("brand","add"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword)]]),
                 ("room_eus",[[("brand","eus"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword)]]),
                 ("room_bee",[[("brand","bee"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword)]]),
                 ("room_mon",[[("brand","mon"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword)]]),
                 ("room_tan",[[("brand","tan"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword)]]),
                 ("room_gor",[[("brand","gor"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword),("item", ItemNames.endless_void_rod)]]),
                 ("room_lev",[[("brand","lev"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword),("item", ItemNames.endless_void_rod)]]),
                 ("room_cif",[[("brand","cif"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword),("item", ItemNames.endless_void_rod)]]),
                 ("room_dis",[[("brand","dis"),("idol","killer"),("item", ItemNames.void_wings),("item", ItemNames.void_sword),("item", ItemNames.endless_void_rod)]])],
        }

RequiredMainBranes = {
        "B000": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B002": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B030": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B143": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                [("idol","smiler")]]},
        # murals
        "B001": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B029": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("brand","eus")]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B057": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","bee")]])},
        "B085": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","mon")]])},
        "B113": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","tan")]])},
        "B141": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","gor")]])},
        "B169": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","lev")]])},
        "B197": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","cif")]])},
        "B225": {"Chest_Score": 0,
                "Stairs":       ("next",[
                                    [("brand","dis")]]),
                "Shortcut":     [("deadend_entrance",[[]])]},
        
        # trees
        "B028": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B056": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B084": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B112": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B140": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B168": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B196": {"Chest_Score": 0, "Stairs": ("next",[[]]), # also a mon floor
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B224": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        # brand rooms
        "B023": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B053": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B067": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B089": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B137": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B157": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B179": {"Chest_Score": 1, "Stairs": ("next",[[]]), "Brand_Room": True},
        "B223": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True, "Skipped": True},
        "B227": {"Chest_Score": 0, "Stairs": ("next",[[]]), "Brand_Room": True},
        # mon floors
        "B004": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B044": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B086": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B124": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        }

# B077's locust chest can be tripled and obtained without burdens, but then the exit cannot be reached.
# Thus, logic expects you to triple it and then die, resulting in a chest_score of 2.
OptionalMainBranes = {
        "B003": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B005": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B006": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B007": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Shortcut":    [("mon_shortcut_1",[
                                    [("shortcut","mon1")]])]},
        "B008": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B009": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B010": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B011": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B012": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B013": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B014": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B015": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B016": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B017": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B018": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B019": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B020": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B021": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B022": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B024": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B025": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B026": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B027": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B031": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B032": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B033": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B034": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B035": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B036": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B037": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Shortcut":    [("mon_shortcut_2",[
                                    [("shortcut","mon2")]])]},
        "B038": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B039": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]],
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B040": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B041": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B042": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B043": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B045": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B046": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B047": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B048": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B049": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B050": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B051": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B052": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B054": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B055": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B058": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B059": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B060": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B061": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B062": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B063": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B064": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B065": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B066": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B068": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B069": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B070": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B071": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B072": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B073": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B074": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]],
                 "Statues":     {"smiler":[[]]}},
        "B075": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B076": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B077": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B078": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B079": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B080": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B081": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B082": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B083": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Shortcut":    [("mon_shortcut_3",[
                                    [("shortcut","mon3")]])]},
        "B087": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B088": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B090": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B091": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B092": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B093": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("item",ItemNames.void_wings)]]},
        "B094": {"Chest_Score": 1, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]],
                 "Statues":     {"smiler":[[]]}},
        "B095": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B096": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B097": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B098": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B099": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B100": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B101": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B102": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B103": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B104": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B105": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B106": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B107": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B108": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B109": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B110": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B111": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B114": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B115": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B116": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B117": {"Chest_Score": 1, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("item",ItemNames.void_wings)]]},
        "B118": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B119": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B120": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B121": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B122": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B123": {"Chest_Score": 1,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B125": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B126": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B127": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B128": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B129": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B130": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Statues":     {"killer":[[]]}},
        "B131": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Shortcut":    [("mon_shortcut_4",[
                                    [("shortcut","mon4"),("idol","killer")]])],
                 "Statues":     {"killer":[[]]}},
        "B132": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B133": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B134": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B135": {"Chest_Score": 1, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B136": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B138": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B139": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B142": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B144": {"Chest_Score": 1, "Stairs": ("next",[[]]),
                 "Shortcut":    [("beehole_entrance",[[]])]},
        "B145": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Smiler":      [
                                [("idol","smiler")]]},
        "B146": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B147": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B148": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B149": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B150": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B151": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B152": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B153": {"Chest_Score": 0, 
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B154": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B155": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B156": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B158": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B159": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B160": {"Chest_Score": 2, "Stairs": ("next",[[]])},
        "B161": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B162": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B163": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Shortcut":    [("mon_shortcut_5",[
                                    [("shortcut","mon5")]])]},
        "B164": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B165": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B166": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B167": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B170": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B171": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B172": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B173": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B174": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B175": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B176": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B177": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B178": {"Chest_Score": 2, "Stairs": ("next",[[]])},
        "B180": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B181": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]])},
        "B182": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B183": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B184": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B185": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B186": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","watcher")],
                                    [("item",ItemNames.void_wings)],
                                    [("item",ItemNames.void_sword)]]),
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B187": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","watcher")]])},
        "B188": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")],[("item",ItemNames.void_wings)]])},
        "B189": {"Chest_Score": 3, "Stairs": ("next",[[]])},
        "B190": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B191": {"Chest_Score": 1, "Stairs": ("next",[[]])},
        "B192": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B193": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Shortcut":    [("greedzone_entrance",[[]])],
                 "Smiler":      [
                                    [("idol","smiler")]]},
        "B194": {"Chest_Score": 0,
                 "Stairs":      ("next",
                                    [[("idol","watcher")]])},
        "B195": {"Chest_Score": 4, "Stairs": ("next",[[]])},
        "B198": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B199": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("item",ItemNames.void_wings)]]},
        "B200": {"Chest_Score": 3, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B201": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B202": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B203": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","watcher")]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("idol","watcher"),("item",ItemNames.void_wings)],
                                    [("item",ItemNames.interface_manip),("idol","watcher"),("item",ItemNames.endless_void_rod)]]},
        "B204": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B205": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B206": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B207": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("item",ItemNames.void_wings)]]},
        "B208": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B209": {"Chest_Score": 3, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]],
                 "Statues":     {"killer":[[]]}},
        "B210": {"Chest_Score": 3, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B211": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B212": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B213": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B214": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B215": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B216": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B217": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("idol","killer")]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B218": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B219": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B220": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B221": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B222": {"Chest_Score": 0, "Stairs": ("next",[[]]),
                 "Interface":   [
                                    [("item",ItemNames.interface_manip),("item",ItemNames.void_wings)]]},
        "B226": {"Chest_Score": 0, "Stairs": ("next",[[]])},
        "B228": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B229": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B230": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B231": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B232": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B233": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B234": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B235": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B236": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B237": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B238": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B239": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B240": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B241": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B242": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B243": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B244": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B245": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B246": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B247": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B248": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B249": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B250": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B251": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B252": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B253": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B254": {"Chest_Score": 0, "Stairs": ("next",[[]]),         
                 "Interface":   [
                                    [("item",ItemNames.interface_manip)]]},
        "B255": {"Chest_Score": 0,
                 "Stairs":      ("next",[
                                    [("item",ItemNames.void_wings)]])},
        }

RequiredSideBranes = {
        "room_add": {"Chest_Score": 0, "Stairs": ("B025",[[]])},
        "room_eus": {"Chest_Score": 0, "Stairs": ("B055",[[]])},
        "room_bee": {"Chest_Score": 0, "Stairs": ("B071",[[]])},
        "room_mon": {"Chest_Score": 0, "Stairs": ("B111",[[]])},
        "room_tan": {"Chest_Score": 0,
                     "Stairs":      ("B140",[
                                        [("item",ItemNames.void_sword),("idol","killer")]])},
        "room_gor": {"Chest_Score": 0, "Stairs": ("B162",[[]])},
        "room_lev": {"Chest_Score": 0,
                     "Stairs":      ("B181",[
                                        [("item",ItemNames.void_wings)],
                                        [("idol","watcher")]])},
        "room_cif": {"Chest_Score": 0, "Stairs": ("B224",[[]])},
        }

OptionalSideBranes = {
        "mon_shortcut_1": {"Chest_Score": 0, "Stairs": ("B023",[[]])},
        "mon_shortcut_2": {"Chest_Score": 0, "Stairs": ("B053",[[]])},
        "mon_shortcut_3": {"Chest_Score": 0, "Stairs": ("B109",[[]])},
        "mon_shortcut_4": {"Chest_Score": 0, "Stairs": ("B167",[[]])},
        "mon_shortcut_5": {"Chest_Score": 0, "Stairs": ("B197",[[]])},
        "room_dis": {"Chest_Score": 0,
                     "Stairs":      ("dis",[
                                        [("item",ItemNames.void_wings),("item",ItemNames.void_sword)]])},
        }
        
Dungeons = {
        "deadend_entrance": {"Chest_Score": 0,
                 "Stairs":      ("deadend",[
                                    [("item",ItemNames.void_orange)]]),
                 "Dungeon": "deadend"},
        "deadend": {"Chest_Score": 0, "Stairs": False,
                 "Dungeon": "deadend"},
        "whitevoid": {"Chest_Score": 0, "Stairs": False,
                 "Dungeon": "include"},
        "beehole_entrance": {"Chest_Score": 0, "Stairs": ("B146",[[]]),
                 "Shortcut":    [("beehole",[
                                    [("item",ItemNames.void_sword)]])],
                 "Dungeon": "beehole"},
        "beehole": {"Chest_Score": 0, "Stairs": False,
                 "Dungeon": "beehole"},
        "greedzone_entrance": {"Chest_Score": 0, "Stairs": ("B195",[[]]),
                 "Shortcut":    [("greedzone",[
                                    [("item",ItemNames.void_wings),("item",ItemNames.void_sword)]])],
                 "Dungeon":     "greedzone"},
        "greedzone": {"Chest_Score": 0, "Stairs": False,
                 "Dungeon": "greedzone"},
        "dis": {"Chest_Score": 0, "Stairs": False,
                 "Dungeon": "dis"},
        }

# 1) include all dungeons "floors"
# 2) if vanilla dungeon exists or if shuffle floors is off, include the vanilla entrance floor
# 3) new dungeons need shuffle floors anyway
# 4) if shuffle true, check "dungeon" tag in entrances list, and if dungeon in dungeon list, include, else exclude
# 5) if "dungeon" tag is "include", always include it
# 6) put entrances in with dungeons list
# 7) may need to move dungeon entrance connection from "shortcut" tag to new tag after shuffle floors inplemented