import redis

r = redis.Redis()

#keys corresponding to tables
headwear = range(2695,3393)

#Query 18
results18 = []
for key in headwear:
    elem_decoded = r.hmget(key,'DIY')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == 'No') and (elem_decoded1 == 'Gulliver'):
        result18 = []
        result18.append(r.hmget(key,'Name')[0].decode())
        result18.append(r.hmget(key,'Variation')[0].decode())
        result18.append(r.hmget(key,'Buy')[0].decode())
        result18.append(r.hmget(key,'Sell')[0].decode())
        result18.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result18.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result18.append(r.hmget(key,'Color_1')[0].decode())
        result18.append(r.hmget(key,'Color_2')[0].decode())
        result18.append(r.hmget(key,'Label_Themes')[0].decode())
        result18.append(r.hmget(key,'Style')[0].decode())
        result18.append(r.hmget(key,'Type')[0].decode())
        results18.append(result18)
print("Query 18 :", results18)