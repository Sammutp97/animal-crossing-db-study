import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)
achievements = range(222,306)
art = range(306,376)
bags = range(376,472)
bottoms = range(472,1198)
construction = range(1198,1434)
dress_up = range(1434,2347)
fencing = range(2347,2366)
fish = range(2366,2446)
floors = range(2446,2622)
fossils = range(2622,2695)
headwear = range(2695,3393)
housewares = range(3393,6668)
insects = range(6668,6748)
miscellaneous = range(6748,8055)
music = range(8055,8153)
other = range(8153,8506)
photos = range(8506,11634)
posters = range(11634,12086)
reactions = range(12086,12130)
recipes = range(12130,12725)
rugs = range(12725,12857)
shoes = range(12857,13311)
socks = range(13311,13661)
tools = range(13661,13861)
tops = range(13861,14982)
umbrellas = range(14982,15049)
villagers = range(15049,15440)
wall_mounted = range(15440,15898)
wallpaper = range(15898,16145)

#Query 1
results1 = []
for key in accessories :
    elem = r.hmget(key,'DIY')
    result1 = []
    if elem[0].decode() == 'Yes' :
        result1.append((r.hmget(key,'Name'))[0].decode())
        result1.append((r.hmget(key,'Variation'))[0].decode())
        result1.append((r.hmget(key,'Sell'))[0].decode())
        result1.append((r.hmget(key,'Miles_Price'))[0].decode())
        result1.append((r.hmget(key,'Seasonal_Availability'))[0].decode())
        result1.append((r.hmget(key,'Villager_Equippable'))[0].decode())
        result1.append((r.hmget(key,'Color_1'))[0].decode())
        result1.append((r.hmget(key,'Color_2'))[0].decode())
        results1.append(result1)
print("Query 1 : ",results1)

#Query 2
list_sell = []
for key in accessories :
    elem = r.hmget(key,'Sell')
    list_sell.append(int(elem[0].decode()))
results2 = sum(list_sell)/len(list_sell)
print("Query 2 :", results2)

#Query 3
list_profit = []
for key in accessories :
    elem = r.hmget(key,'Buy')
    if elem[0].decode() != '-1':
        sell_price = r.hmget(key,'Sell')
        list_profit.append(int(sell_price[0].decode()) - int(elem[0].decode()))
results3 = sum(list_profit)/len(list_profit)
print("Query 3 :", results3)

#Query 4
result4 = []
max_profit = -1000
max_idx = 0
for key in accessories :
    elem = r.hmget(key,'Buy')
    if elem[0].decode() != '-1':
        sell_price = r.hmget(key,'Sell')
        profit = int(sell_price[0].decode()) - int(elem[0].decode())
        if profit > max_profit :
            max_profit = profit
            max_idx = key
result4.append((r.hmget(max_idx,'Name'))[0].decode())
result4.append((r.hmget(max_idx,'Variation'))[0].decode())
result4.append((r.hmget(key,'Source'))[0].decode())
result4.append(max_profit)
print("Query 4 :", result4)

#Query 5
results5 = []
for key in accessories :
    elem = r.hmget(key,'DIY')
    if elem[0].decode() == 'Yes' :
        elem_name = r.hmget(key,'Name')[0].decode()
        for key2 in recipes :
            elem_name2 = r.hmget(key2,'Name')[0].decode()
            if elem_name == elem_name2 :
                result5 = []
                result5.append(elem_name2)
                result5.append((r.hmget(key2,'#1'))[0].decode())
                result5.append((r.hmget(key2,'Material_1'))[0].decode())
                result5.append((r.hmget(key2,'#2'))[0].decode())
                result5.append((r.hmget(key2,'Material_2'))[0].decode())
                result5.append((r.hmget(key2,'#3'))[0].decode())
                result5.append((r.hmget(key2,'Material_3'))[0].decode())
                result5.append((r.hmget(key2,'#4'))[0].decode())
                result5.append((r.hmget(key2,'Material_4'))[0].decode())
                result5.append((r.hmget(key2,'#5'))[0].decode())
                result5.append((r.hmget(key2,'Material_5'))[0].decode())
                result5.append((r.hmget(key2,'#6'))[0].decode())
                result5.append((r.hmget(key2,'Material_6'))[0].decode())
                results5.append(result5)
print("Query 5 :", results5)

#Query 6
result6 = set()
for key in accessories :
    elem = r.hmget(key,'Variation')
    result6.add(elem[0].decode())
print("Query 6 :", sorted(result6))

#Query 7
results7 = []
for key in achievements :
    result7 = []
    result7.append((r.hmget(key,'#'))[0].decode())
    result7.append((r.hmget(key,'Name'))[0].decode())
    result7.append((r.hmget(key,'Award_Criteria'))[0].decode())
    elem_decoded = r.hmget(key,'Num_of_Tiers')[0].decode()
    result7.append(elem_decoded)
    if elem_decoded == '1' :
        result7.append(r.hmget(key,'Tier_1')[0].decode())
        result7.append(r.hmget(key,'Reward_Tier_1')[0].decode())
    if elem_decoded == '2' :
        result7.append(r.hmget(key,'Tier_2')[0].decode())
        result7.append(int((r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())))
    if elem_decoded == '3' :
        result7.append(r.hmget(key,'Tier_3')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())))
    if elem_decoded == '4' :
        result7.append(r.hmget(key,'Tier_4')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())) + int((r.hmget(key,'Reward_Tier_4')[0].decode())))
    if elem_decoded == '5' :
        result7.append(r.hmget(key,'Tier_5')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())) + int((r.hmget(key,'Reward_Tier_4')[0].decode())) + int((r.hmget(key,'Reward_Tier_5')[0].decode())))
    results7.append(result7)

print("Query 7 :", results7)

#Query 8
results8 = []
for key in art :
    elem_decoded = r.hmget(key,'Size')[0].decode()
    elem_decoded2 = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded3 = r.hmget(key,'HHA_Concept_2')[0].decode()
    elem_decoded4 = r.hmget(key,'Tag')[0].decode()
    if (elem_decoded == '1x1') and (elem_decoded2 == 'expensive') and (elem_decoded3 == 'folk art') and (elem_decoded4 == 'Sculpture') :
        result8 = []
        result8.append(r.hmget(key,'Name')[0].decode())
        result8.append(r.hmget(key,'Category')[0].decode())
        result8.append(r.hmget(key,'Buy')[0].decode())
        result8.append(r.hmget(key,'Sell')[0].decode())
        result8.append(r.hmget(key,'Catalog')[0].decode())
        result8.append(r.hmget(key,'Artist')[0].decode())
        result8.append(r.hmget(key,'Museum_Description')[0].decode())
        results8.append(result8)

print("Query 8 :", results8)

#Query 9 careful this one is much longer than the others
# results9 = []
# search = [accessories, bags, bottoms, dress_up, fencing, floors, headwear, housewares, miscellaneous, other, photos, rugs, shoes, socks, tools, tops, umbrellas, wall_mounted, wallpaper]
# for group in search :
#     results_group9 = []
#     #print(group)
#     for key in group :
#         #print(key)
#         elem = r.hmget(key,'DIY')
#         if elem[0].decode() == 'Yes' :
#             elem_name = r.hmget(key,'Name')[0].decode()
#             for key2 in recipes :
#                 elem_name2 = r.hmget(key2,'Name')[0].decode()
#                 if elem_name == elem_name2 :
#                     result9 = []
#                     result9.append(elem_name2)
#                     result9.append((r.hmget(key2,'#1'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_1'))[0].decode())
#                     result9.append((r.hmget(key2,'#2'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_2'))[0].decode())
#                     result9.append((r.hmget(key2,'#3'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_3'))[0].decode())
#                     result9.append((r.hmget(key2,'#4'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_4'))[0].decode())
#                     result9.append((r.hmget(key2,'#5'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_5'))[0].decode())
#                     result9.append((r.hmget(key2,'#6'))[0].decode())
#                     result9.append((r.hmget(key2,'Material_6'))[0].decode())
#                     results_group9.append(result9)
#     results9.append(results_group9)
#print("Query 9 :", results9) too long to be printed
#print("Query 9 : done")
print("Query 9 : skipped")

#Query 10
results10 = []
for key in bags :
    elem = r.hmget(key,'DIY')
    if elem[0].decode() == 'No' :
        result10 = []
        result10.append(r.hmget(key,'Name')[0].decode())
        result10.append(r.hmget(key,'Variation')[0].decode())
        result10.append(r.hmget(key,'Sell')[0].decode())
        result10.append(r.hmget(key,'Miles_Price')[0].decode())
        result10.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result10.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result10.append(r.hmget(key,'Color_1')[0].decode())
        result10.append(r.hmget(key,'Color_2')[0].decode())
        results10.append(result10)
print("Query 10 :", results10)

#Query 11
results11 = []
for key in bottoms :
    elem_decoded = r.hmget(key,'DIY')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    elem_decoded2 = r.hmget(key,'Label_Themes')[0].decode()
    if (elem_decoded == 'No') and (elem_decoded1 == 'Recycle bin') and (elem_decoded2 == 'goth') :
        result11 = []
        result11.append(r.hmget(key,'Name')[0].decode())
        result11.append(r.hmget(key,'Variation')[0].decode())
        result11.append(r.hmget(key,'Sell')[0].decode())
        result11.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result11.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result11.append(r.hmget(key,'Color_1')[0].decode())
        result11.append(r.hmget(key,'Color_2')[0].decode())
        results11.append(result11)
print("Query 11 :", results11)

#Query 12
results12 = []
for key in construction :
    elem_decoded = r.hmget(key,'Category')[0].decode()
    elem_decoded1 = int(r.hmget(key,'Buy')[0].decode())
    if (elem_decoded == 'Bridge') and (elem_decoded1 < 100000) :
        result12 = []
        result12.append(r.hmget(key,'Name')[0].decode())
        result12.append(r.hmget(key,'Source')[0].decode())
        results12.append(result12)
print("Query 12 :", results12)

#Query 13
results13 = []
for key in dress_up :
    elem_decoded = r.hmget(key,'DIY')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == 'No') and (elem_decoded1 == 'Recycle bin') :
        result13 = []
        result13.append(r.hmget(key,'Name')[0].decode())
        result13.append(r.hmget(key,'Variation')[0].decode())
        result13.append(r.hmget(key,'Sell')[0].decode())
        result13.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result13.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result13.append(r.hmget(key,'Primary_Shape')[0].decode())
        result13.append(r.hmget(key,'Secondary_Shape')[0].decode())
        result13.append(r.hmget(key,'Color_1')[0].decode())
        result13.append(r.hmget(key,'Color_2')[0].decode())
        result13.append(r.hmget(key,'Label_Themes')[0].decode())
        results13.append(result13)
print("Query 13 :", results13)

#Query 14
results14 = []
for key in fencing :
    result14 = []
    result14.append(r.hmget(key,'Name')[0].decode())
    result14.append(r.hmget(key,'Sell')[0].decode())
    result14.append(r.hmget(key,'Source_Notes')[0].decode())
    results14.append(result14)
print("Query 14 :", results14)

#Query 15
results15 = []
for key in fish:
    elem_decoded = r.hmget(key,'Where/How')[0].decode()
    elem_decoded1 = r.hmget(key,'Lighting_Type')[0].decode()
    if (elem_decoded == 'Sea') and (elem_decoded1 == 'Fluorescent') :
        result15 = []
        result15.append(r.hmget(key,'Name')[0].decode())
        result15.append(r.hmget(key,'Sell')[0].decode())
        result15.append(r.hmget(key,'Color_1')[0].decode())
        result15.append(r.hmget(key,'Color_2')[0].decode())
        result15.append(r.hmget(key,'Shadow')[0].decode())
        result15.append(int(r.hmget(key,'Total_Catches_to_Unlock')[0].decode()))
        result15.append(r.hmget(key,'Spawn_Rates')[0].decode())
        result15.append(r.hmget(key,'Rain/Snow_Catch_Up')[0].decode())
        results15.append(result15)
print("Query 15 :", sorted(results15,key = lambda x: x[5]))

#Query 16
results16 = []
for key in floors:
    elem_decoded = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded1 = r.hmget(key,'HHA_Concept_2')[0].decode()
    if (elem_decoded == 'expensive') and (elem_decoded1 == 'facility') :
        result16 = []
        result16.append(r.hmget(key,'Name')[0].decode())
        result16.append(r.hmget(key,'Buy')[0].decode())
        result16.append(r.hmget(key,'Sell')[0].decode())
        result16.append(r.hmget(key,'Catalog')[0].decode())
        result16.append(r.hmget(key,'VFX')[0].decode())
        result16.append(r.hmget(key,'Color_1')[0].decode())
        result16.append(r.hmget(key,'Color_2')[0].decode())
        result16.append(r.hmget(key,'Tag')[0].decode())
        result16.append(r.hmget(key,'Source')[0].decode())
        results16.append(result16)
print("Query 16 :", results16)

#Query 17
results17 = []
for key in fossils:
    elem_decoded = r.hmget(key,'Museum')[0].decode()
    if (elem_decoded == 'Room 2'):
        result17 = []
        result17.append(r.hmget(key,'Name')[0].decode())
        result17.append(r.hmget(key,'Sell')[0].decode())
        result17.append(r.hmget(key,'Color_1')[0].decode())
        result17.append(r.hmget(key,'Color_2')[0].decode())
        result17.append(r.hmget(key,'Size')[0].decode())
        results17.append(result17)
print("Query 17 :", results17)