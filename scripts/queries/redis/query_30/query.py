import redis

r = redis.Redis()

#keys corresponding to tables
socks = range(13311,13661)

#Query 31
results31 = []
for key in socks:
    elem_decoded = r.hmget(key,'DIY')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == 'No') and (elem_decoded1 == 'Kicks'):
        result31 = []
        result31.append(r.hmget(key,'Name')[0].decode())
        result31.append(r.hmget(key,'Variation')[0].decode())
        result31.append(r.hmget(key,'Sell')[0].decode())
        result31.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result31.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result31.append(r.hmget(key,'Color_1')[0].decode())
        result31.append(r.hmget(key,'Color_2')[0].decode())
        result31.append(r.hmget(key,'Label_Themes')[0].decode())
        results31.append(result31)
print("Query 31 :", results31)