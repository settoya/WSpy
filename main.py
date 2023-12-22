import requests
import csv
from threading import Thread
import time

start = time.time()

url = 'https://pixels-server.pixels.xyz/v1/marketplace/listings/count'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
page = requests.get(url, headers=headers)
file = open('js-table-data.csv', 'w')
writer = csv.writer(file)
writer.writerow(['itemname'])
data = page.json()
# all_arrays = data['counts']
# print(len(all_arrays))
# print(data['counts'])

rawRecipe = [
'itm_clover4LeafFruit', 'itm_4_leaf_cloveregano', 'itm_storageChest6Slot', 'itm_archery', 'itm_Space_Chair', 'itm_tentacactus',
'itm_tentacactus_tequila', 'itm_barn', 'itm_barrel01', 'itm_barrel02', 'itm_barrel03', 'itm_Bomb_Shell', 'itm_bones_hut_2',
'itm_brick', 'itm_butterberry', 'itm_butterberry_butterbrew', 'itm_clay', 'itm_Plastic', 'itm_cloverFruit', 'itm_cunstruction_cone',
'itm_constructionPowder', 'itm_cottoncandyshake', 'itm_egg', 'itm_eggsplosive', 'itm_barrel04', 'itm_Fireplace',
'itm_fireplace-pot-decoration', 'itm_flour', 'itm_Glue', 'itm_grainbow', 'itm_grainbow_grainshine', 'itm_tent-v1-01-decoration',
'itm_grumpkinFruit', 'itm_grumpkinPie', 'itm_grumpkingspicedlatte', 'itm_grumpkinwine', 'itm_hard_wood', 'itm_hardwood_smoked_bbq_sauce',
'itm_heartbeetFruit', 'itm_honey', 'itm_honey_bbq_sauce', 'itm_hot_sauce', 'itm_hotato', 'itm_hotato_hotka', 'itm_Iron_Ore',
'itm_Iron_Bar', 'itm_coffeepod', 'itm_log_decoration2', 'itm_hay', 'itm_muckchuck', 'itm_muckchuck_mead', 'itm_pancakes',
'itm_limestone_paving_stones', 'itm_plain_omelet', 'itm_plank', 'itm_plaster', 'itm_popberryFruit', 'itm_popberryLoaf',
'itm_popberryPie', 'itm_popberrywine', 'itm_queenbee', 'itm_Marble', 'itm_tree_sap', 'itm_scarecrow', 'itm_scarrotFruit',
'itm_scarrotLoaf', 'itm_scarrotPie', 'itm_scarrotwine', 'itm_seltsamEgg', 'itm_shorelimeFruit', 'itm_Shrapnel', 'itm_silkcloth',
'itm_silkfiber', 'itm_silkrope', 'itm_silkslugslime', 'itm_silkslugspider', 'itm_small_puprle_rug', 'itm_wood', 'itm_spicy_bbq_sauce',
'itm_Small_Fountain_04',
# 'itm_stick',
'itm_tangy_bbq_sauce', 'itm_traditional_bbq_sauce', 'itm_Trashcan', 'itm_Small_Fountain_03',
'itm_turquoise_Couch',
'itm_void', 'itm_waterland_statue', 'itm_wintermintFruit', 'itm_wintermint_whiskey', 'itm_beeswax',
'itm_Wooden_Stool', 'itm_Wooden_Throne', 'itm_woodenbeam']


def make_request(url, header):
    response = requests.get(url)
    data1 = response.json()
    selected_elements = [
        [sublist['itemId'], sublist['price']]  # Select first and last elements
        for sublist in data1['listings']
        if sublist['currency'] == "cur_berry"  # Filter sublists based on conditions
    ]
    mini = min(selected_elements)
    print(mini)


threads = []


for listitem in rawRecipe:
    modList = str(listitem).replace('[', '').replace(']', '').replace("'", '')
    # print(listItem)
    urlItem = 'https://pixels-server.pixels.xyz/v1/marketplace/item/' + modList
    app = Thread(target=make_request, args=(urlItem, headers))
    app.daemon = False
    threads.append(app)
    app.start()


for thread in threads:
    thread.join()

end = time.time()

time_ended = int(end - start)
print(time_ended)
