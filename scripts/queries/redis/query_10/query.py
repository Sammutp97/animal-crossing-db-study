import redis

r = redis.Redis()

#keys corresponding to tables
bottoms = range(472,1198)

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