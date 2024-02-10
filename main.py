import requests
from threading import Thread
import time
import pyperclip
import traceback

start = time.time()

url = 'https://pixels-server.pixels.xyz/v1/marketplace/listings/count'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

rawRecipe = [
'itm_clover4LeafFruit', 'itm_4_leaf_cloveregano', 'itm_storageChest6Slot', 'itm_archery', 'itm_Space_Chair', 'itm_tenta',
'itm_tentacactus_tequila', 'itm_barn', 'itm_barrel01', 'itm_barrel02', 'itm_barrel03', 'itm_Bomb_Shell', 'itm_bones_hut_2',
'itm_brick', 'itm_butterberry', 'itm_butterberry_butterbrew', 'itm_clay', 'itm_Plastic', 'itm_cloverFruit', 'itm_cunstruction_cone',
'itm_constructionPowder', 'itm_cottoncandyshake', 'itm_egg', 'itm_eggsplosive', 'itm_barrel04', # 'itm_Fireplace',
'itm_fireplace-pot-decoration', 'itm_flour', 'itm_Glue', 'itm_grainbow', 'itm_grainbow_grainshine', 'itm_tent-v1-01-decoration',
'itm_grumpkinFruit', 'itm_grumpkinPie', 'itm_grumpkingspicedlatte', 'itm_grumpkinwine', 'itm_hard_wood', 'itm_hardwood_smoked_bbq_sauce',
'itm_heartbeetFruit', 'itm_honey', 'itm_honey_bbq_sauce', 'itm_hot_sauce', 'itm_hotato', 'itm_hotato_hotka', 'itm_Iron_Ore',
'itm_Iron_Bar', 'itm_coffeepod', 'itm_log_decoration2', 'itm_hay', 'itm_muckchuck', 'itm_muckchuck_mead', 'itm_pancakes',
'itm_limestone_paving_stones', 'itm_plain_omelet', 'itm_plank', 'itm_plaster', 'itm_popberryFruit', 'itm_popberryLoaf',
'itm_popberryPie', 'itm_popberrywine', 'itm_queenbee', 'itm_Marble', 'itm_tree_sap', 'itm_scarecrow', 'itm_scarrotFruit',
'itm_scarrotLoaf', 'itm_scarrotPie', 'itm_scarrotwine', 'itm_seltsamEgg', 'itm_shorelimeFruit', 'itm_Shrapnel', 'itm_silkcloth',
'itm_silkfiber', 'itm_silkrope', 'itm_silkslugslime', 'itm_silkslugspider', 'itm_small_puprle_rug', 'itm_spicy_bbq_sauce',
'itm_Small_Fountain_04',
# 'itm_stick', #'itm_wood',
'itm_tangy_bbq_sauce', 'itm_traditional_bbq_sauce', 'itm_Trashcan', 'itm_Small_Fountain_03',
# 'itm_turquoise_Couch',
'itm_void', 'itm_waterland_statue', 'itm_wintermintFruit', 'itm_wintermint_whiskey', 'itm_beeswax',
'itm_Wooden_Stool', 'itm_Wooden_Throne', 'itm_woodenbeam',
'itm_dry_baby_back_butterberry_ribs', 'itm_dry_honey_kissed_popberry_chops', 'itm_dry_maple_glazed_grumpkin_slabs',
'itm_dry_pulled_muckchuck_platter', 'itm_dry_salt_encrusted_scarrot_skewers', 'itm_moist_broiled_muckchuck_burgers',
'itm_moist_honey_kissed_grumpkin_chops', 'itm_moist_maple_glazed_scarrot_slabs', 'itm_moist_salt_encrusted_popberry_skewers',
'itm_moist_scarrot_butterberry_kebabs', 'itm_starry_butterberry_brisket', 'itm_starry_grilled_hotato_kielbasa',
'itm_starry_honey_kissed_scarrot_chops', 'itm_starry_maple_glazed_popberry_slabs', 'itm_starry_salt_encrusted_grumpkin_skewers'
]

genlist = []

def make_request(urlItem):
    try:
        response = requests.get(urlItem)
        response.raise_for_status()  # Check for request success
        data1 = response.json()
        selected_elements = [
            [sublist['itemId'], sublist['price']]
            for sublist in data1.get('listings', [])  # Added a default value for the case when 'listings' key is missing
            if sublist.get('currency') == "cur_coins"
        ]
        if selected_elements:
            mini = min(selected_elements)
            genlist.append(mini)
        else:
            print(f"No valid listings for item: {urlItem}")
    except Exception as e:
        print(f"Error in thread for item {urlItem}: {e}")
        traceback.print_exc()  # Print traceback for more details

threads = []

for listitem in rawRecipe:
    modList = str(listitem).replace('[', '').replace(']', '').replace("'", '')
    urlItem = 'https://pixels-server.pixels.xyz/v1/marketplace/item/' + modList + '?pid=6565e9eb1cd025b311190154'
    app = Thread(target=make_request, args=(urlItem,))
    app.daemon = False
    threads.append(app)
    app.start()

for thread in threads:
    thread.join()

list_as_string = '\n'.join(str(item).replace(']', '').replace('[', '').replace("'", '') for item in genlist)
print(list_as_string)
pyperclip.copy(list_as_string)

end = time.time()

time_ended = int(end - start)
print(f"Execution time: {time_ended} seconds")

