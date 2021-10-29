import redis

r = redis.Redis()

#keys corresponding to tables
dress_up = range(1434,2347)

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